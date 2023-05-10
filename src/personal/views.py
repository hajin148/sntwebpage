from account.models import Account
from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.views import get_blog_queryset1
from blog.models import BlogPost
from announce.views import get_blog_queryset2
from announce.models import BlogPost

# Create your views here.
BLOG_POSTS_PER_PAGE = 10

def home_screen_view(request):
	context = {}

	accounts = Account.objects.all()
	context['accounts'] = accounts 
	return render(request, "personal/home.html", context)

def introduce_snt_view(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/introduce_snt.html", context)

# curriculums

def curriculum_snt_view(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/curriculum/curriculum_snt.html", context)


def c_lit_essay(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/curriculum/c_lit_essay.html", context)


def c_cur_issue(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/curriculum/c_cur_issue.html", context)

def c_debate(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/curriculum/c_debate.html", context)


#schedules

def schedule_snt_view(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/schedule/schedule.html", context)

def g6(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/schedule/g6.html", context)

def g5(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/schedule/g5.html", context)

def g4(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/schedule/g4.html", context)

def g3(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/schedule/g3.html", context)

def begin_test_view(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/begin_test.html", context)

def opinion_view(request):

	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	blog_posts = sorted(get_blog_queryset1(query), key=attrgetter('date_updated'), reverse=True)
	
	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts

	return render(request, "personal/opinion.html", context)


def announce_view(request):

	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	blog_posts = sorted(get_blog_queryset2(query), key=attrgetter('date_updated'), reverse=True)
	
	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts

	return render(request, "personal/announce.html", context)