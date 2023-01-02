import math
import re
import xml.etree.ElementTree as ET
from threading import Thread

import translators as ts

from translate.models import Session, FileStatus


def serialize_text(text):
    if text is not None:
        tag_match_regex = re.compile('<.*?>')
        text = re.sub(tag_match_regex, '', text)  # Remove all html tags from text
        text = text.replace("\\n", "\n")  # Replace "\" "n" with next line character
        text = text.replace("\\'", "'")  # Replace \' with '
        text = text.replace("\\@", "@")  # Replace \@ with @
        text = text.replace("\\?", "?")  # Replace \? with ?
        text = text.replace("\\\"", "\"")  # Replace \" with "
    return text


def translate_internal(to_translate, input_language="auto", output_language="auto"):

        print(to_translate)
        to_translate = serialize_text(to_translate)
        return ts.translate_text(query_text=to_translate, translator='bing', from_language=input_language, to_language=output_language)


def process_translation_by_range_of_elements(root, output_lang, input_lang, start_at, end_at, session_pk, total_elements):
    for i in range(start_at,end_at):
        isTranslatable = root[i].get('translatable')
        if (root[i].tag == 'string') & (isTranslatable != 'false'):
            toTranslate = root[i].text

            if toTranslate is not None:
                root[i].text = translate_internal(toTranslate, output_language=output_lang, input_language=input_lang)

            if len(root[i]) != 0:
                for element in range(len(root[i])):
                    if root[i][element].text is not None:
                        root[i][element].text = " " + translate_internal(root[i][element].text, output_language=output_lang,
                                                                     input_language=input_lang)
                    if root[i][element].tail is not None:
                        root[i][element].tail = " " + translate_internal(root[i][element].tail, output_language=output_lang,
                                                                     input_language=input_lang)
        if root[i].tag == 'string-array':
            for j in range(len(root[i])):
                isTranslatable = root[i][j].get('translatable')
                if (root[i][j].tag == 'item') & (isTranslatable != 'false'):
                    # translate text and fix any possible issues translator creates
                    toTranslate = root[i][j].text
                    if toTranslate is not None:
                        root[i][j].text = translate_internal(toTranslate, output_language=output_lang,
                                                             input_language=input_lang)

                    # if string was broken down due to HTML tags, reassemble it
                    if len(root[i][j]) != 0:
                        for element in range(len(root[i][j])):
                            if root[i][j][element].text is not None:
                                root[i][j][element].text = " " + translate_internal(root[i][j][element].text,
                                                                                    output_language=output_lang,
                                                                                    input_language=input_lang)
                            if root[i][j][element].tail is not None:
                                root[i][j][element].tail = " " + translate_internal(root[i][j][element].tail,
                                                                                    output_language=output_lang,
                                                                                    input_language=input_lang)
        current_session = Session.objects.get(pk=session_pk)
        current_status = FileStatus.objects.get(session=current_session)
        current_percentage = current_status.status
        number_of_elements_translated = (current_percentage / 99) * total_elements
        number_of_elements_translated += 1.0
        percentageStatus = (number_of_elements_translated / total_elements) * 99
        current_status.status = percentageStatus
        current_status.save()


def perform_translate(xml_file, output_lang, input_lang, session_pk):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    totalElements = len(root)

    ending_position_first = math.floor(totalElements/2)
    starting_position_second = totalElements - ending_position_first

    # split string file into two and perform translation in two threads
    thread_1st_half = Thread(target=process_translation_by_range_of_elements, args=(root, output_lang, input_lang, 0,
                                                                                    ending_position_first, session_pk,
                                                                                    totalElements))
    thread_1st_half.start()
    thread_2nd_half = Thread(target=process_translation_by_range_of_elements,
                             args=(root, output_lang, input_lang, starting_position_second, totalElements, session_pk,
                                   totalElements))
    thread_2nd_half.start()

    thread_1st_half.join()
    thread_2nd_half.join()

    if not (thread_1st_half.is_alive() and thread_2nd_half.is_alive()):
        current_session = Session.objects.get(pk=session_pk)
        current_status = FileStatus.objects.get(session=current_session)

        for dataElement in tree.iter('resources'):
            current_session.translatedText = ET.tostring(dataElement, encoding='unicode')
            current_session.save()

            current_status.status = 100
            current_status.save()


