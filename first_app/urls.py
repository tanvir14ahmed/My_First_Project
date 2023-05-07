from django.urls import include, path
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactPage.as_view(), name='contact')

]
