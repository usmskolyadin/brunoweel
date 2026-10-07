import os

from django.core.files import File
from django.db import migrations

SEED_IMAGES = os.path.join(os.path.dirname(__file__), "..", "fixtures", "seed_images")


def forwards(apps, schema_editor):
    SiteContent = apps.get_model("main", "SiteContent")
    Location = apps.get_model("main", "Location")
    LocationHighlight = apps.get_model("main", "LocationHighlight")
    LocationPhoto = apps.get_model("main", "LocationPhoto")
    PackingItem = apps.get_model("main", "PackingItem")
    KinologyTag = apps.get_model("main", "KinologyTag")

    content = SiteContent.objects.get(pk=1)

    content.phone = "+7 (985) 188-66-66"
    content.telegram_url = "https://t.me/brunoweel13"
    content.whatsapp_url = "https://wa.me/79778051864"
    content.instagram_url = "https://www.instagram.com/brunoweel"

    content.quiet_hour_eyebrow = "Забота каждый день"
    content.quiet_hour_heading = "Время"
    content.quiet_hour_heading_accent = "отдыхать"
    content.quiet_hour_text = (
        "В нашем режиме предусмотрен тихий час для хвостиков — это не просто пауза, "
        "а важная часть заботы о питомцах.\n"
        "🐾 В условиях спокойствия и уюта они могут расслабиться и восстановить силы.\n\n"
        "Мы уверены, что внимание к их потребностям — это не только комфорт, "
        "но и ответственность за благополучие и здоровье каждого гостя 😌💤"
    )
    with open(os.path.join(SEED_IMAGES, "quiet_hour.jpg"), "rb") as f:
        content.quiet_hour_photo.save("quiet_hour.jpg", File(f), save=False)

    content.locations_eyebrow = "Две локации на выбор"
    content.locations_heading = "Выбирайте,"
    content.locations_heading_accent = "где гостить"
    content.locations_intro = (
        "У «Бруновиля» два формата — просторная квартира в городе и загородный дом. "
        "Расскажем, чем они отличаются, чтобы вам было проще выбрать."
    )
    content.locations_choice_heading = "Как выбрать локацию?"
    content.locations_choice_apartment_title = "Квартира"
    content.locations_choice_apartment_text = (
        "Лучше подходит для социализации собак, помогает корректировать поведение в городской среде."
    )
    content.locations_choice_house_title = "Дом"
    content.locations_choice_house_text = (
        "Прекрасное место для собак, которые нуждаются в большом пространстве "
        "и активных прогулках на свежем воздухе."
    )

    content.packing_eyebrow = "Собираемся в гости"
    content.packing_heading = "Что взять"
    content.packing_heading_accent = "с собой"
    content.packing_intro = "Короткий список, чтобы вашему хвостику было ещё уютнее с первых минут."

    content.kinology_eyebrow = "Партнёрский проект"
    content.kinology_heading = "Кинология и"
    content.kinology_heading_accent = "дрессировка"
    content.kinology_description = (
        "Если хочется не просто передержки, а системной работы над поведением — "
        "рекомендуем нашего партнёра по кинологии. Индивидуальные занятия, коррекция "
        "поведения и дог-фитнес для питомцев любого возраста."
    )
    content.kinology_telegram_url = "https://t.me/sobakanutaya_1"
    content.kinology_instagram_url = "https://www.instagram.com/sobakanutaya"

    content.save()

    istra = Location.objects.create(
        name="Истра",
        tagline="Простор и активность",
        address="Московская область, КДЗ Малиновка, 39",
        yandex_maps_url="https://yandex.ru/maps/?text=Московская+область,+КДЗ+Малиновка,+39",
        order=1,
    )
    LocationHighlight.objects.bulk_create([
        LocationHighlight(location=istra, order=1, text="Загородный дом + территория"),
        LocationHighlight(location=istra, order=2, text="Идеально для крупных пород"),
        LocationHighlight(location=istra, order=3, text="Подходит для тех, кто привык к свободным прогулкам, любит бегать и много играть"),
        LocationHighlight(location=istra, order=4, text="Много места для прогулок и базовых тренировок"),
    ])
    for i, filename in enumerate(("location_istra_1.jpg", "location_istra_2.jpg"), start=1):
        photo = LocationPhoto(location=istra, order=i)
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            photo.image.save(filename, File(f), save=False)
        photo.save()

    khimki = Location.objects.create(
        name="Химки",
        tagline="Уют и концентрация",
        address="Московская область, Деревня Холмы, 84",
        yandex_maps_url="https://yandex.ru/maps/?text=Московская+область,+Деревня+Холмы,+84",
        order=2,
    )
    LocationHighlight.objects.bulk_create([
        LocationHighlight(location=khimki, order=1, text="Квартира 65 кв. м"),
        LocationHighlight(location=khimki, order=2, text="Не более 4 хвостиков"),
        LocationHighlight(location=khimki, order=3, text="Рядом большой парк для активных прогулок в городе"),
        LocationHighlight(location=khimki, order=4, text="Идеально для неагрессивных собак маленьких пород"),
        LocationHighlight(location=khimki, order=5, text="Оборудована для коррекции поведения и дрессировки"),
    ])
    for i, filename in enumerate(("location_khimki_1.jpg", "location_khimki_2.jpg"), start=1):
        photo = LocationPhoto(location=khimki, order=i)
        with open(os.path.join(SEED_IMAGES, filename), "rb") as f:
            photo.image.save(filename, File(f), save=False)
        photo.save()

    PackingItem.objects.bulk_create([
        PackingItem(text="Полотенце", order=1),
        PackingItem(text="Одежда для собаки", order=2),
    ])

    KinologyTag.objects.bulk_create([
        KinologyTag(text="Коррекция поведения", order=1),
        KinologyTag(text="Дрессировка", order=2),
        KinologyTag(text="Дог-фитнес", order=3),
    ])


def backwards(apps, schema_editor):
    apps.get_model("main", "Location").objects.all().delete()
    apps.get_model("main", "PackingItem").objects.all().delete()
    apps.get_model("main", "KinologyTag").objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_kinologytag_location_packingitem_and_more"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
