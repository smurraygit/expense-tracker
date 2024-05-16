# contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(
                name=name, email=email, message=message)

            subject = 'Contact Form Submission'
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(
                    subject,
                    email_message,
                    email,  # Use the email obtained from the form as the sender
                    # Use EMAIL_HOST_USER from settings as the recipient
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except BadHeaderError as e:
                return HttpResponse('Invalid header found: %s' % e)

            return redirect('thank_you')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def thank_you(request):
    return render(request, 'contact/thank_you.html')
