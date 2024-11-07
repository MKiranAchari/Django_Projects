from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup,name='signup'),
    path('loginn/', views.loginn,name='loginn'),
    path('todo/', views.todo),
    path('update/<int:sno>', views.update, name='update'),
    path('delete/<int:sno>', views.delete),
    path('signout/', views.signout, name='signout'),
]

