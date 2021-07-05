from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
# Create your views here.

def index(request): 
    message = {}
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.subject = form.cleaned_data['subject']
                contact.content = form.cleaned_data['content']
                contact.email = form.cleaned_data['email'] 
                contact.save()
                form = ContactForm()
                message = {'tag' : 'alert-success', 'text' : 'form submitted successfully!'}
        else:
            form = ContactForm()
    except Exception as e: 
        message = {'tag' : 'alert-danger', 'text' : str(e)}

    return render(request, 'contact/index.html', {"form": form, 'message': message})