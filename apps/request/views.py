from django.shortcuts import render

from apps.request.models import SavedRequest


# Create your views here.
def request_store(request):
    saved_requests = SavedRequest.objects.all().order_by('-id')
    count = SavedRequest.objects.count()
    last_ten = saved_requests[:10]

    return render(request, "show_requests.html", {'requests': last_ten,
                  'title': count})
