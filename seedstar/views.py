from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.template.context_processors import csrf
from .models import Contact

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template import loader
from .models import *
from .forms import ContactForm


def landing(request):
    template = loader.get_template('landing.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def list(request, template_name='list.html'):
    contact = Contact.objects.all()
    data = {}
    data['contacts'] = contact
    return render(request, template_name, data)

#handles creation of new contact
def create(request, template_name='create.html'):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list')
    else:
        print (form.errors)
    return render(request, template_name, {'form': form})

#handles the update of existing contact
def update(request, id, template_name='create.html'):
    contact = get_object_or_404(Contact, id=id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('/list')
    return render(request, template_name, {'form': form})

#handles the deleting process of a contact, with confirmation below commiting
def delete(request, id, template_name='confirm_delete.html'):
    contact = get_object_or_404(Contact, id=id)
    if request.method=='POST':
        contact.delete()
        return redirect('/list')

    return render(request, template_name, {'object':contact.fname + " " + contact.lname})
