from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm


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
def register(request):
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
            # return redirect('')

    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)


# Login
def login(request):
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
