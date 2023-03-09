from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostIndexView.as_view(), name='index'),
    path('categoria/<str:categoria>', views.PostCategoryView.as_view(), name='post_category'),
    path('busca/', views.PostSearchView.as_view(), name='post_search'),
    path('detalhes/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]