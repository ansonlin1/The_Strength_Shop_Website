from django.shortcuts import render
from .forms import EmailReachOutsForm

# Create your views here.

owner_email = '15ansonlin@gmail.com'

def SendEmail(request):
    context = {}
    if request.method == 'POST':
        # Get info from forms
        email_form = EmailReachOutsForm(data=request.POST)
        # Check to see if forms are valid
        if email_form.is_valid():
            # Save Email Form to Database
            email_form.save()

            email_form = EmailReachOutsForm()
        else:
            # Form was invalid
            print(email_form.errors)
        context['email_form'] = email_form
    else:
        # Was not an HTTP post so we just render the forms as blank.
        email_form = EmailReachOutsForm()
        context['email_form'] = email_form

    return render(request, 'about/about_home.html', context)
