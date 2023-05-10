from django.shortcuts import render
from account.models import Account

def begin_test_view(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "reservation/begin_test.html", context)