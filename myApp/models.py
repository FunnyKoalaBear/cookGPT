from django.contrib.auth.models import AbstractUser
from django.db import models 

#gives field types like CharField, IntegerField, TextField, ImageField
#relatoinships like OneToOneField, ForeignKey, ManyToManyField


class User(AbstractUser):
    
    def __str__(self):
        return f"{self.username}, ({self.email})"

