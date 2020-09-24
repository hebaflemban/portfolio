from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 50)
    date = models.DateTimeField()
    description = models.TextField()
    pretty_picture = models.ImageField()
    date_added =  models.DateTimeField(auto_now=True)
    tags = models.TextField()
    tags = models.ManyToManyField("Tag", related_name='projects')
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=191)
    def __str__(self):
        return self.name

class Guest(models.Model):
    name = models.CharField(max_length = 50)
    messege = models.TextField()
    messege_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
