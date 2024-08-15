from django.urls import path
from first_app.views import Django_form

urlpatterns = [
    path('', Django_form),
]