from django.contrib.auth.models import Group, User
from .models import JobListing , CompanyProfile
from freelance_app.models import FreelancerProfile, JobApplication
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class JobListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobListing
        fields = '__all__'


class FreelancerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FreelancerProfile
        fields = '__all__'


class CompanyProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'


class JobApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

