import re
import xml.etree.ElementTree as ET

from googletrans import Translator


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
    translator = Translator()
    to_translate = serialize_text(to_translate)
    try:
        print(to_translate)
        translation = translator.translate(to_translate, dest=output_language, src=input_language)
        return translation.text
    except:
        return to_translate


def perform_translate(xml_file, output_lang, input_lang, fileStatus, session):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    totalElements = len(root)
    status = 1
    # cycle through elements
    for i in range(len(root)):
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
                # for each translatable string call the translation subroutine and replace the string by its translation
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
        status += 1
        percentageStatus = (status / totalElements) * 99
        fileStatus.status = percentageStatus
        fileStatus.save()
    for dataElement in tree.iter('resources'):

        session.translatedText = ET.tostring(dataElement, encoding='unicode')
        session.save()

        fileStatus.status = 100
        fileStatus.save()
