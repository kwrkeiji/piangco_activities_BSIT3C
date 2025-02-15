from django.urls import path
from .views import index, about, skills, services, contact

app_name = "portfolio"
urlpatterns = [
path('', index, name='index'),
path('home/', index, name='index'),
path('about/', about, name='about'), # portolio html
path('skills/', skills, name='skills'),
path('services/', services, name='services'),
path('contact/', contact, name='contact'),
]
