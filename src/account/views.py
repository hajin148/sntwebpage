from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegisterationForm, AccountAuthenticationForm, AccountUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from blog.models import BlogPost
from announce.models import BlogPost as AnnouncePost

def registration_view(request):
	context = {}
	if request.POST:
		form =RegisterationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			phone_number = form.cleaned_data.get('phone_number')
			first_name = form.cleaned_data.get('first_name')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(username=username, email=email, phone_number=phone_number, first_name=first_name, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registeration_form'] = form
	else:
		form = RegisterationForm()
		context['registeration_form'] = form
	return render(request, 'account/register.html', context)


def logout_view(request):
	logout(request)
	return redirect('home')


def login_view(request):

	context = {}

	user = request.user
	if(user.is_authenticated):
		return redirect('home')

	if(request.POST):
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect('home')

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form
	return render(request, 'account/login.html', context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data.get('new_password')
            if new_password:
                user.set_password(new_password)
            user.save()
            messages.success(request, '계정 정보가 성공적으로 업데이트되었습니다. 다시 로그인 해주세요.')
            return redirect('home')  # Replace 'home' with the desired view name for your home page
    else:
        form = AccountUpdateForm(initial={"first_name": request.user.first_name, "username": request.user.username})

    context['account_form'] = form
    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts
    announce_posts = AnnouncePost.objects.filter(author=request.user)
    context['announce_posts'] = announce_posts
    return render(request, 'account/account.html', context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})