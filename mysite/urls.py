from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name = "intro"),
    path('skills/',views.skills,name = "skills"),
    path('education/',views.edu,name = "edu"),
    path('experience/',views.exp,name = "exp"),
    path('achievements/',views.ach,name = "ach"),
    path('certifications/',views.certi,name = "certi"),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)