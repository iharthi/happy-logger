from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from entry.models import LogEntry


class ReceiveMessageView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request):
        # Check security token
        security_token = settings.LOGGER_SECURITY_TOKEN
        if security_token and request.headers.get('X-Logger-Token') != security_token:
            return HttpResponse('Forbidden', status=403, content_type='text/plain')

        # Try to determine remote hostname, either by special header, or from IP address
        remote_hostname = request.headers.get('X-Logger-Hostname') or request.META.get('REMOTE_ADDR') or _('Unknown')

        # Decode raw message as unicode, escape unknown
        message = request.body.decode("utf-8", "backslashreplace")

        # Save the entry
        LogEntry.objects.create(
            message=message,
            hostname=remote_hostname,
        )

        return HttpResponse('Ok', status=200, content_type='text/plain')

    def get(self, request):
        return redirect(reverse('admin:login'))
