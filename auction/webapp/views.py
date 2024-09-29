from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import redirect, render

from .forms import CreateUserForm, LoginForm


def hello(request):
    """
    Renders the 'index.html' template for the webapp.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object rendering the 'index.html' page.
    """
    return render(request, 'webapp/index.html', {})


def user_register(request):
    """
    Handles user registration by displaying and processing the
    registration form.

    If the request method is POST and the form is valid, a new
    user is created. Otherwise, it displays the empty or invalid
    form.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object rendering the 'register.html' page
        with the registration form or redirects to the login page
        upon successful registration.
    """
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')

    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)


def user_login(request):
    """
    Handles user login by displaying and processing the login form.

    If the request method is POST and the form is valid, the user
    is authenticated and logged in. Otherwise, it displays the
    empty or invalid form.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object rendering the 'login.html' page with
        the login form or redirects to the dashboard upon successful
        login.
    """
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {'form': form}
    return render(request, 'webapp/login.html', context=context)


@login_required(login_url='login')
def user_dashboard(request):
    """
    Renders the dashboard for the logged-in user.

    This view requires the user to be logged in. If the user is not
    logged in, they will be redirected to the login page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object rendering the 'dashboard.html' page.
    """
    return render(request, 'webapp/dashboard.html')


def user_logout(request):
    """
    Logs out the user and redirects to the login page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object redirecting to the login page after
        logging out the user.
    """
    auth.logout(request)
    return redirect("login")
