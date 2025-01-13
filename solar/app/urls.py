from app.views import *

from django.urls import path
urlpatterns = [
    path("",home, name="home"),
    path("about/",about, name="about"),
    path("contact/",contact, name="contact"),
    path("service/",service, name="service"),
    path("project/",project, name="project"),
    path("team/",team, name="team"),
    path("testimonial/",testimonial, name="testimonial"),
    
]