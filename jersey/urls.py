from django.urls import path
from jersey import views
from .views import delete_jersey, confirm_delete_jersey

urlpatterns = [
    path('', views.home, name='home'),
    path('jerseys/', views.home, name='jersey_page'),
    path('delete/<int:jersey_id>/', delete_jersey, name='delete_jersey'),
    path('delete/confirm/<int:jersey_id>/', confirm_delete_jersey, name='confirm_delete_jersey'),
    path('edit/<int:jersey_id>/', views.edit_jersey, name='edit_jersey'),
    path('contact/', views.contact, name='contact'),
]