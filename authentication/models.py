from django.db import models

# Create your models here.

class User(models.Model):
    #id_user = models.AutoField(primary_key=True)
    id_city = models.ForeignKey('City', on_delete=models.CASCADE, null= True, blank = True,related_name="users")
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}" 

class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    id_country = models.ForeignKey('Country', on_delete=models.CASCADE, null= True, blank = True, related_name="departments")
    name = models.CharField(max_length=100)
    abrv = models.CharField(max_length=10)
    status = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.abrv}" 

class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    abrv = models.CharField(max_length=10)
    status = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.abrv} {self.status}" 

class City(models.Model):
    id_city = models.AutoField(primary_key=True)
    id_department = models.ForeignKey('Department', on_delete=models.CASCADE, null= True, blank = True, related_name="cities")
    name = models.CharField(max_length=100)
    abrv = models.CharField(max_length=10)
    status = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.abrv}" 

