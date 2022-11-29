import json

from django.shortcuts import render

# Create your views here.
from googletrans import Translator

from translate.models import Language, Session
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
        generatedFileName = generate_file_name(10) + '.xml'

        session = Session()
        session.source = src
        session.destination = dest
        session.file_name = generatedFileName
        session.save()

        with open('translate/uploads/' + generatedFileName + '.xml', 'wb+') as destination:
            for chunk in string_file.chunks():
                destination.write(chunk)

    return render(request, "translate/index.html", context)
