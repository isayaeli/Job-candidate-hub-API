from django.urls import path
from .import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Job-candidate-hub-API",
      default_version='v1',
      description="A task for Job-candidate-hub-API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="isayaelib@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('api/add-information', views.add_candidate_information, name='add_info'),
    path('api/update-information/<int:pk>', views.update_candidate_information, name='update_info'),

    # url for api Documentation using swagger
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]