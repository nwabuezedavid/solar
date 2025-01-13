from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path("",home, name="home"),
    path("about/",about, name="about"),
    path("contact/",contact, name="contact"),
    path("service/",service, name="service"),
    path("project/",project, name="project"),
    path("Product/",team, name="team"),
    path("testimonial/",testimonial, name="testimonial"),
    path("quote/",quote, name="quote"),
    path("Policy/",Policy, name="Policy"),
    
]


if settings.DEBUG:  # Only serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)