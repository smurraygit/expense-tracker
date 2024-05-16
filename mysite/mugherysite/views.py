from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construct the message body
            message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

            # Use the email address from your settings
            from_email = settings.EMAIL_HOST_USER

            # Send email to yourself
            recipient_list = [settings.EMAIL_HOST_USER]
            send_mail(
                subject=subject,
                message=message_body,
                from_email=from_email,
                recipient_list=recipient_list,
                fail_silently=False,
            )

            # Redirect to success page
            return HttpResponseRedirect('/success/')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})


def success(request):
    return render(request, 'success.html', {'message': 'Your message has been sent successfully!'})
