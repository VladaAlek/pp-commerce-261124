from django.urls import path
from . import views



urlpatterns = [
    path('', views.all_categories, name='categories'),
    path('materials/<int:category_id>/', views.category_detail, name='materials'),
    path('category/<int:category_id>/', views.individual_category, name='individual_category'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_material/<int:category_id>', views.add_material, name='add_material'),
    path('edit/<int:category_id>/', views.edit_course, name='edit_course'),
    path('delete/<int:category_id>/', views.delete_course, name='delete_course'),
]

