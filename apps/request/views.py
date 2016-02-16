from django.shortcuts import render

from apps.request.models import SavedRequest


def request_store(request):
    '''
    Requests store and sorting
    '''
    order_by = request.GET.get('order_by', '')
    saved_requests = SavedRequest.objects.all()
    saved_requests = saved_requests.exclude(priority=0)
    count = SavedRequest.objects.count()
    try:
        if "all" in order_by:
            saved_requests = saved_requests.order_by('-priority')
            if request.GET.get('reverse', '') == '1':
                saved_requests = saved_requests.reverse()
            last_ten = saved_requests[:10]

            return render(request, "show_requests.html", {'requests': last_ten,
                          'title': count})
        order_by = order_by or 1
        saved_requests = SavedRequest.objects.filter(priority=order_by)
        saved_requests = saved_requests.order_by('-id')
        count = len(saved_requests)
        last_ten = saved_requests[:10]
        return render(request, "show_requests.html", {'requests': last_ten,
                      'title': count})
    except:
        return render(request, "show_requests.html")
