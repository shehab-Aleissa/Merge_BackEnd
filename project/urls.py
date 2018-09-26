"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import ProductListView, CategoryListView, OrderList, UserOrder, MakingOrder
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from landing_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token, name='login'),
    path('api/products/', CategoryListView.as_view(), name='api-products'),
    path('api/make/order/', MakingOrder.as_view(), name='api-make-order'),
    path('api/orders/', OrderList.as_view(), name='api-orders'),
    path('api/user/order/', UserOrder.as_view(), name='api-user-order'),

    path('', views.user_post, name='landing-page'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
