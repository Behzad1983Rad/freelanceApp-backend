from django.contrib.auth.models import Group, User
from .models import *
from freelance_app.models import *
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
        fields = ['company', 'title', 'description', 'location', 'salary', 'application_deadline' , 'id']
        
# class JobListingSerializer(serializers.HyperlinkedModelSerializer):
#     created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

#     class Meta:
#         model = JobListing
#         fields = ['company', 'title', 'description', 'location', 'salary', 'application_deadline', 'id', 'created_by']
       


class FreelancerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FreelancerProfile
        fields = '__all__'

        


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = ['id', 'user', 'name', 'description', 'website', 'url']
        
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'






 


class JobApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'






