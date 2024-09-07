# from django.urls import path
# from .views import register, login, predict, userProfile, admin, delete_user, getNonAdminUsers
# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from .views import sign_up, sign_in

urlpatterns = [
   path('signup/', sign_up, name='sign_up'),
    path('signin/', sign_in, name='sign_in'),
] 
