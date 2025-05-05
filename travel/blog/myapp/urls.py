from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns = [    
    path('', views.index, name='index'),
    path('subic-freeport-vtms', views.freeport, name='freeport'),
    path('subic-law-enforcement-dept', views.law, name='law'),
    path('museo-pampangulong-sasakyan', views.museo, name='museo'),
    path('bangko-sentral-pilipinas', views.bsp, name='bsp'),
    path('hytec-power-inc', views.hytec, name='hytec'),
    path('light-rail-transit', views.lrt, name='lrt'),
    path('metropolitan-manila-dev-auth', views.mmda, name='mmda'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)