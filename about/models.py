from django.db import models
from django.utils import timezone


""" Modelo para formación """
class Education(models.Model):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='education/')
    date = models.DateField()
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['-date']

    def __str__(self):
        return self.name

""" Modelo para experiencia laboral """
class Job(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='jobs/')
    date = models.DateField()
    duration = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-date']

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='skills/')
    years_experience = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['years_experience']

    def __str__(self):
        return self.title
