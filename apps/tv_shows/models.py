from django.db import models
import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters in length."
        if (datetime.date.today() - datetime.datetime.strptime(postData['released'], "%Y-%m-%d").date()) < datetime.timedelta(days=1):
            errors['release_date'] = "Release date must be before today!"
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors['desc'] = "Description should be either blank or more than 10 characters."
    
        return errors

class Network(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.ForeignKey(Network, related_name="shows")
    release_date = models.DateField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()