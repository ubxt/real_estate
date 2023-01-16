from django.shortcuts import render
from .models import Listing


def listing_list(request):
    queryset = Listing.objects.all()
    context = {"listings": queryset}
    return render(request=request, template_name="listings.html", context=context)
