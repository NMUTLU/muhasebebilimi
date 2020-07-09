from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def emailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form .is_valid():
            isminiz = form.cleaned_data['isminiz']    
            notunuz = form.cleaned_data['notunuz']
            form.save()
            messages.success(request,"Notunuzu başarılı şekilde aldık")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, "contact.html",{'form':form})