from django.contrib import admin

from .models import JobListing , CompanyProfile, Photo
from freelance_app.models import FreelancerProfile, JobApplication

# Register your models here.

admin.site.register(JobListing)
admin.site.register(CompanyProfile)
admin.site.register(FreelancerProfile)
admin.site.register(JobApplication)
admin.site.register(Photo)

