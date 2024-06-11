# decorators.py
from django.http import HttpResponse

from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    """
    Decorator for views that checks if the user is an admin.
    """
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            # If user is authenticated and is staff (admin), allow access
            return view_func(request, *args, **kwargs)
        else:
            # Otherwise, redirect to login or show an error page
            # Here, you can customize the behavior for non-admin users
            return HttpResponse("You are not authorized to access this page.")
    return _wrapped_view
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login page if user is not authenticated
        return view_func(request, *args, **kwargs)
    return wrapper
