import os
from collections import defaultdict
from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders
from django.conf import settings

class Command(BaseCommand):
    help = 'Find duplicate static files'

    def handle(self, *args, **options):
        found_files = defaultdict(list)

        self.stdout.write("Searching for static files...")

        # Check STATICFILES_DIRS
        for static_dir in settings.STATICFILES_DIRS:
            self.stdout.write(f"Checking directory: {static_dir}")
            for root, _, files in os.walk(static_dir):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    relative_path = os.path.relpath(filepath, static_dir)
                    found_files[relative_path].append(filepath)

        # Check using finders
        for finder in finders.get_finders():
            for path, storage in finder.list([]):
                full_path = os.path.join(storage.location, path)
                found_files[path].append(full_path)

        total_files = sum(len(locations) for locations in found_files.values())
        self.stdout.write(f"Total files checked: {total_files}")

        duplicates = {path: locations for path, locations in found_files.items() if len(locations) > 1}

        if not duplicates:
            self.stdout.write(self.style.SUCCESS('No duplicate files found.'))
        else:
            self.stdout.write(f"Found {len(duplicates)} sets of duplicate files:")
            for path, locations in duplicates.items():
                self.stdout.write(f"\nDuplicate found for {path}:")
                for location in locations:
                    self.stdout.write(f"  - {location}")
                    self.stdout.write(f"    File exists: {os.path.exists(location)}")
                    self.stdout.write(f"    Is symlink: {os.path.islink(location)}")
                    if os.path.exists(location):
                        self.stdout.write(f"    File size: {os.path.getsize(location)} bytes")
                        self.stdout.write(f"    Last modified: {os.path.getmtime(location)}")
