from django.db import models
from Anar_Django.utils.base import BaseModel
# Create your models here.


class Contact(BaseModel):
    name = models.CharField(max_length=100,verbose_name='Name:',help_text="max simvol 100")
    email = models.EmailField(verbose_name='Email:')
    desgription = models.TextField(verbose_name='Desgription',)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return self.email

