from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('list_category', listCategory,name='list-category'),
    path('add_category', addCategory, name='add-category'),
    path('edit_category/<int:pk>', editCategory, name='edit-category'),
    path('delete_category/<int:pk>', deleteCategory, name='delete-category'),
]