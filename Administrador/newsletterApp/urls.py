from django.urls import path
from . import views
urlpatterns = [
path('',views.membersList.as_view(), name="inicio" ),
]