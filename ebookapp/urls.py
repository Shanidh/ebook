from django.urls import path
from . import views

urlpatterns = [
    path('',views.funapi,name='ap1'),
    path('deleteapi/<int:delid>',views.fundeleteapi,name='deleteapi'),
    path('funuserreg',views.funuserreg,name='funuserreg'),
    path('funuserlogin',views.funuserlogin,name='funuserlogin'),
    path('funuserget',views.funuserget,name='funuserget'),
    path('funtoken',views.funtoken,name='funtoken')
    ]