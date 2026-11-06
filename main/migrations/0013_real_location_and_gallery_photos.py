import os
import random

from django.core.files import File
from django.db import migrations

SEED_IMAGES = os.path.join(os.path.dirname(__file__), "..", "fixtures", "seed_images")

ISTRA_FILES = [f"istra_{i:02d}.jpg" for i in range(1, 8)]
MALINOVKA_FILES = [f"malinovka_{i:02d}.jpg" for i in range(1, 8)]


def forwards(apps, schema_editor):
    Location = apps.get_model("main", "Location")
    LocationPhoto = apps.get_model("main", "LocationPhoto")
    GalleryImage = apps.get_model("main", "GalleryImage")

    istra = Location.objects.get(name="Истра")
    istra.photos.all().delete()
    for i, filename in enumerate(ISTRA_FILES, start=1):
        photo = LocationPhoto(location=istra, order=i)
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            photo.image.save(filename, File(f), save=False)
        photo.save()

    malinki = Location.objects.get(name="Малинки")
    malinki.photos.all().delete()
    for i, filename in enumerate(MALINOVKA_FILES, start=1):
        photo = LocationPhoto(location=malinki, order=i)
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            photo.image.save(filename, File(f), save=False)
        photo.save()

    # Mix the same real photos into the gallery, alongside the existing ones.
    for filename in ISTRA_FILES + MALINOVKA_FILES:
        img = GalleryImage()
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            img.image.save(filename, File(f), save=False)
        img.save()

    # Shuffle the whole gallery order so the new photos don't sit in one
    # block — a genuine mixed-up gallery feel rather than two batches.
    all_gallery = list(GalleryImage.objects.all())
    random.seed(20261108)
    random.shuffle(all_gallery)
    for i, img in enumerate(all_gallery, start=1):
        img.order = i
        img.save(update_fields=["order"])


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0012_seed_story"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
