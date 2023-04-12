from django.shortcuts import render
from django.http import HttpResponse
# Importe le modèle des groupes de musiques :
from listings.models import Band, Listing
from django.shortcuts import render


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})


def about(request):
    return HttpResponse('<h1>À propos</h1>')


def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})


def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})


def contact(request):
    return render(request, 'listings/contact.html')
