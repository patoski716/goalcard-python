from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import GoalViewSet, GoalDetail

router = DefaultRouter()
router.register('goals', GoalViewSet, basename='goals')

urlpatterns = [
    path('', include(router.urls)),
    path('goals/delete/<int:pk>/', GoalDetail.as_view(), name='detailcreate'),

]