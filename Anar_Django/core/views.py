from typing import Any, Dict
from django.shortcuts import render,redirect,resolve_url
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.utils.translation import get_language_from_request
from datetime import datetime
from .models import Contact
from .forms import *
# Create your views here.

def index(request):
    return render(request,'index.html')
    # return render(request,'time.html')


def time(request):
    now = datetime.now()
    context = {
        'title': "Time page",
        'vaht': now
    }
    return render(request, 'time.html', context=context)


def contact(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         # Создаем экземпляр модели и сохраняем данные из формы
    #         contact = Contact(
    #             name=form.cleaned_data['fullname'],
    #             email=form.cleaned_data['email'],
    #             desgription=form.cleaned_data['message']
    #         )
    #         contact.save()  # Сохраняем объект в базу данных
    #         return redirect('shop')  # Перенаправление на страницу успеха или другую страницу
    # else:
    #     form = ContactForm()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем объект в базу данных
            return redirect('shop')  # Перенаправление на страницу успеха или другую страницу
    else:
        form = ContactModelForm()

    return render(request, 'contact-us.html', {'form': form})

class ContactView(FormView):
    template_name = 'contact-us.html'
    form_class = ContactModelForm
    success_url = '/shop/'  # URL, на который будет перенаправлен пользователь после успешного сохранения формы

    def form_valid(self, form):
        form.save()  # Сохраняем объект в базу данных
        return super().form_valid(form)
    
class ContactListVies(ListView):
    model = Contact
    context_object_name = 'data'
    template_name = 'contact-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CreatePostView(CreateView):
    model = Contact
    form_class = ContactModelForm
    template_name = 'create.html'
    def get_success_url(self):
        return resolve_url('contact')



class UpdatePostView(UpdateView):
    model = Contact
    form_class = ContactModelForm
    template_name = 'update.html'
    def  get_success_url(self):
        return resolve_url('contact')
    
class DeletePostView(DeleteView):
    model = Contact
    template_name = 'delete.html'
    context_object_name = 'data'
    success_url = '/contact/'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        return context
    

def checkout(request):
    return render(request,'checkout.html')

def change_language(request):
    lang = request.GET.get('language')  # Исправлено на 'language'
    if lang in ['az', 'en', 'default']:
        referer = request.META.get('HTTP_REFERER')
        if not referer:
            return HttpResponseRedirect('/')

        path_list = referer.split('/')
        
        if lang == 'default':
            # Удаление языка из URL
            if len(path_list) > 3:
                path_list.pop(3)
        else:
            # Замена или добавление языка в URL
            if len(path_list) > 3:
                path_list[3] = lang
            else:
                path_list.insert(3, lang)

        path = '/'.join(path_list)
        
        # Установка языка в cookie
        response = HttpResponseRedirect(path)
        response.set_cookie('django_language', lang)
        activate(lang)  # Активация языка

        return response

    return HttpResponseRedirect('/')