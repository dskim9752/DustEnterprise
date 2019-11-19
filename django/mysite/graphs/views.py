# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Jongro_Female_20, Choice, Catname
from django.shortcuts import redirect
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
# Create your views here.
	
def choices(request):
	choices = Choice.objects.get(pk = 1)
	selection = request.POST['buttons']
	choices.category = selection
	choices.save()
	return redirect('/')

def choicelocations(request):
	choicelocations = Choice.objects.get(pk = 1)
	selection = request.POST['buttons']
	choicelocations.location = selection
	choicelocations.save()
	return redirect('/')	
	
class LineChartJSONViewM(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[41, 41, 41, 41, 41, 41, 41],
        		[75, 44, 92, 11, 44, 95, 35]]

class LineChartJSONViewF(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["GOOD", "NORMAL", "BAD", "VERYBAD"]

    def get_providers(self):
        """Return names of datasets."""
        return ["FLAT", "SELLS"]

    def get_data(self):
    	categorys = 1
    	choice = Choice.objects.get(pk=1)	
    	if choice.location == 1:
			datas = Jongro_Female_20.objects.get(pk = 1)
    	elif choice.location == 2:
			datas = Jongro_Female_20.objects.get(pk = 25)
    	categorys = choice.category
        """Return 3 datasets to plot."""

        return [[41, 41, 41, 41],
        		[75, datas.USE_CNT, 75, categorys]]


line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json_m = LineChartJSONViewM.as_view()
line_chart_json_f = LineChartJSONViewF.as_view()

def index(request):
	catchoices = Choice.objects.get(pk = 1)
	catnames = Catname.objects.get(catnumber = catchoices.category)
	context = {'catnames':catnames}
	return render(request, 'graphs/index.html', context)
	

