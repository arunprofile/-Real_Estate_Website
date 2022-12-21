from django.shortcuts import redirect, render
from .models import Listings
from .forms import ListingsForm

# Create your views here.
 

#create a function to perform tasks on django
def listing_list(request):
    listings = Listings.objects.all()
    context = {
        "listings": listings
    }                         #here we pass request(information) that comes from either user or browser.
    return render(request,'listings.html', context)

def listing_retrieve(request,pk):
    listing = Listings.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request,'index.html',context)

def listing_create(request):
    form = ListingsForm()
    if request.method == "POST":
        form = ListingsForm(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
           form.save()
           return redirect("/")

    context ={
        "form" : form
    }

    return render(request,"listing_create.html",context)

def listing_update(request,pk):
    listing = Listings.objects.get(id=pk)
    form = ListingsForm(instance=listing)

    if request.method == "POST":
        form = ListingsForm(request.POST,instance=listing,files = request.FILES)
        if form.is_valid():
           form.save()
           return redirect("/")

    context ={
        "form" : form
    }

    return render(request,"listing_update.html",context)

def listing_delete(request,pk):
    listing = Listings.objects.get(id=pk)
    listing.delete()
    return redirect("/")
