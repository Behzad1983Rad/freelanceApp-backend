from django.db import models
from django.contrib.auth.models import User
from company_app.models import JobListing  

# Create your models here.

class FreelancerProfile(models.Model):
    name = models.CharField(max_length=100)    
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class JobApplication(models.Model):
    freelancer = models.ForeignKey(FreelancerProfile, on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)


class Freelancer_Photo(models.Model):
  url = models.CharField(max_length=200)
  freelancer = models.ForeignKey(FreelancerProfile, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for freelancer_id: {self.freelancer_id} @{self.url}"