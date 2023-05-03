from django.urls import path
from .views import region_list, region_create, region_update, region_delete, home
from .views import district_list, district_create, district_update, district_delete

app_name = 'tawi'

urlpatterns = [
    # URLs for Region views
    path('', home, name='home'),
    path('region/', region_list, name='region_list'),
    path('region/add/', region_create, name='region_create'),
    path('region/<int:pk>/', region_update, name='region_update'),
    path('region/<int:pk>/delete/', region_delete, name='region_delete'),

    # URLs for District views
    path('district/', district_list, name='district_list'),
    path('district/add/', district_create, name='district_create'),
    path('district/<int:pk>/', district_update, name='district_update'),
    path('district/<int:pk>/delete/', district_delete, name='district_delete'),
]
