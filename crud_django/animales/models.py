from django.db import models

# Create your models here.
class Animal(models.Model) :
    name = models.CharField(max_length = 100 , blank = False , null = False)
    raza = models.CharField(max_length = 100 , blank = False , null = False)
    description = models.TextField(blank = False , null = False)
    
class Meta : 
        verbose_name = "animal"
        verbose_name_plural = "animals"
    
        def __str__(self) :
         return f'Animal : { self.name }'  