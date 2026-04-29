

from django.shortcuts import render,redirect
from . import models

# Create your views here.

# def start(request):
#     users=models.User.objects.all() 
#     return render(request, 'app/index.html',context={'users':users})

# def user_view(request,slug):
#     user=models.User.objects.get(slug=slug)
#     return render(request,'app/user_view.html',{'user':user})

# def create_user(request):
#     if request.POST:
#         name=request.POST.get('ism')
#         surename=request.POST.get('familiya')
#         age=request.POST.get('yosh')
#         picture=request.FILES.get('picture')

#         models.User.objects.create(
#             ism=name,
#             familiya=surename,
#             yosh=age,
#             picture=picture
#         )
#         return redirect('/start/')
#     return render(request,'app/create_user.html')


# def update_user(request, slug):
#     user = models.User.objects.get(slug=slug)

#     if request.POST:
#         user.ism = request.POST.get('ism')
#         user.familiya = request.POST.get('familiya')
#         user.yosh = request.POST.get('yosh')

#         if request.FILES.get('picture'):
#             user.picture = request.FILES.get('picture')

#         user.save()
#         return redirect('/start/')

#     return render(request, 'app/update_user.html', {'user': user})

# def delete_user(request, slug):
#     user = models.User.objects.get(slug=slug)

#     if request.POST:
#         user.delete()
#         return redirect('/start/')

#     return render(request, 'app/delete_user.html', {'user': user})



#-------------------Class-Based Views (CBV)------------------

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User

# READ (list)
class UserListView(ListView):
    model = User
    template_name = 'app/index.html'
    context_object_name = 'users'


# READ (detail)
class UserDetailView(DetailView):
    model = User
    template_name = 'app/user_view.html'
    context_object_name = 'user'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


# CREATE
class UserCreateView(CreateView):
    model = User
    template_name = 'app/create_user.html'
    fields = ['ism', 'familiya', 'yosh', 'picture']
    success_url = reverse_lazy('home')


# UPDATE
class UserUpdateView(UpdateView):
    model = User
    template_name = 'app/update_user.html'
    fields = ['ism', 'familiya', 'yosh', 'picture']
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('home')


# DELETE
class UserDeleteView(DeleteView):
    model = User
    template_name = 'app/delete_user.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('home')