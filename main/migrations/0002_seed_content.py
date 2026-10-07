import os

from django.conf import settings
from django.core.files import File
from django.db import migrations

SEED_IMAGES = os.path.join(os.path.dirname(__file__), "..", "fixtures", "seed_images")


def seed(apps, schema_editor):
    SiteContent = apps.get_model("main", "SiteContent")
    CareFeature = apps.get_model("main", "CareFeature")
    Stat = apps.get_model("main", "Stat")
    Tagline = apps.get_model("main", "Tagline")
    GalleryImage = apps.get_model("main", "GalleryImage")

    content = SiteContent(
        pk=1,
        hero_eyebrow="С любовью к хвостикам с 2017 года",
        hero_heading="Пока вы заняты\nделами,",
        hero_heading_accent="у него каникулы",
        hero_description="Тёплый загородный дом, зелёные дорожки и люди, которые знают: у каждой собаки свой характер.",
        hero_button_primary_text="Знакомиться и гулять",
        hero_button_secondary_text="Узнать про отель",
        hero_proof_text="Больше 1 200 хвостиков уже отдохнули у нас",
        hero_photo_caption="Здесь можно просто быть собакой",
        hero_sticker_text="свежий воздух каждый день!",
        about_eyebrow="Не передержка. Маленький отпуск.",
        about_heading="Своя территория.",
        about_heading_accent="Свои люди.",
        about_paragraph_1="Мы придумали «Бруновиль» для тех, кому важно не просто оставить питомца, а быть уверенным: его услышат, поймут и не дадут заскучать.",
        about_paragraph_2="Дом стоит среди сосен в Подмосковье. Здесь есть место для долгих прогулок, спокойного сна и новых друзей — в темпе, который подходит именно вашей собаке.",
        about_image_stamp="дом, где ждут хвост",
        about_link_text="Вот что мы для этого делаем",
        care_eyebrow="Забота в мелочах",
        care_heading="Хорошо ему.",
        care_heading_accent="Спокойно вам.",
        care_description="Мы не обещаем одинаковый день для всех. Мы обещаем внимание к тому, что нужно именно вашему хвостику.",
        gallery_eyebrow="Маленькая жизнь за городом",
        gallery_heading="Смотрите, как",
        gallery_heading_accent="тут хорошо",
        gallery_note="Каждый день в отеле — чуть-чуть разный.\nИ всегда с прогулкой.",
        contact_eyebrow="Начнём с знакомства",
        contact_heading="Приезжайте",
        contact_heading_accent="на прогулку",
        contact_description="Покажем дом, познакомимся с вашим хвостиком и ответим на все вопросы. Без обязательств — просто чай, лес и собаки.",
        phone="+7 495 123-45-67",
        telegram_url="https://t.me/",
        address="Московская область,\nИстринский район, д. Лесная",
        hours="Каждый день, с 9:00 до 20:00\nПо предварительной договорённости",
        map_note="Здесь заканчивается город и начинается хороший собачий день.",
        footer_tagline="Сделано с любовью к тем, кто встречает у двери.",
        footer_copyright="© 2026 · Московская область",
    )
    with open(os.path.join(SEED_IMAGES, "hero.jpg"), "rb") as f:
        content.hero_photo.save("hero.jpg", File(f), save=False)
    with open(os.path.join(SEED_IMAGES, "about.jpg"), "rb") as f:
        content.about_image.save("about.jpg", File(f), save=False)
    content.save()

    CareFeature.objects.bulk_create([
        CareFeature(icon="✳", title="Свобода гулять", order=1,
                    description="Закрытая зелёная территория и несколько прогулок каждый день — без городского шума и короткого поводка."),
        CareFeature(icon="☼", title="Знакомые рядом", order=2,
                    description="Небольшие компании, знакомство в комфортном темпе и человек рядом, который замечает настроение."),
        CareFeature(icon="♡", title="Вы всё знаете", order=3,
                    description="Присылаем фото и короткие новости каждый день. Можно выдохнуть и наслаждаться своей поездкой."),
    ])

    Stat.objects.bulk_create([
        Stat(value="7", label="лет заботимся", order=1),
        Stat(value="24/7", label="люди рядом", order=2),
        Stat(value="12", label="собак максимум", order=3),
        Stat(value="100%", label="любви к хвостам", order=4),
    ])

    Tagline.objects.bulk_create([
        Tagline(text="✳ носом в ветер", order=1),
        Tagline(text="♡ друзья по желанию", order=2),
        Tagline(text="☼ новости каждый день", order=3),
    ])

    gallery_data = [
        ("gallery_1.jpg", "Утро начинается с прогулки"),
        ("gallery_2.jpg", "Новые друзья — по желанию"),
        ("gallery_3.jpg", "Можно и просто понюхать траву"),
        ("gallery_4.jpg", "Возвращаться домой довольными"),
        ("gallery_5.jpg", "Тёплый плед и тишина вечером"),
        ("gallery_6.jpg", "Пять минут до новой прогулки"),
    ]
    for i, (filename, caption) in enumerate(gallery_data, start=1):
        img = GalleryImage(caption=caption, order=i)
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            img.image.save(filename, File(f), save=False)
        img.save()


def unseed(apps, schema_editor):
    apps.get_model("main", "SiteContent").objects.filter(pk=1).delete()
    apps.get_model("main", "CareFeature").objects.all().delete()
    apps.get_model("main", "Stat").objects.all().delete()
    apps.get_model("main", "Tagline").objects.all().delete()
    apps.get_model("main", "GalleryImage").objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
