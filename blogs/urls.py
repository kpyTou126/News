from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
	path("", views.index, name="index"),
	path("new_post/", views.new_post, name="new_post"),
	path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
]