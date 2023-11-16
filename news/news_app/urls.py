from django.urls import path
from .views import login_views, main_page, register_view 
urlpatterns =[
    path('',view=main_page),
    path('login/', view=login_views),
    path('register/', view=register_view, name='register')
]