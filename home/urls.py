from django.urls import path
from home import views
urlpatterns = [
    path('',views.homepage, name = "home"),
    path('register/', views.register,name = "register"),
    path('search/',views.search,name='search'),
]
