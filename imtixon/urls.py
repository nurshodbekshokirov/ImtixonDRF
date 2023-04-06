
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from asosiy.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="ImtixonDRF API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Nurshodbek Shokirov,<nurshodbekshokirov@gmail.com>"),

   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register('suvlar', SuvviewSet)
router.register('haydovchilar', HaydovchiViewset)
router.register('adminlar', AdminViewSet)
router.register('mijozlar', MijozViewSet)
router.register('buyurtmalar', BuyurtmaviewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('haydovchilar/',  HaydovchiApiview.as_view()),
    path('token_ber/', TokenObtainPairView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('token_yangila/', TokenRefreshView.as_view()),
    path('', include(router.urls))
]
