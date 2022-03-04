from django.urls import path
from . import views

urlpatterns = [
    path('',views.funapi,name='ap1'),
    path('deleteapi/<int:delid>',views.fundeleteapi,name='deleteapi'),
    path('funfilter',views.funfilter,name='funfilter')
    ]