import os

from django.core.files import File
from django.db import migrations

SEED_IMAGES = os.path.join(os.path.dirname(__file__), "..", "fixtures", "seed_images")


def forwards(apps, schema_editor):
    SiteContent = apps.get_model("main", "SiteContent")
    Location = apps.get_model("main", "Location")
    LocationPhoto = apps.get_model("main", "LocationPhoto")
    GalleryImage = apps.get_model("main", "GalleryImage")
    PackingItem = apps.get_model("main", "PackingItem")

    content = SiteContent.objects.get(pk=1)
    content.hero_sticker_text = "свежий воздух\nкаждый день"
    content.about_image_stamp = "дом, где ждут вашего хвостика"
    with open(os.path.join(SEED_IMAGES, "hero_poodle.jpg"), "rb") as f:
        content.hero_photo.save("hero_poodle.jpg", File(f), save=False)
    with open(os.path.join(SEED_IMAGES, "about_tent.jpg"), "rb") as f:
        content.about_image.save("about_tent.jpg", File(f), save=False)
    with open(os.path.join(SEED_IMAGES, "kinology_liya.jpg"), "rb") as f:
        content.kinology_photo.save("kinology_liya.jpg", File(f), save=False)
    content.save()

    istra = Location.objects.get(name="Истра")
    istra.photos.all().delete()
    for i, filename in enumerate(("location_istra_2026_1.jpg", "location_istra_2026_2.jpg"), start=1):
        photo = LocationPhoto(location=istra, order=i)
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            photo.image.save(filename, File(f), save=False)
        photo.save()

    malinki = Location.objects.get(name="Малинки")
    malinki.photos.all().delete()
    for i, filename in enumerate(("location_malinki_1.jpg", "location_malinki_2.jpg"), start=1):
        photo = LocationPhoto(location=malinki, order=i)
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            photo.image.save(filename, File(f), save=False)
        photo.save()

    GalleryImage.objects.all().delete()
    gallery_data = [
        ("gallery_01.jpg", "Завтрак по расписанию"),
        ("gallery_02.jpg", "Тихий час на диване"),
        ("gallery_03.jpg", "Главное — улыбаться"),
        ("gallery_04.jpg", "Пятая прогулка за день"),
        ("gallery_05.jpg", "Друзья по интересам"),
        ("gallery_06.jpg", "Первые шаги в дрессировке"),
        ("gallery_07.jpg", "Осенняя прогулка"),
        ("gallery_08.jpg", "Фото на память"),
        ("gallery_09.jpg", "Большая компания"),
        ("gallery_10.jpg", "Два характера — один дом"),
        ("gallery_11.jpg", "Готовы к прохладному вечеру"),
        ("gallery_12.jpg", "Отдых после игр"),
        ("gallery_13.jpg", "Перетягивание каната"),
        ("gallery_14.jpg", "Компашка разбойников"),
    ]
    for i, (filename, caption) in enumerate(gallery_data, start=1):
        img = GalleryImage(caption=caption, order=i)
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            img.image.save(filename, File(f), save=False)
        img.save()

    PackingItem.objects.all().delete()
    PackingItem.objects.bulk_create([
        PackingItem(text="Привычный корм", order=1),
        PackingItem(text="Любимые лакомства", order=2),
        PackingItem(text="Лежанку или плед с запахом дома", order=3),
        PackingItem(text="Любимые игрушки", order=4),
        PackingItem(text="Ошейник или шлейку с поводком", order=5),
        PackingItem(text="Пелёнки и средства индивидуального ухода", order=6),
        PackingItem(text="Полотенце и одежду по сезону", order=7),
        PackingItem(text="Лекарства, если питомец принимает их регулярно", order=8),
        PackingItem(text="Ветеринарный паспорт", order=9),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_sitecontent_max_url"),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
