from django.shortcuts import render,redirect
from django.views import generic
from .models import Todo,Wordle
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CreateLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(generic.FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)

        return super().form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')

        return super().get(*args,**kwargs)




class TaskList(LoginRequiredMixin,generic.ListView):
    model = Todo
    queryset = Todo.objects.order_by('created')
    context_object_name = 'tasks'

    template_name = 'index.html'

    def get_context_data(self, **kwargs):                       #kunai specific user ko list matrai show garna
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin,generic.DetailView):
    model = Todo
    context_object_name = 'tsk'
    template_name = 'detail.html'

class TaskCreate(LoginRequiredMixin,generic.CreateView):
    model = Todo
    fields = ['title','desc','complete']
    template_name = 'create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):                 #user field hatauna , specific userle matrai data entry garna paucha
        form.instance.user = self.request.user
        return super().form_valid(form)




class TaskUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Todo
    fields = ['title','desc','complete']
    success_url = reverse_lazy('home')
    template_name = 'create.html'


class TaskDelete(LoginRequiredMixin,generic.DeleteView):
    model = Todo
    context_object_name = 'delete'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class WordleView(LoginRequiredMixin,generic.CreateView):
    model = Wordle
    fields = ['word']
    context_object_name = 'words'
    template_name = 'wordle.html'
    success_url = reverse_lazy('wordle')

    def form_valid(self, form):
        user = form.save()          # user field hatauna , specific userle matrai data entry garna paucha
        form.instance.user = self.request.user
        return super().form_valid(form)

class WordleList(LoginRequiredMixin,generic.ListView):
    model = Wordle
    context_object_name = 'words'
    template_name = 'wordle.html'

    def get_context_data(self, **kwargs):                       #kunai specific user ko list matrai show garna
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['words'] = context['words'].filter(user=self.request.user)

        return context




# Create your views here.
