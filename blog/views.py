from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from .forms import BlogForm


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


#Important:
# Django's home form is returned using the POST method, in which the browser bundles up the form data, encodes it for transmission, sends it to the server, and then receives back its response.
# GET , by contrast, bundles the submitted data into a string, and uses this to compose a URL.
# we use POST and GET while using the function views

# function view
# we have created a particular form for this view in forms.py
def addblog(request): 
    form=BlogForm()
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    context={
        'form':form,
    }
    return render(request,'add_blog.html',context)
    # render responds by HTTP response of context. Here (i.e) forms

class deleteBlog(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blog:home')# it asked to provide a success url, so...


# @login_required(login_url = ‘/home’)
# below is the kind of 'FORM' in django, because it takes some input from the user
# class addBlog(CreateView):
#     model = Post
#     template_name = 'add_blog.html'
#     form_class = BlogForm()
#     fields = ('title', 'slug', 'content','author',) # we can give specific fields also...
#     fields = '__all__' # here all takes all the fields from the Post model that we have mentioned above
    # In the above fields we are getting the input from the user
    # fields = ('author',)  using tuples # here author is field of Post model.
