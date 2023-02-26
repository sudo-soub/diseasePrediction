from django.urls import path
from disease import views

urlpatterns = [
    path("checkup/", views.DiseasePredictionViews.as_view())
]