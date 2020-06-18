from django.db import models

class Category(models.Model):
    code = models.CharField(max_length=20,verbose_name='Mã', unique=True)
    name = models.CharField(max_length=100,verbose_name='Tên')

    def __str__(self):
        return self.name
