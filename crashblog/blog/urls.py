from django.urls import path
from . import views


urlpatterns =[
    path('search/', views.search, name='search'),
    path('<slug:catergory_slug>/<slug:slug>/', views.details, name='post_details'),
    path('<slug:slug>/', views.category, name='category_details'),
]
