from django.http.response import *


class FiltraIPMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        ips_autorizados = ['127.0.0.1']

        ip = request.META.get('REMOTE_ADDR')

        if ip not in ips_autorizados:
            return HttpResponseForbidden(
                'IP NÃO AUTORIZADO'
            )

        return None
