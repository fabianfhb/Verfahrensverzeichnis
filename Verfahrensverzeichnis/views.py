# -*- coding: utf-8 -*-
from django.core import urlresolvers
from django.core.urlresolvers import reverse, reverse_lazy

from django.forms import *
from django.contrib.admin.forms import *
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, render_to_response
from django.views.generic import RedirectView
from forms import *
from admin import *

from Verfahrensverzeichnis.models import *

# Create your views here.




def report(request):
    return render(request, 'report.html')


def index(request):
    vl = Verfahrensverzeichnis.objects.get(pk=1)
    return HttpResponsePermanentRedirect(reverse('user_admin_site:Verfahrensverzeichnis_verfahrensverzeichnis_change',args=(1,)))
    #print(vl.datenVerfahren.all())
    #return render(request, 'index.html', {'vl':vl})
