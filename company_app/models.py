from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CompanyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)


class JobListing(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100, blank=True)
    application_deadline = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Photo(models.Model):
  url = models.FileField(max_length=200)
  profile = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for profile_id: {self.profile_id} @{self.url}"
    

# class Photo(models.Model):
#     title = models.CharField(max_length=255)
#     document = models.FileField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True )
    
#     class Meta:
#         verbose_name_plural = 'Photos'

#     def __str__(self):
#         return f"Photo url: {self.url}"
