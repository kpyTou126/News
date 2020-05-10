from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import PostForm, EditForm

# Create your views here.

def index(request):
	blog_posts = BlogPost.objects.order_by("-date_added")
	context = {"blog_posts": blog_posts}
	return render(request, "blogs/index.html", context)

def new_post(request):
	if request.method !=  "POST":
		# Просто загрузка формы
		form = PostForm()
	else:
		# Обработка данных.
		form = PostForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect("blogs:index")
	context = {"form": form}
	return render(request, "blogs/new_post.html", context)

def edit_post(request, post_id):
	post = BlogPost.objects.get(id=post_id)

	if request.method != "POST":
		# Исходный запрос. Форма заполняется данными текущей записи.
		form = EditForm(instance=post)
	else:
		# Отправка данных POST. Обработать данные.
		form = EditForm(instance=post, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect("blogs:index")
	context = {"post": post, "form": form}
	return render(request, "blogs/edit_post.html", context)