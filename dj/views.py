from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.views.generic.edit import CreateView

from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin ## NEW
# Create your views here.

class Home(View):

    def get(self, request):
        return render(request, 'dj/home.html')