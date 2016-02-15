from django.shortcuts import render

from apps.request.models import SavedRequest


def request_store(request):
    '''
    Requests store and sorting
    '''
    order_by = request.GET.get('order_by', '')
    # sort by priority which is passed in GET request
    if order_by:
        saved_requests = SavedRequest.objects.filter(priority=order_by)
        saved_requests = saved_requests.exclude(priority=0)
        saved_requests = saved_requests.order_by('-id')
        count = len(saved_requests)
        last_ten = saved_requests[:10]
        return render(request, "show_requests.html", {'requests': last_ten,
                      'title': count})
    # sort by standard selection priority=1
    saved_requests = SavedRequest.objects.filter(priority=1).order_by('-id')
    count = SavedRequest.objects.count()
    last_ten = saved_requests[:10]

    return render(request, "show_requests.html", {'requests': last_ten,
                  'title': count})
