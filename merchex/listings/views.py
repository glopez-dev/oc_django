from django.shortcuts import render
from django.http import HttpResponse
# Importe le modèle des groupes de musiques :
from listings.models import Band, Listing
from django.shortcuts import render


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})


def about(request):
    return HttpResponse('<h1>À propos</h1>')


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})


def contact(request):
    return render(request, 'listings/contact.html')
