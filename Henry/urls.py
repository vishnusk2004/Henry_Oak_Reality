from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('featured_properties/', views.featured_properties, name='featured_properties'),
    path('blog/', views.blog, name='blog'),
    path('blog_page/', views.blog_page, name='blog_page'),
]
