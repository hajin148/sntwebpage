from django.shortcuts import render, redirect
from account.models import Account
from .forms import ReservationForm, DateOptions
import json

def begin_test_view(request):
    context = {}
    accounts = Account.objects.all()
    dates = DateOptions.objects.all()

    available_dates = [date.date.strftime('%Y-%m-%d') for date in dates]

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
    context['available_dates'] = json.dumps(available_dates)
    return render(request, "reservation/begin_test.html", context)

def success(request):
    return render(request, "reservation/success.html")
