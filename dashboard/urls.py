from django.urls import path
from .views import home,index_view,search_view,about_us

urlpatterns = [
    path('', index_view, name='index'),
    path('home/', home, name='home'),
    path('search/', search_view, name='search'),
    path('about/',about_us , name='about')
]