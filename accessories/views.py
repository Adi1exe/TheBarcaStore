from django.shortcuts import render, redirect, get_object_or_404
from .models import Accessory
from .forms import AccessoryForm

def accessories_page(request):
    """Display all accessories and handle form submission for adding new accessories."""
    if request.method == "POST":
        form = AccessoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accessories')  # Redirect to prevent resubmission
    else:
        form = AccessoryForm()

    accessories = Accessory.objects.all()
    return render(request, 'accessories/accessories.html', {'form': form, 'accessories': accessories})

def confirm_delete_accessory(request, accessory_id):
    """Show confirmation page before deleting an accessory."""
    accessory = get_object_or_404(Accessory, id=accessory_id)
    return render(request, 'accessories/confirm_delete_accessory.html', {'accessory': accessory})


def edit_accessory(request, accessory_id):
    """Edit an existing accessory."""
    accessory = get_object_or_404(Accessory, id=accessory_id)
    
    if request.method == "POST":
        form = AccessoryForm(request.POST, request.FILES, instance=accessory)
        if form.is_valid():
            form.save()
            return redirect('accessories')  # Redirect back to accessories list
    else:
        form = AccessoryForm(instance=accessory)

    return render(request, 'accessories/edit_accessory.html', {'form': form, 'accessory': accessory})

def delete_accessory(request, accessory_id):
    """Delete an accessory after user confirmation."""
    accessory = get_object_or_404(Accessory, id=accessory_id)

    if request.method == "POST":
        accessory.delete()
        return redirect('accessories')  # Redirect after deletion

    return render(request, 'accessories/delete_confirmation.html', {'accessory': accessory})

def accessories_home(request):
    accessories = Accessory.objects.all()
    return render(request, 'accessories/accessories.html')
