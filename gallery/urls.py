from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('search/', views.search_images, name="search_images"),
    path('category/<category>', views.view_category, name='view_category'),
    path('location/<location>', views.view_location, name='view_location')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
