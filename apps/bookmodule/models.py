from django.db import models

# Create your models here.

#-----------------------------Practice section-----------------
class company(models.Model):
    name = models.CharField(max_length = 50)
    address = models.TextField(max_length = 50)

class product(models.Model):
    kind = models.CharField(max_length = 50)
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    expire_year = models.IntegerField()

#-----------------------------Practice section-----------------
    
class Book(models.Model): 
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)


    
#class Address(models.Model):
  #  city = models.CharField(max_length = 50)

#class Student(models.Model):
 #   name = models.CharField(max_length = 50)
  #  age = models.SmallIntegerField(default = 1)
   # address = models.ForeignKey(Address, on_delete=models.CASCADE)
class department(models.Model):
    name = models.CharField(max_length = 50)
    
class card(models.Model):    
    card_number = models.SmallIntegerField(default = 1)

class course(models.Model):   
    title = models.CharField(max_length = 50)
    code = models.SmallIntegerField(default = 1)
    
# class student(models.Model):
#   name = models.CharField(max_length = 50)
#   card = models.OneToOneField(card, on_delete=models.PROTECT)
#   department = models.ForeignKey(department, on_delete=models.CASCADE)
#   course = models.ManyToManyField(course)
  
#------------------The First Task (LAB11)------------------
class address1(models.Model):
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.city
  



class student1(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(address1, on_delete=models.CASCADE)

#------------------The Second Task (LAB11)------------------

class address2(models.Model):
    city = models.CharField(max_length = 50)
    def __str__(self):
        return self.city
  
class student2(models.Model):
    name = models.CharField(max_length = 50)
    address = models.ManyToManyField(address2) 
    
#------------------The Third Task (LAB11)------------------ 
class register1(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField(default = 1)
    picture = models.FileField(upload_to='documents/')  # Save under 'product_images/'

    def __str__(self):
        return self.name

# class Document(models.Model):
#     title = models.CharField(max_length=100)              
#     file  = models.FileField(upload_to='documents/')
    
