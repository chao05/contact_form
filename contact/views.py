from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            notice_email=f'email is {form.cleaned_data["email"]}'
            notice_po_number=f'po_number is {form.cleaned_data["po_number"]}'
            send_mail(notice_email,notice_po_number, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
