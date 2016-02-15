from apps.request.models import SavedRequest


class RequestMiddleware(object):
    """Save request to the db"""

    def process_request(self, request):
        # store requests if they are not ajax
        if request.is_ajax():
            return
        new_request = SavedRequest()
        new_request.path = request.get_full_path()
        new_request.host = request.get_host()
        new_request.method = request.method
        new_request.save()

        # for example how other priorities can be assigned
        if 'edit' in request.path:
            new_request.priority = 2
        elif 'login' in request.path:
            new_request.priority = 3
        elif 'order_by' in request.GET:
            new_request.priority = 0
        new_request.save()
