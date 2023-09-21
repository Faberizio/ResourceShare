from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import User  # Import your User model
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from django.contrib.auth.views import LogoutView

# Create your views here.
def user_list(request):
    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'user/user_list.html', context)


def login_view(request):
    error_message = None

    # Unbound state of our form
    form = AuthenticationForm()

    if request.method == 'POST':
        # Bound state of our form
        form = AuthenticationForm(data=request.POST)

        # Validate the data
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Corrected typo
            password = form.cleaned_data.get('password')  # Corrected typo

            # Authenticate the user
            user = authenticate(
                request=request,  # Pass the request object
                username=username,
                password=password,
            )

            # Check if user was authenticated
            if user is not None:
                # Use the session to keep the authenticated user id
                login(request, user)

                # Redirect the user to their profile page
                return redirect('profile')  # Corrected the redirect function

            # TODO: If the user is not authenticated, you can handle it here, e.g., show an error message.
            error_message = 'Invalid username or password.'

        else:
            # User's data is not valid. Display an error message.
            error_message = 'Sorry, something went wrong. Try again later.'

    context = {'form': form, "error_message": error_message}

    return render(request, "user/login.html", context)


@login_required  # Protect the profile view with login_required decorator
def profile(request):
    return render(request, 'user/profile.html')


