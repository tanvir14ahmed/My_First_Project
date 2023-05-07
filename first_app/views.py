from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView


class IndexView(TemplateView):
    template_name = 'first_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sample_text_1"] = "First Text"
        context["sample_text_2"] = "Second Text"
        return context

class ContactPage(TemplateView):
    template_name = 'first_app/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["intro"] = "This is our contact page"
        return context
