from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from rest_framework import generics, viewsets

from .models import RawData, Interactions, DataPlot, Transitions
from .forms import RawDataForm, EditInteractionsForm
from .functions import *
from .serializers import *

import pandas as pd

threshold = 1
behavior = 'shell'
show_grid = True


def entry(request):
    if request.method == 'POST':
        form = RawDataForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
    else:
        form = RawDataForm()

    return render(request, 'entry.html', {'form': form})

def success(request):
    # upload data
    if request.method == 'POST':
        form = RawDataForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
    else:
        form = RawDataForm()

    # handle and clean data
    data = handle_upload(RawData.objects.all().last().media)

    # save interactinos to model
    i = Interactions(image=interaction_network(data, threshold))
    i.save()

    d = DataPlot(image=dataplot(data, behavior, show_grid))
    d.save()

    t = Transitions(image=transition_network(data))
    t.save()

    info = Info(
            preview=preview(data),
            headers=column_headers(data),
            ids=get_fish_ids(data),
            behaviors=data.behavior.unique(),
            categories=data.behavioral_category.unique(),
            )
    info.save()

    #fill data in template and show all
    return render(request, 'success.html', {
        'form': form,
        'preview': preview(data),
        'column_headers': column_headers(data),
        'fish_ids': get_fish_ids(data),
        'behaviors': data.behavior.unique(),
        'behavioral_categories': data.behavioral_category.unique(),
        'data_plot': d.image,
        'interactions': i.image,
        'transitions': t.image,
        })


class RawDataView(viewsets.ModelViewSet):
    queryset = RawData.objects.all()
    serializer_class = RawDataSerializer

class InteractionView(viewsets.ModelViewSet):
    queryset = Interactions.objects.all()
    serializer_class = InteractionsSerializer

class PlotView(viewsets.ModelViewSet):
    queryset = DataPlot.objects.all()
    serializer_class = DataPlotSerializer

class TransitionView(viewsets.ModelViewSet):
    queryset = Transitions.objects.all()
    serializer_class = TransitionsSerializer

class InfoView(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


