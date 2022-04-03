from django.contrib.auth import authenticate
from django.contrib.auth.models import User
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

# @login_required(login_url = ‘/home’)
# below is the kind of 'FORM' in django, because it takes some input from the user
# class addBlog(CreateView):
#     model = Post
#     template_name = 'add_blog.html'
#     # fields = ('title', 'slug', 'content','author',) # we can give specific fields also...
#     fields = '__all__' # here all takes all the fields from the Post model that we have mentioned above
    # In the above fields we are getting the input from the user
    # fields = ('author',)  using tuples # here author is field of Post model.


#Important:
# Django's home form is returned using the POST method, in which the browser bundles up the form data, encodes it for transmission, sends it to the server, and then receives back its response. GET , by contrast, bundles the submitted data into a string, and uses this to compose a URL.
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

class deleteBlog(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blog:home')# it asked to provide a success url, so...

#
# def Register(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 != password2:
#             messages.error(request, "Passwords do not match.")
#             return redirect('/register')
#
#         user = User.objects.create_user(username, email, password1)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()
#         return render(request, 'home.html')
#     return render(request, "register.html")
#
#
# def Login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             home(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("/")
#         else:
#             messages.error(request, "Invalid Credentials")
#         return render(request, 'blog.html')
#     return render(request, "home.html")
#
# def Profile(request):
#     return render(request, "profile.html")
#
# def edit_profile(request):
#     try:
#         profile = request.user.profile
#     except Profile.DoesNotExist:
#         profile = Profile(user=request.user)
#     if request.method=="POST":
#         form = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             alert = True
#             return render(request, "edit_profile.html", {'alert':alert})
#     else:
#         form=ProfileForm(instance=profile)
#     return render(request, "edit_profile.html", {'form':form})