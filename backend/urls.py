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
from rest_framework_simplejwt import views as jwt_views
from company_app import views
from freelance_app import views as freelanceView
from company_app.views import *
# from company_app.views import CSRFTokenView
from company_app.views import get_photo_url

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'companies' , views.CompanyProfileViewSet)
router.register(r'companies' , views.CompanyProfileViewSet, basename = 'companyprofile')
router.register(r'jobs', views.JobListingViewSet )
router.register(r'freelancers', views.FreelancerProfileViewSet)
router.register(r'applications' , views.JobApplicationViewSet)
router.register(r'add_photo', views.PhotoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('auth_logout/', views.LogoutView.as_view(), name ='auth_logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('signup/', views.SignupView.as_view(), name ='signup'),
    path('company/<int:profile_id>/photo/', get_photo_url, name='get_photo_url'),
    path('', include(router.urls)),
   
]
