from rest_framework.test import APITestCase
from django.core.management import call_command
from django.core.management.base import CommandError

from musicals.models import Musical


class CreateMusicalsTest(APITestCase):
    def test_should_fail_when_csvfile_not_provided_as_argument(self):
        with self.assertRaises(CommandError) as exc:
            call_command("createmusicals")
        self.assertEquals(
            str(exc.exception), "Error: the following arguments are required: file_path"
        )

    def test_should_fail_when_csvfile_not_found(self):
        with self.assertRaises(CommandError) as exc:
            call_command("createmusicals", "wrong_file.csv")
        self.assertEquals(str(exc.exception), "File 'wrong_file.csv' not found")

    def test_should_create_musicals(self):
        call_command("createmusicals", "test_csvs/csv.csv")

        musicals_count = Musical.objects.all().count()

        self.assertGreater(musicals_count, 0)
