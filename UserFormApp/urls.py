
from django.urls import path
from . import views


urlpatterns = [
            path('update-user',views.update_user, name='update_user'),
    path('', views.index, name='index'),
     path('form', views.registration_form_page, name='registration_form'),
     path('add_data', views.create_form, name='add_data'),
     path('delete', views.delete_user, name='delete'),
 path('update_user_data', views.update_user_data, name='update_user_data'),
]