from django.urls import path, include

urlpatterns = [
    
    path('api/supers/', include('- optional params')),
    path ('api/supers', include ('<int:pk>'))
]