from . import views
from django.urls import path

urlpatterns = [
    path('', views.home , name ='home'),
    path('landing/',views.landing_page,name='landing'),
    path('details/', views.details,name='details'),
    path('profile/', views.profile,name='profile'),
    path('search/' ,views.search, name='search' ),
    path('posts/' , views.create_post, name = 'posts'),
    path('user/' , views.user_profile, name = 'user_profile'),
    
    # path('like/<id>' , views.like , name='like'),

]
