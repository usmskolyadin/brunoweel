import os

from django.core.files import File
from django.db import migrations
from django.utils import timezone

SEED_IMAGES = os.path.join(os.path.dirname(__file__), "..", "fixtures", "seed_images")


def forwards(apps, schema_editor):
    SiteContent = apps.get_model("main", "SiteContent")
    Review = apps.get_model("main", "Review")
    ReviewPhoto = apps.get_model("main", "ReviewPhoto")

    content = SiteContent.objects.get(pk=1)
    content.reviews_eyebrow = "Нам доверяют"
    content.reviews_heading = "Что говорят"
    content.reviews_heading_accent = "гости «Бруновиля»"
    content.reviews_note = "Честные отзывы владельцев хвостиков, которые уже у нас погостили."
    content.yandex_maps_url = "https://yandex.ru/navi/org/zoootel_brunovil/15643200813?si=57qcf90390decybktb98edwq38"
    content.save()

    review1 = Review.objects.create(
        name="Анастасия Р.",
        rating=5,
        text=(
            "Оставляли нашего корги на неделю — переживали жутко, он первый раз без нас. "
            "Но присылали фото и видео каждый день, вернулся довольный и совсем не похудевший! "
            "Спасибо за заботу, теперь это наше постоянное место для передержки."
        ),
        created_at=timezone.datetime(2026, 9, 14, 18, 32, tzinfo=timezone.get_current_timezone()),
        order=1,
    )
    for i, filename in enumerate(("gallery_01.jpg", "gallery_02.jpg"), start=1):
        photo = ReviewPhoto(review=review1, order=i)
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            photo.image.save(filename, File(f), save=False)
        photo.save()

    Review.objects.create(
        name="Дмитрий К.",
        rating=5,
        text=(
            "Возили собаку на кинологическую передержку в Малинки — результат превзошёл ожидания. "
            "Пёс стал гораздо спокойнее на прогулках, перестал реагировать на других собак. "
            "Лия — профессионал своего дела, видно, что искренне любит животных."
        ),
        created_at=timezone.datetime(2026, 8, 2, 11, 5, tzinfo=timezone.get_current_timezone()),
        order=2,
    )


def backwards(apps, schema_editor):
    apps.get_model("main", "Review").objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_review_sitecontent_reviews_eyebrow_and_more"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
