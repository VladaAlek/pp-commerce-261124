from django.urls import path
from . import views



urlpatterns = [
    path('', views.all_categories, name='categories'),
    path('<int:category_id>/', views.category_detail, name='materials'),
    #path('products/', views.products, name='products'),
]