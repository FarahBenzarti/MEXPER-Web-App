from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Alls, net
from django.urls import reverse

#views.py catch the request and reference to the html file


def net(request, net_inc):
    response = "You net earnings are: %0.2f."
    return HttpResponse(response % net_inc)

def upcoming(request):
    Upcoming_pay = Alls.objects.order_by('-pub_date')
    template = loader.get_template('split/upcoming.html')
    #The context is a dictionary mapping template variable names to Python objects
    context = {
        'Upcoming_Payments': Upcoming_pay,
    }
    return HttpResponse(template.render(context, request))
    
