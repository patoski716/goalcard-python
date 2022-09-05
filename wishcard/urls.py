from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import GoalViewSet, delete_goal

router = DefaultRouter()
router.register('goals', GoalViewSet, basename='goals')

urlpatterns = [
    path('', include(router.urls)),
    path('goals/delete_goal/<int:pk>/', delete_goal.as_view()),
]