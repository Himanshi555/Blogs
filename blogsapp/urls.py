from django.urls import path
from blogsapp import views
app_name = 'bl'
urlpatterns=[
    path('',views.blogview.as_view(), name='blogview'),
    path('detail/<int:pk>', views.Detail_view, name='Detail_view'),


]
