from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from store.sitemaps import StaticViewSitemap, ProductSitemap, OrderDetailSitemap, CategorySitemap

sitemaps = {
    'static'    :   StaticViewSitemap,
    'product'   :   ProductSitemap,
    'order_detail'   :   OrderDetailSitemap,
    'categories'    :   CategorySitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('user_accounts.urls')),
    path('', include('store.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type='text/plain'))
]

handler404 = "store.views.error_404"


