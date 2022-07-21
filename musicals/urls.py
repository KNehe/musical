from django.urls import path

from musicals.views import MusicalRetrieveAPIView


urlpatterns = [path("musical/<str:iswc>/", MusicalRetrieveAPIView.as_view())]
