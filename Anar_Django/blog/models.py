from django.db import models
from Anar_Django.utils.base import BaseModel


class Blogs(BaseModel):

    image= models.ImageField(upload_to ='Blog_img',verbose_name= 'Blogun sekli')
    title = models.CharField(max_length=255,verbose_name= 'Blog name')
    desgription = models.TextField(verbose_name='Desgription of the blog')
    is_publised = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        
    def __str__(self):
        return self.title
# Create your models here.
class Comment(BaseModel):
    coments = models.TextField(verbose_name= 'Bloga comment elave et: ')   
    name = models.CharField(max_length=255,verbose_name='Name: ') 
    email = models.EmailField(verbose_name='Email: ') 
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
    def __str__(self):
        return self.name

