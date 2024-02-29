# import uuid
# import boto3
# import os
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from rest_framework import permissions, viewsets, parsers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *
from freelance_app.models import *

class UserViewSet(viewsets.ModelViewSet): 

    queryset = User.objects.all().order_by('-date_joined')
    # user = User.objects.filter('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_class = [permissions.IsAuthenticated]

class HomeView(APIView):
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)

class LogoutView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        # role = request.data.get('role')
        
        try:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            # group = Group.objects.get(name=role)
            # group.user_set.add(user)
            return Response(status=status.HTTP_200_OK)
        
        except Group.DoesNotExist:
            return Response({"error": "Group does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CompanyProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return CompanyProfile.objects.filter(user = user)
    
    def post (self, request):
        # user = User.objects.get(user= request.data.get('user'))
        user = request.user
        name = request.data.get('name')
        description = request.data.get('description')
        website = request.data.get('website')
      
        try:
            company = CompanyProfile.objects.create(name=name, description=description, website=website, user_id=user.id)
            company.save()
            return Response(status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             

        

       

# class CompanyProfileViewSet(viewsets.ModelViewSet):
#     queryset = CompanyProfile.objects.all()
#     serializer_class = CompanyProfileSerializer
#     permission_class = [permissions.IsAuthenticated]
#     def post (self, request):
#         user = User.objects.get(user= request.data.get('user'))
#         name = request.data.get('name')
#         description = request.data.get('description')
#         website = request.data.get('website')
      
#         try:
#             company = CompanyProfile.objects.create(name=name, description=description, website=website, user_id=user.id)
#             company.save()
#             return Response(status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProfileCreate(LoginRequiredMixin, CreateView):
    queryset = CompanyProfile.objects.all()
    model = CompanyProfile
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
  

class ProfileUpdate(LoginRequiredMixin, UpdateView):
  model = CompanyProfile
#   fields = '__all__'
  fields = ['id', 'user', 'name', 'description', 'website', 'url']

class ProfileDelete(LoginRequiredMixin, DeleteView):
  model = CompanyProfile
  success_url = '/companies'




class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    permission_class = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     user_id = self.request.user.id
    #     return JobListing.objects.filter(created_by=user_id)
        
    def post (self, request):
        company = request.data.get('role')
        title = request.data.get('title')
        description = request.data.get('description')
        salary = request.data.get('salary')
        description = request.data.get('description')
        application_deadline = request.data.get('application_deadline')
        try:
            job = JobListing.objects.create(company=company, title= title, description=description, salary = salary, application_deadline = application_deadline )
            job.save()
            return Response(status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
# class JobListingViewSet(viewsets.ModelViewSet):
#     queryset = JobListing.objects.all()
#     serializer_class = JobListingSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         data = request.data.copy() 
#         data['created_by'] = request.user.id 
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
        
class JobCreate(LoginRequiredMixin, CreateView):
    queryset = JobListing.objects.all()
    model = JobListing
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
  

class JobUpdate(LoginRequiredMixin, UpdateView):
  model = JobListing
  fields = ['company', 'title', 'description', 'location', 'salary', 'application_deadline']

class JobDelete(LoginRequiredMixin, DeleteView):
  model = JobListing
  success_url = '/companies'

class FreelancerProfileViewSet(viewsets.ModelViewSet):
    queryset = FreelancerProfile.objects.all()
    serializer_class = JobListingSerializer
    permission_class = [permissions.IsAuthenticated]


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_class = [permissions.IsAuthenticated]

class PhotoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated)
    permission_class = [permissions.IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']




def get_photo_url(request, profile_id):
    try:
        profile = CompanyProfile.objects.get(pk=profile_id)
        photo = profile.photo_set.first()  
        if photo:
            return JsonResponse({'url': photo.url.url})  
        else:
            return JsonResponse({'error': 'Photo not found'}, status=404)
    except CompanyProfile.DoesNotExist:
        return JsonResponse({'error': 'Company profile not found'}, status=404)








