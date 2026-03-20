from django.db import connections
from django.db.utils import OperationalError
from django.shortcuts import render

class DatabaseCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # We only want to check the DB for regular pages, 
        # not for static files or media.
        if not request.path.startswith('/static/') and not request.path.startswith('/media/'):
            try:
                # Attempt a simple connection check
                connections['default'].ensure_connection()
            except OperationalError:
                # If the DB is down, show a nice maintenance page
                return render(request, 'jobs/maintenance.html', {
                    'message': "We're currently updating our portfolio. Please check back in a few minutes!"
                }, status=503)
        
        return self.get_response(request)