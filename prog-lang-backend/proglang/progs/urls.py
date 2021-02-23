from rest_framework import routers
from .api import ProgViewSet, ReviewViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('api/progs', ProgViewSet, 'progs')
router.register('api/review', ReviewViewSet, 'review')
router.register('api/user', UserViewSet, 'users')

urlpatterns = router.urls