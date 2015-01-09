# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response
import pdfkit

from Verfahrensverzeichnis import models


def report_pdf(request):
    vz = models.Verfahrensverzeichnis.objects.get(id=1)
    return render_to_response('report_pdf.html',{'vz':vz, 'is_popup':True})

def report(request):
    vz = models.Verfahrensverzeichnis.objects.get(id=1)
    url = request.META['HTTP_HOST']+reverse('report_html')
    pdfkit.from_url(url, 'static/report.pdf')
    return render_to_response('report.html',{'vz':vz,'file':'static/report.pdf'})