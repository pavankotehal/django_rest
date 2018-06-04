__author__ = 'Pavan Kotehal'

from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('', views.ToDoViewSet, base_name='todos')
urlpatterns = router.urls