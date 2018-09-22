from django.urls import path, include
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, UserCreate, LoginView

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from . import  apiviews as view
router = DefaultRouter()

router.register('login', view.LoginView, base_name='login')

urlpatterns = [
            path("polls/", PollList.as_view(), name='poll_list'),
            path("polls/<int:pk>/", PollDetail.as_view(), name='poll_detail'),
            path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
            path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
            path("users/", UserCreate.as_view(), name="user_create"),
            path(r'', include(router.urls))
            ]