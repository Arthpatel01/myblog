import os

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from abp_globle import Tools
from myblog.settings import BASE_DIR


# Create your views here.

class TextToSpeech(CreateView):
    template_name = "text_to_speech.html"

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text_input', None)
        if text:
            t = Tools()
            file_path = t.text_to_speech(text=text)
            if file_path:
                return render(request, self.template_name, context={'file_path': file_path})

        return redirect("text_to_speech")

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request=request, template_name=self.template_name, context=context)
