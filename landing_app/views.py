from django.shortcuts import render
from .forms import UserEmailForm
# Create your views here.


def user_post(request):
    form = UserEmailForm()
    if request.method == 'POST':
        form = UserEmailForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'landingPage.html', context)
