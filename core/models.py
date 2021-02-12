from django.db import models

# About Class.
class About(models.Model):
    name = models.CharField(max_length=100,verbose_name="Your Name :")
    profile = models.CharField(max_length=100,verbose_name="Your Profile :")
    email = models.EmailField(max_length=150,unique=True,verbose_name="Your E-Mail :")
    mobile = models.CharField(max_length=15,unique=True,verbose_name="Your Mobile : ")
    image = models.ImageField(upload_to='about',verbose_name="Upload Image : ")
    description = models.TextField(max_length=600,verbose_name="About You : ")

    class Meta:
        db_table = "about"

# Service Class.
class Service(models.Model):
    title = models.CharField(max_length=100,verbose_name="Service Title : ")
    description = models.TextField(max_length=600,verbose_name="Service Description : ")

    class Meta:
        db_table = "service"


#Portfolio Class.
class Portfolio(models.Model):
    title = models.CharField(max_length=100,verbose_name="Portfolio Title : ")
    image = models.ImageField(upload_to="portfolio",verbose_name="Upload Image : ")
    datetime = models.DateTimeField(auto_now=False,auto_now_add=False,verbose_name="DataTime")
    description = models.TextField(max_length=600,verbose_name="Portfolio Description : ")

    class Meta:
        db_table = "portfolio"

#Blog Class.
class Blog(models.Model):
    title = models.CharField(max_length=100,verbose_name="blog Title : ")
    image = models.ImageField(upload_to="blog",verbose_name="Upload Image : ")
    datetime = models.DateTimeField(auto_now=False,auto_now_add=False,verbose_name="DataTime")
    description = models.TextField(max_length=600,verbose_name="blog Description : ")

    class Meta:
        db_table = "blog"