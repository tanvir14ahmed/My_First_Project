from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, DetailView, CreateView
from first_app import models

class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.html'


class ContactPage(TemplateView):
    template_name = 'first_app/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["intro"] = "This is our contact page"
        return context

class MusicianDetail(DetailView):
    model = models.Musician
    context_object_name = 'musician'
    template_name = 'first_app/musician_details.html'

class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'first_app/musician_form.html'
