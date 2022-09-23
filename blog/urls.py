from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('create_text_trans/', views.create_text_trans, name='create_text_trans'),
    path('ipfs_trans/', views.ipfs_trans, name='ipfs_trans'),
    path('update_texttrans/<int:id_transaction>/', views.update_texttrans, name='update_texttrans'),

]
