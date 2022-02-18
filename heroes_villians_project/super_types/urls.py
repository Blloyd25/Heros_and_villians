from django.urls import path, include
from . import views
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.super_type_list),
    path('<int:pk>/', views.super_types_detail)
]