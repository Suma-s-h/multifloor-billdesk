from django.urls import path
from textiles import views
urlpatterns=[
    path('',views.product_list,name='textiles')
]