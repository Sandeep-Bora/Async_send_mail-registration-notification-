from django.urls import path
from .views import registerview, article_create, dashboard

app_name = "async_project"
urlpatterns = [
    path('', dashboard),
    path('register/', registerview, name ="register"),
    path('article/', article_create, name ="article"),
]