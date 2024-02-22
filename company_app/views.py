from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import JobListing, CompanyProfile
from .serializers import *
from freelance_app.models import FreelancerProfile, JobApplication

class UserViewSet(viewsets.ModelViewSet): 
 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_class = [permissions.IsAuthenticated]


class CompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    permission_class = [permissions.IsAuthenticated]


class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    permission_class = [permissions.IsAuthenticated]

class FreelancerProfileViewSet(viewsets.ModelViewSet):
    queryset = FreelancerProfile.objects.all()
    serializer_class = JobListingSerializer
    permission_class = [permissions.IsAuthenticated]


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_class = [permissions.IsAuthenticated]