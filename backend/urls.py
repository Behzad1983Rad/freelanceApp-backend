"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from company_app import views
# from freelance_app import views as freelanceViews

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'companies' , views.CompanyProfileViewSet)
router.register(r'jobs', views.JobListingViewSet)
router.register(r'freelancers', views.FreelancerProfileViewSet)
router.register(r'application' , views.JobApplicationViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
   
]
