from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class homeview(TemplateView):
    template_name='Home/welcome.html'
    extra_context={'today':datetime.today()}

class Authorize(LoginRequiredMixin,TemplateView):
    template_name="Home/authorize.html"
    login_url='/admin'