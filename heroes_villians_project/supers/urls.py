from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.supers_detail),
    # path('api/supers/', include('- optional params')),
    # path ('api/supers', include ('<int:pk>'))
]