from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import ListView,DetailView
from shop.models import *
# Create your views here.

def shop(request):
    data = Shop.objects.all()
    return render(request,'shop.html',{'data':data})

class shopPost(ListView):
    model = Shop
    template_name = 'shop.html'
    context_object_name = 'data'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def shopping(request):
    return render(request,'shopping-cart.html')
    
def singleProduct(request,pk):
    filterData = Shop.objects.exclude(pk = pk)
    filterData = list(filterData)
    filterData = filterData[:4]
    data = get_object_or_404(Shop,pk=pk)
    images = data.detal_Image.all()
    print(filterData)
    context = {
        'filterData':filterData,
        'data':data,
        'images':images
    }
    return render(request,'shopId.html',context)

class SinglePostProduct(View):
    def get_object(self):
        return Shop.objects.get(pk = self.kwargs.get('pk'))
    def get(self,request,*args,**kwargs):
        context = {
            'data':self.get_object
        }
        return render(request, 'shopId.html',context)

class SingleDetailView(DetailView):
    model = Shop
    context_object_name = 'data'
    template_name = 'shopId.html'
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        filter_data = Shop.objects.exclude(pk=pk)[:4]
        images = context['data'].detal_Image.all()
        context['filterData'] = filter_data
        context['images'] = images
        return context

def wishlist(request):
    return render(request,'wishlist.html')