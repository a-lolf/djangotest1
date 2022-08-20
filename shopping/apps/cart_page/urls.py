from django.urls.conf import re_path
from . import views

urlpatterns = [
    re_path(r'^cart_view/$', views.CartView.as_view()),
]
