from django.shortcuts import render
from .models import Education, Job, Skill 

# Create your views here.
def about(request):
     educations = Education.objects.all()
     jobs = Job.objects.all()
     skills = Skill.objects.all()

     return render(request, 'about/about.html', {'educations': educations, 'jobs': jobs, 'skills': skills})
 
