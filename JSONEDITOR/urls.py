from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from editor import views as editor_views

router = routers.DefaultRouter()
router.register('json', viewset=editor_views.JsonViewSet, basename='json')
urlpatterns = router.urls
urlpatterns += path('admin/', admin.site.urls),
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
