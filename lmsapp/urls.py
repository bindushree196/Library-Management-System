
from django.urls import path
from .import views

urlpatterns = [
    path('',views.library_list, name='library_list'),
    path('add/',views.add_library, name='add_library'),
    path('delete/<int:id>/', views.delete_library, name='delete_library'),   
    path('update/<int:id>/', views.update_library, name='update_library'),
]