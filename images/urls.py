from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

path("images", views.imgsearch, name="imagesearch")
]
