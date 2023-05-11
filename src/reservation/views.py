from django.shortcuts import render, redirect
from account.models import Account
from .forms import ReservationForm

def begin_test_view(request):
    context = {}
    accounts = Account.objects.all()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print("Form is not valid:")
            print(form.errors)
    else:
        form = ReservationForm()

    context['form'] = form
    context['accounts'] = accounts
    return render(request, "reservation/begin_test.html", context)

def success(request):
    return render(request, "reservation/success.html")
