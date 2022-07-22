from django.urls import path

from musicals.views import MusicalRetrieveAPIView


urlpatterns = [path("musicals/<str:iswc>/", MusicalRetrieveAPIView.as_view())]
