from django.shortcuts import render

from apps.hello.models import Contact


# home page view
def home(request):
    context = Contact.objects.first()
    return render(request, 'home.html', {'info': context})
