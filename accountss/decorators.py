from django.shortcuts import redirect
def backend_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_admin:
            # User is authenticated and has dashboard access
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to an unauthorized page or raise an exception
            return redirect('admin_login')

    return wrapper

def frontend_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_customer:
            # User is authenticated and has shop access
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to an unauthorized page or raise an exception
            return redirect('user_login')

    return wrapper
