from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404 # Ensure get_object_or_404 is imported
from .forms import LostItemForm, FoundItemForm
from .models import LostItem, FoundItem

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('home')
    return render(request, 'core/login.html', {'form': form})

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'core/register.html', {'form': form})

@login_required
def report_lost(request):
    # Removed the duplicate @login_required decorator if it was there
    print("\n--- Inside report_lost view ---")
    if request.method == 'POST':
        print("Request method is POST.")
        # Removed 'or None' for POST request as request.POST and request.FILES are always present
        form = LostItemForm(request.POST, request.FILES)
        print(f"Form created. Is bound: {form.is_bound}")
        if form.is_valid():
            print("Form is VALID!")
            instance = form.save() # Capture the instance that was saved
            print(f"Form saved. Item ID: {instance.id}, Image path: {instance.image.url if instance.image else 'No image'}")
            print("Redirecting to gallery...")
            return redirect('gallery')
        else:
            print("Form is NOT VALID!")
            print("Form errors:", form.errors) # Crucial for debugging validation errors
            print("Non-field errors:", form.non_field_errors())
    else: # GET request
        print("Request method is GET.")
        form = LostItemForm()
    print("Rendering lost_form.html...")
    print("--- Exiting report_lost view --- \n")
    return render(request, 'core/lost_form.html', {'form': form})

@login_required
def report_found(request):
    form = FoundItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('gallery')
    return render(request, 'core/found_form.html', {'form': form})

def gallery(request):
    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()
    return render(request, 'core/item_gallery.html', {
        'lost_items': lost_items,
        'found_items': found_items
    })

# New view for resolving a lost item
@login_required
def resolve_lost_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(LostItem, id=item_id)
        item.delete() # For simplicity, delete the item. Consider a 'status' field for production.
        return redirect('gallery')
    # If not POST (e.g., someone tried to navigate directly), redirect to gallery
    return redirect('gallery')

# New view for resolving a found item
@login_required
def resolve_found_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(FoundItem, id=item_id)
        item.delete() # For simplicity, delete the item. Consider a 'status' field for production.
        return redirect('gallery')
    # If not POST, redirect to gallery
    return redirect('gallery')