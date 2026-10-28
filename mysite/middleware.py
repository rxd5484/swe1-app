from django.http import HttpResponse


class HealthCheckMiddleware:
    """Reply to ALB health checks before Django validates the IP Host header."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/health/":
            return HttpResponse("ok", content_type="text/plain")
        return self.get_response(request)
