from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    local = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True) 
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='authentification_user_set',   
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='authentification_user_permissions_set',  
        blank=True
    )

    def __str__(self):
        return self.username