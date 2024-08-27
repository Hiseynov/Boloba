from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework import generics
from blog.models import Blogs

from .serializers import BlogSerializer

class BlogApiList(APIView):
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self,request,*args,**kwargs):
        if kwargs.get('pk'):
            blog = Blogs.objects.get(pk = kwargs.get('pk'))
            serializer = self.serializer_class(blog)
        
        else:
            blogs = Blogs.objects.all()
            serializer = self.serializer_class(blogs,many = True)

        return Response(serializer.data, status.HTTP_200_OK)
    
class BlogApiCreateList(generics.ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

class BlogApiUpdateList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        blog = self.get_object()  # Получаем объект blog
        serializer = self.get_serializer(blog)
        data = serializer.data

        # Добавляем данные о ProductVersion

        return Response(data)

    

