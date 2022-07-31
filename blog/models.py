from django.db import models

# Create your models here.

class Contact(models.Model):
    query_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    subject = models.CharField(max_length=50, default=0)
    message = models.CharField(max_length=3000)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=300000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    
class FAQ(models.Model):
    FAQ_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.FAQ_id)