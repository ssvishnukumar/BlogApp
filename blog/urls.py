from .views import PostList, PostDetail, deleteBlog, addblog
from django.urls import path
# from blog.views import addBlog
app_name = 'blog'
urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('delete/<str:slug>/', deleteBlog.as_view(), name='delete_blog'),
    path('add/', addblog, name='add_blog'), # I tried to paste this line in the last url, But it showed me a error and after that I pasted this above ...then it runs
    path('<str:slug>/', PostDetail.as_view(), name='post_detail'),
]
