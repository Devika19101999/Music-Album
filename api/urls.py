from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

from api import views

from api.views import *

router = DefaultRouter()

router.register("album",views.AlbumViewSetView,basename="album"),








urlpatterns=[

      path("token/",ObtainAuthToken.as_view()),

      path("tracks/<int:pk>/",TrackMixinView.as_view()),

      path("register/",Userregister.as_view()),

      path("review/<int:pk>/",ReviewMixinview.as_view())

]+router.urls