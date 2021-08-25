from django.contrib import admin
from django.urls import path, include
from home import views

#django admin header customization

admin.site.site_header ="Developer Sajib"
admin.site.site_title = "Welcome to dashboard"
admin.site.index_title = "Welcome this portal"
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('home/', include('home.urls'))
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]