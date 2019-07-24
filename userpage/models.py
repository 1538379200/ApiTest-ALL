from django.db import models

# Create your models here.
class user(models.Model):
    account=models.CharField(max_length=30)
    pwd=models.CharField(max_length=30)
    Email=models.EmailField()
    def __str__(self):
        return self.account