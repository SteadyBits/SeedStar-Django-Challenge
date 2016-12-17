from django.shortcuts import render, redirect, get_object_or_404

from django.template.context_processors import csrf # to prevent XSS attack on form

from .models import Contact
from .forms import ContactForm

#landing page
def landing(request, template_name='landing.html'):
    data = {
    }
    return render(request, template_name, data)

#list method
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
