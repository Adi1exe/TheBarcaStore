from django.core.files.base import ContentFile
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product 
from .forms import ProductForm

def home(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to refresh the page

    else:
        form = ProductForm()
    
    prod = Product.objects.all()
    return render(request, "jersey/home.html", {"prod": prod, "form": form})

def homepage(request):
    return render(request, 'jersey/homepage.html')

def delete_jersey(request, jersey_id):
    jersey = get_object_or_404(Product, id=jersey_id)
    return render(request, 'jersey/delete_confirmation.html', {'jersey': jersey})

def confirm_delete_jersey(request, jersey_id):
    jersey = get_object_or_404(Product, id=jersey_id)
    jersey.delete()
    return redirect('home')

def edit_jersey(request, jersey_id):
    jersey = get_object_or_404(Product, id=jersey_id)
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=jersey)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=jersey)
    
    return render(request, 'jersey/edit_jersey.html', {'form': form, 'jersey': jersey})

def about(request):
    return render(request, 'jersey/about.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"New message from {email}: {message}")
    return render(request, 'jersey/contact.html')