from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import BookViewSet, LibraryViewSet
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'libraries', LibraryViewSet)
urlpatterns = router.urls
