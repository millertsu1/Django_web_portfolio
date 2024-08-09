from django.db import models

""" modelo para formacion """

class Education(models.Model):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='education/')
    date = models.DateField()
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.name

""" modelo para experiencia laboral """

class Training(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    duration = models.IntegerField()
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='training_images/', null=True, blank=True)

    def __str__(self):
        return self.name

""" modelo para habilidades """

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()

    def __str__(self):
        return self.name

