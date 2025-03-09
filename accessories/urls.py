from django.urls import path
from .views import accessories_page, accessories_home
from . import views

urlpatterns = [
    path('', accessories_page, name='accessories_page'),
    path('delete/<int:accessory_id>/', views.delete_accessory, name='delete_accessory'),
    path('delete/confirm/<int:accessory_id>/', views.confirm_delete_accessory, name='confirm_delete_accessory'),
    path('edit/<int:accessory_id>/', views.edit_accessory, name='edit_accessory'),
]