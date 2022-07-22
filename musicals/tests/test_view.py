from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from musicals.models import Contributor, Musical


class MusicalRetrieveAPIViewTest(APITestCase):
    def test_should_fetch_a_musical(self):
        contributor = Contributor.objects.create(name="random_name")
        musical = Musical.objects.create(
            iswc="T0101974597", title="Adventure of a Lifetime"
        )
        musical.contributors.add(contributor)

        response = self.client.get(
            reverse("get_musical", kwargs={"iswc": musical.iswc})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["iswc"], musical.iswc)
        self.assertEqual(response.data["title"], musical.title)
        self.assertEqual(response.data["contributors"][0]["name"], contributor.name)

    def test_should_not_find_a_musical_when_not_created(self):

        response = self.client.get(
            reverse("get_musical", kwargs={"iswc": "T0101974597"})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["detail"], "Not found.")


# etc
