from django.urls import path, include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()

router.register(r'User', UserModelAdminViewSet)
router.register(r'Test', TestModelAdminViewSet)
router.register(r'Questiion', QuestionModelAdminViewSet)
router.register(r'Option', OptionModelAdminViewSet)
router.register(r'Answer', AnswerModelAdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegistrationView.as_view()),
    path('result/', ResultModelAdminViewSet.as_view())
    
]