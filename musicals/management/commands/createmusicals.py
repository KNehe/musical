from django.core.management.base import BaseCommand, CommandError
import os
from pathlib import Path
import csv

from musicals.models import Contributor, Musical


class Command(BaseCommand):
    help: str = "Generates musical works from csv file"

    def add_arguments(self, parser) -> None:
        parser.add_argument("file_path", nargs=1, type=str, help="Path to csv file")

    def handle(self, *args, **options):
        file_path = options["file_path"][0]
        allowed_extensions = [".csv"]

        # validate file
        if not os.path.isfile(file_path):
            raise CommandError(f"File '{file_path}' not found")

        if not Path(file_path).suffix in allowed_extensions:
            raise CommandError("Only csv allowed")

        # read file and create musicals
        musicals = []
        try:
            with open(file=file_path, mode="r") as file:
                reader = csv.reader(file)
                # skip columns names
                next(reader)

                self.stdout.write("Matching data...")
                matched_data = match_data(self, reader)

                self.stdout.write("Creating musical objects...")
                for k, v in matched_data.items():
                    musical, _ = Musical.objects.get_or_create(title=v[0], iswc=k)
                    for contributor_name in v[1]:
                        contributor, _ = Contributor.objects.get_or_create(
                            name=contributor_name
                        )
                        musical.contributors.add(contributor)

                # for k, v in matched_data.items():
                # musical, _ = Musical(contributors=",".join(v[1]), title=v[0], iswc=k)
                # musicals.append(musical)
            # Musical.objects.bulk_create(musicals)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created musical works from {file_path}"
                )
            )
        except Exception as e:
            self.stderr.write(f"An error occurred: {e}")


def match_data(command, reader):
    """
    Takes an instance of Command class and a csv reader
    """
    data = {}
    for row in reader:
        if len(row) != 3:
            command.stdout.write(command.style.NOTICE(f"Skipping invalid row {row}"))
            continue

        # work on rows with a iswc
        if row[2]:
            key = row[2]
            if key in data:
                # get existing contributors
                old_set = data[key][1]
                # get contributors from current row
                new_contributors = {i for i in row[1].split("|")}
                # compute union of current row's contributors and existing contributors
                new_set = old_set | new_contributors
                # update contributors
                data[key][1] = new_set
            else:
                contributors = {i for i in row[1].split("|")}
            # values are made up of a title and a set of contributors
            data[key] = [row[0], contributors]
        # TODO handle row without iswc
    return data
