from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    return render(request, 'index.html')

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_create.html', {'form': form})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_edit.html', {'form': form, 'item': item})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_delete.html', {'item': item})

def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('email_template.html', {
            "name": request.POST['name'],
            "email": request.POST['email'],
            "message": request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['xtianized1@gmail.com'],
        )
        email.fail_silently=False
        email.send()

    return render(request, 'EmailSent.html')