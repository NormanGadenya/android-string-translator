import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, resolve_url

# Create your views here.
from translate.textProcessor import *
from translate.utils import *


def home(request):
    context = {'languages': get_languages_and_codes()}
    if request.method == 'POST':
        src = request.POST['source_language']
        dest = request.POST['destination_language']
        files = request.FILES
        string_file = files['string_file']  # returns a dict-like object
        generatedFileName = generate_file_name(10)

        session = Session()
        session.source = src
        session.destination = dest
        session.old_file_name = generatedFileName
        session.save()

        with open('translate/uploads/' + generatedFileName + '.xml', 'wb+') as destination:
            for chunk in string_file.chunks():
                destination.write(chunk)
        return redirect(resolve_url(processing, session.pk))

    return render(request, "translate/index.html", context)


def translateText(fileName, fileStatus):
    xml_file_name = fileName + '.xml'
    session = fileStatus.session
    perform_translate('translate/uploads/' + xml_file_name, input_lang=session.source, output_lang=session.destination,
                      session_pk=session.pk)
    os.remove('translate/uploads/' + xml_file_name)


def processing(request, pk):
    session = Session.objects.get(pk=pk)
    sourceLanguage = get_language_by_code_name(session.source)
    destinationLanguage = get_language_by_code_name(session.destination)
    context = {
        'session': session,
        'sourceLanguage': sourceLanguage,
        'destinationLanguage': destinationLanguage,
        'fileName': session.old_file_name,
    }

    fileStatus = FileStatus()
    fileStatus.status = 0
    fileStatus.session = session
    fileStatus.save()
    thread = Thread(target=translateText, args=(session.old_file_name, fileStatus))
    thread.start()

    return render(request, 'translate/processing.html', context)


def get_file_status(request, fileName):
    if request.method == 'GET':
        session = Session.objects.get(old_file_name=fileName)
        fileStatus = FileStatus.objects.filter(session=session)
        status = fileStatus.values().first()['status']
        state = {'status': '{:0.2f}'.format(status)}
        return JsonResponse(state, safe=False, status=200)


def download_generated(request, fileName):
    if request.method == 'GET':
        session = Session.objects.get(old_file_name=fileName)
        response = HttpResponse(content_type='text/xml')
        generatedFileName = 'strings_' + session.destination + '.xml'
        response['Content-Disposition'] = 'attachment; filename=' + generatedFileName
        response.write(session.translatedText)
        return response


def completed_page(request, pk):
    session = Session.objects.get(pk=pk)
    context = {'fileName': session.old_file_name}
    return render(request, 'translate/completed.html', context)


def edit_generated(request, fileName):
    session = Session.objects.get(old_file_name=fileName)
    context = {'translated_content': session.translatedText}
    if request.method == 'POST':
        stringText = request.POST['string_text']
        session.translatedText = stringText
        session.save()
        return redirect(resolve_url(completed_page, session.pk))
    return render(request, 'translate/edit_generated.html', context)
