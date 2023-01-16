from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


def listing_list(request):
    queryset = Listing.objects.all()
    context = {"listings": queryset}
    return render(request=request, template_name="listings.html", context=context)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(pk=pk)
    context = {"listing": listing}
    return render(request, "listing.html", context)


def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/listings")
    else:
        form = ListingForm()

    context = {"form": form}
    return render(request, "listing_create.html", context)


def listing_update(request, pk):
    listing = Listing.objects.get(pk=pk)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("/listings")
    else:
        form = ListingForm(instance=listing)

    context = {"form": form}
    return render(request, "listing_update.html", context)


def listing_delete(request, pk):
    listing = Listing.objects.get(pk=pk)
    listing.delete()
    return redirect("/listings")
