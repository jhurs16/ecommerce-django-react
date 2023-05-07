
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/defender/', include('defender.urls')), # defender admin
    path('admin/', admin.site.urls),
    path('api/products/', include('product.urls.product_urls')),
    path('api/users/', include('product.urls.user_urls')),
    path('api/orders/', include('product.urls.order_urls')),
    path('api/categories/', include('product.urls.category_urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)