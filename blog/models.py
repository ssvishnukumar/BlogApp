from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:home') # we have to mention the app name also because we have mentioned that in the url page.


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     facebook = models.CharField(max_length=300, blank=True, null=True)
#     instagram = models.CharField(max_length=300, blank=True, null=True)
#     linkedin = models.CharField(max_length=300, blank=True, null=True)
#
#     def __str__(self):
#         return str(self.user)
#
