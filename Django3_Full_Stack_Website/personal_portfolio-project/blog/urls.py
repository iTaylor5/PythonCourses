from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    # this says if anyone enters and integer after blog, I want you to represent that integer with blog_id,
    # and then pass it forward to detail
]