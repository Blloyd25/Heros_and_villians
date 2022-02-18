from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/super_types/', include('super_types.urls')),
]