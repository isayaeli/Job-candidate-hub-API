from django.urls import path
from .import views
urlpatterns = [
    path('api/add-info', views.add_candidate_info, name='add_info')
]