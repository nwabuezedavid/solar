from django.db import models

# Create your models here.

class images (models.Model):
    name = models.CharField( max_length=50 ,blank=True, null=True,)
    logo = models.ImageField( blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    

   
    def __str__(self):
        return self.name
class projext (models.Model):
    name = models.CharField( max_length=50 ,blank=True, null=True,)
    logo = models.ImageField( blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    

   
    def __str__(self):
        return self.name

class expertteam (models.Model):
    name = models.CharField( max_length=50 ,blank=True, null=True,)
    logo = models.ImageField( blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    

   
    def __str__(self):
        return f"the item id:{self.id}"
class siteedit(models.Model):
    name = models.CharField( max_length=50 ,blank=True, null=True,)
    email = models.CharField( max_length=50 ,blank=True, null=True,)
    domain = models.CharField( max_length=50 ,default=name, blank=True, null=True,)
    Address = models.CharField( max_length=50 ,blank=True, null=True,)
    country = models.CharField( max_length=50 ,blank=True, null=True,)
    dis = models.TextField( blank=True, null=True,)
    phone = models.CharField( max_length=50 ,blank=True, null=True,)
    logo = models.ImageField( blank=True, null=True,)
    image1 = models.ImageField( blank=True, null=True,)
    idx = models.IntegerField( default=1) 
    
    facebooklink = models.CharField( max_length=500 ,blank=True, null=True,)
    twiiterlink = models.CharField( max_length=500 ,blank=True, null=True,)
    instergram = models.CharField( max_length=500 ,blank=True, null=True,)
    youtubelink = models.CharField( max_length=500 ,blank=True, null=True,)
   
    def __str__(self):
        return self.name
    
    
    


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    service = models.CharField(max_length=100)
    special_note = models.TextField(blank=True)

    def __str__(self):
        return self.name
    