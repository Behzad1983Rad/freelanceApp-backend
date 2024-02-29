# from django.contrib.auth.models import Group, User
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# # Create your views here.
# class SignupView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')
#         role = request.data.get('role')
        
#         try:
#             user = User.objects.create(username=username, email=email)
#             user.set_password(password)
#             user.save()
#             group = Group.objects.get(name=role)
#             group.user_set.add(user)
#             return Response(status=status.HTTP_200_OK)
        
#         except Group.DoesNotExist:
#             return Response({"error": "Group does not exist"}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)