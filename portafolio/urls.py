from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from portfolio import views as portfolio_views
from about import views as about_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('about-me/', about_views.about, name='about-me'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('contact/', core_views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
