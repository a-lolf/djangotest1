from django.urls.conf import re_path
from . import views

urlpatterns = [
    re_path(r'^apple/$', views.Apple.as_view()),
]
