from django.urls import path,include
from .views import PredictImageView
urlpatterns = [
    path('predict/',PredictImageView.as_view(),name='predict')

]