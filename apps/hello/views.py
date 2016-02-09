from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from apps.hello.models import Contact
from .forms import ContactForm
import json


# home page view
def home(request):
    context = Contact.objects.first()
    return render(request, 'home.html', {'info': context})


# edit form view
@login_required(login_url='/login/')
def edit(request, template_name="edit.html"):
    info = Contact.objects.get()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'result': 'success'}),
                                mimetype='application/json')

        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            return HttpResponse(json.dumps({'response': response,
                                            'result': 'error'}))
    form = ContactForm(instance=info)
    return render(request, template_name, {'form': form})
