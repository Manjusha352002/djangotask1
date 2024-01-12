from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    path('url/task/', views.task_view, name='task_view'),
    
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', include('yourappname.urls')),  
]
