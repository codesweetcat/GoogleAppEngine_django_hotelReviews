# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "hotelsite/home.html")


def about(request):
    return render(request, "hotelsite/about.html")


def reviews(request):
    return render(request, "hotelsite/reviews.html")