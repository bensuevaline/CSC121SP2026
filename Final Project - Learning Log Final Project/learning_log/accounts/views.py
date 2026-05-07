from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Register a new user and log them in automatically
def register(request):
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process the completed registration form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)