from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'servers', views.ServerViewSet)
router.register(r'applications', views.ApplicationViewSet)
router.register(r'address', views.AddressViewSet)
router.register(r'invoice', views.InvoiceViewSet)
router.register(r'invoice-items', views.InvoiceItemViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
