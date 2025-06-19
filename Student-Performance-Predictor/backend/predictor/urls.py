from django.urls import path
from .views import PredictGradeView

urlpatterns = [
    path('predict/', PredictGradeView.as_view(), name='predict-grade'),
]
# This file defines the URL patterns for the predictor app in a Django project.