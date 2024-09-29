from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages


# Home
def hello(request):
    """
 Renders the 'index.html' template for the webapp.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object rendering the 'index.html' page.
    """
    return render(request, 'webapp/index.html', {})


# Register a user
def user_register(request):
    """
    Handles user registration by displaying and processing the
    registration form.

    If the request method is POST and the form is valid, the
    new user is created. Otherwise, it displays the empty
    or invalid form.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse object rendering the 'register.html' page
        with the registration form.
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


# Login
def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authnticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                # return redirect('')

    context = {'form': form}
    return render(request, 'webapp/login.html', context=context)

# logout


def user_logout(request):
    auth.logout(request)

    return redirect("login")
