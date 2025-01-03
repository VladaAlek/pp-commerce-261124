from django.urls import path
from . import views



urlpatterns = [
    path('', views.all_categories, name='categories'),
    path('materials/<int:category_id>/', views.category_detail, name='materials'),
    path('category/<int:category_id>/', views.individual_category, name='individual_category'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:category_id>/', views.edit_course, name='edit_course'),
]

