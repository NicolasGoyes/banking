from django.db import models

# Create your models here.

class User(models.Model):
#    id_user = models.AutoField(primary_key=True)
#    id_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="users")
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)

class Department(models.Model):
    name=models.CharField(max_length=20)
    abrev=models.CharField(max_length=5)






