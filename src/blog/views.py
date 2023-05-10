from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from blog.models import BlogPost
from django.core.paginator import EmptyPage, Paginator
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account

# Create your views here.

def create_blog_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(first_name=user.first_name).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
        return redirect('../opinion')

    context['form'] = form


    return render(request, "blog/create_blog.html")

def detail_blog_view(request, slug):
    context = {}
    
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    # Add pagination
    blog_posts = BlogPost.objects.all().order_by('-date_updated')
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_posts, 5)  # Show 5 blog posts per page

    try:
        blog_posts = paginator.page(page)
    except EmptyPage:
        blog_posts = paginator.page(paginator.num_pages)

    context['blog_posts'] = blog_posts
    
    return render(request, 'blog/detail_blog.html', context)

	
def edit_blog_view(request, slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	blog_post = get_object_or_404(BlogPost, slug=slug)

	if blog_post.author != user:
		return HttpResponse('업로드인이 아닙니다.')

	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "업데이트 되었습니다."
			blog_post = obj
			return redirect('../../opinion')

	form = UpdateBlogPostForm(
			initial = {
					"title": blog_post.title,
					"body": blog_post.body,
					"image": blog_post.image,
			}
		)

	context['form'] = form
	return render(request, 'blog/edit_blog.html', context)


def get_blog_queryset1(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = BlogPost.objects.filter(
				Q(title__icontains=q) | 
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))	

def delete_blog_post(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.author != user:
        return HttpResponse('업로드인이 아닙니다.')

    blog_post.delete()
    return redirect('opinion') 