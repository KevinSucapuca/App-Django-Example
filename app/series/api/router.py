

from rest_framework.routers import DefaultRouter
from series.views import SeriesViewSet


router = DefaultRouter()

router.register(prefix='series', basename='series', viewset=SeriesViewSet)

