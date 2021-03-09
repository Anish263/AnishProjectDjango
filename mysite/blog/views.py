from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm,contactForm
from django.contrib.auth.forms import UserCreationForm
from django import template

register = template.Library()

@register.filter(name='short_form')
def short_form(text, lenght):
    return text[:lenght]

def contactus(request):
    title = ''
    confirm_message = None
    form = contactForm(request.POST or None)
    recentpost = Post.objects.all()
    if form.is_valid():
        print(form)
        receivers_list = ['gaurav.nagar14cs003@gmail.com','guptaanish029@gmail.com']
        print(receivers_list)
        subject = form.cleaned_data['subject']
        name = form.cleaned_data['name']
        comment = form.cleaned_data['message']
        emailFrom = form.cleaned_data['email']
        message = f'Name: {name}\nEmail Id: {emailFrom}\nMessage: {comment}'
        emailsender = settings.EMAIL_HOST_USER
        send_mail(subject, message, emailsender, receivers_list, fail_silently=False)
        title ="Thanks!"+' '+name
        confirm_message = "Thanks for the message. We will get right back to you."
        form = None

    return render(request,'blog/contact.html',{'title': title, 'form':form, 'confirm_message': confirm_message})


def post_delete(request,pk):
    postobj = Post.objects.get(pk=pk)
    postobj.delete()
    return redirect('post_list')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f'I am user: {user}')
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    recentpost = Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts,'recentpost':recentpost})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    recentpost = Post.objects.all()
    return render(request, 'blog/post_detail.html', {'post': post,'recentpost':recentpost})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            print(request.user)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
