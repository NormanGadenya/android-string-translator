import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.core import serializers
# Create your views here.
from googletrans import Translator

from translate.models import Language, Session, FileStatus
from translate.utils import generate_file_name


def home(request):
    # translator = Translator()
    # list = ['The quick brown fox', 'jumps over', 'the lazy dog']
    # translations = translator.translate(json.dumps(list) , dest='ko')
    # for translation in translations:
    #     print(translation.origin, ' -> ', translation.text)
    context = {'languages': Language.objects.all()}
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


def processing(request, pk):
    session = Session.objects.get(pk=pk)
    sourceLanguage = Language.objects.filter(code__icontains=session.source)
    destinationLanguage = Language.objects.filter(code__icontains=session.destination)
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

    return render(request, 'translate/processing.html', context)


def get_file_status(request, fileName):
    if request.method == 'GET':
        session = Session.objects.get(old_file_name=fileName)
        fileStatus = FileStatus.objects.filter(session=session)
        status = fileStatus.values().first()['status']

        state = {'status': status}
        return JsonResponse(state, safe=False, status=200)


def edit_generated(request, fileName):
    session = Session.objects.get(old_file_name=fileName)
    #Todo change old file name to new file name
    xml_file = fileName + '.xml'
    f = open('translate/uploads/' + xml_file, "r")
    context = {'translated_content': f.read()}
    if request.method == 'POST':
        stringText = request.post['string_text']

        response = HttpResponse(content_type='text/xml')
        response['Content-Disposition'] = 'attachment; filename="string.xml"'
        #Todo fix this issue of downloading files
        response.write(stringText)

        return response
    return render(request, 'translate/edit_generated.html', context)
