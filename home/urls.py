from django.urls import path
from home import views

urlpatterns = [
    path('', views.hello_world_view, name="hello-world")
]
