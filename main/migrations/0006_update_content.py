from django.db import migrations


def forwards(apps, schema_editor):
    SiteContent = apps.get_model("main", "SiteContent")
    CareFeature = apps.get_model("main", "CareFeature")
    Stat = apps.get_model("main", "Stat")
    PackingItem = apps.get_model("main", "PackingItem")
    ScheduleItem = apps.get_model("main", "ScheduleItem")
    KinologyTask = apps.get_model("main", "KinologyTask")
    Location = apps.get_model("main", "Location")
    LocationHighlight = apps.get_model("main", "LocationHighlight")

    content = SiteContent.objects.get(pk=1)

    content.about_paragraph_1 = (
        "В «Бруновиле» у каждого хвостика есть пространство для прогулок, игр и отдыха, "
        "возможность выбирать компанию и проводить время в своём ритме."
    )
    content.about_paragraph_2 = (
        "С 2017 года мы создаём домашнюю атмосферу без клеток и вольеров, где учитывают "
        "характер, привычки и настроение каждой собаки. Наш опыт и знания собачьей психологии "
        "помогают находить подход к каждому гостю, бережно знакомить с новыми друзьями и "
        "создавать условия, в которых спокойно и комфортно."
    )

    content.schedule_eyebrow = "Ритм дня"
    content.schedule_heading = "Как проходит"
    content.schedule_heading_accent = "день в «Бруновиле»?"
    content.schedule_intro = "Прогулки, игры, отдых и ежедневный уход — в комфортном ритме для каждого хвостика."
    content.schedule_note = "Мы чередуем активность и отдых с учётом возраста, привычек и настроения собаки."

    content.locations_intro = (
        "Два загородных дома «Бруновиля» с разными форматами проживания: для комфортного "
        "отдыха или с кинологическим сопровождением. В каждом — домашняя атмосфера, "
        "свобода движения и индивидуальный подход."
    )
    content.locations_cta_heading = "Не знаете, что подойдёт вашему хвостику?"
    content.locations_cta_text = (
        "Расскажите о нём, и мы поможем выбрать дом с учётом его характера и потребностей."
    )
    content.locations_cta_button_text = "Расскажите о своём хвостике"

    content.packing_intro = "Чтобы хвостику было комфортно вдали от дома, рекомендуем собрать:"
    content.packing_note_heading = "Что нам важно знать заранее?"
    content.packing_note_text = (
        "Особенности здоровья, аллергии, режим питания, страхи, привычки, поведенческие "
        "особенности с незнакомцами и другими питомцами, а также контакты владельца на время поездки."
    )

    content.meet_eyebrow = "Перед заездом"
    content.meet_heading = "Будем"
    content.meet_heading_accent = "знакомы"
    content.meet_paragraph_1 = (
        "Мы понимаем, как важно доверить любимого друга людям, которых он ещё не знает. "
        "Поэтому знакомство — важная часть подготовки к отдыху в «Бруновиле»."
    )
    content.meet_paragraph_2 = (
        "Нам важно узнать привычки, характер и особенности вашей собаки, а ей — "
        "познакомиться с нами и новой обстановкой."
    )
    content.meet_button_text = "Записаться на знакомство"

    content.kinology_eyebrow = "Кинологическое сопровождение"
    content.kinology_heading = "Кинология в"
    content.kinology_heading_accent = "«Бруновиле»"
    content.kinology_name = "Лия"
    content.kinology_role = "Кинолог, зоопсихолог, создатель «Бруновиля»"
    content.kinology_quote = "«Я учу собак и их людей понимать друг друга»"
    content.kinology_bio_1 = (
        "«Бруновиль» я создала почти 10 лет назад, объединив профессиональную кинологию "
        "и домашний формат проживания."
    )
    content.kinology_bio_2 = (
        "Для меня премиальный уход — это не только комфорт, но и понимание поведения собаки, "
        "уважение к её потребностям и ответственность за её благополучие."
    )
    content.kinology_tasks_heading = "С какими задачами я помогаю?"
    content.kinology_closing_1 = "Занятия можно совместить с проживанием в «Бруновиле»."
    content.kinology_closing_2 = "Кинолог работает с собакой не только на тренировках, но и в повседневной жизни."
    content.kinology_link_text = "Подробнее о моём подходе"
    content.kinology_telegram_url = "https://t.me/zoopsihologi"
    content.kinology_instagram_url = "https://www.instagram.com/sobakanutaya"

    content.gifts_eyebrow = "Маленькие радости"
    content.gifts_heading = "Обмениваемся"
    content.gifts_heading_accent = "любовью"
    content.gifts_intro = "Мы любим радовать хвостиков подарками, а они и их люди отвечают нам взаимностью!"
    content.gifts_from_us_heading = "Подарки от нас"
    content.gifts_from_us_text = "Любим радовать хвостиков маленькими сюрпризами."
    content.gifts_from_you_heading = "Ваша благодарность"
    content.gifts_from_you_text = "Ваше внимание особенно ценно для нашей команды."

    content.contact_heading = "Ждём вас"
    content.contact_heading_accent = "в гости"
    content.contact_description = (
        "Покажем дом, познакомимся с вашим хвостиком и ответим на все вопросы. "
        "Без обязательств — просто чай, гармония и собаки."
    )
    content.address = (
        "Истра — Московская область, деревня Холмы, 84\n"
        "Малинки — Московская область, КДЗ Малиновка, 39"
    )

    content.save()

    CareFeature.objects.all().delete()
    CareFeature.objects.bulk_create([
        CareFeature(icon="✳", order=1, title="Свобода гулять",
                    description="Прогулки, игры и пространство для движения. Без клеток и вольеров, в ритме, который подходит вашему любимцу."),
        CareFeature(icon="☼", order=2, title="Друзья по желанию",
                    description="Не всем хочется большой компании. Знакомим собак постепенно, учитываем характер и не навязываем общение."),
        CareFeature(icon="✦", order=3, title="Забота от носа до хвоста",
                    description="Следим за гигиеной глаз, зубов, лап и шерсти. Купаем, вычёсываем и подстригаем когти с учётом потребностей и настроения гостя."),
        CareFeature(icon="✛", order=4, title="Здоровье под вниманием",
                    description="Наблюдаем за самочувствием гостей. На связи ветеринарный врач 24/7, а при необходимости можем организовать поездку в клинику."),
        CareFeature(icon="♡", order=5, title="Держим в курсе",
                    description="Быть вдали от питомца спокойнее, когда знаешь, как проходит его день! Мы ежедневно отправляем фото и новости, рассказываем о настроении, прогулках и самочувствии гостей."),
    ])

    Stat.objects.all().delete()
    Stat.objects.bulk_create([
        Stat(value="7", label="лет заботы", order=1),
        Stat(value="10 000+", label="сменных пелёнок", order=2),
        Stat(value="15 000+", label="ватных дисков для гигиены", order=3),
        Stat(value="100+", label="тюбиков зубной пасты", order=4),
        Stat(value="24/7", label="мы рядом", order=5),
        Stat(value="10+", label="кг вычесанной шерсти", order=6),
        Stat(value="12", label="собак максимум в доме", order=7),
    ])

    PackingItem.objects.all().delete()
    PackingItem.objects.bulk_create([
        PackingItem(text="Привычный корм и любимые лакомства", order=1),
        PackingItem(text="Миски для еды и воды", order=2),
        PackingItem(text="Лежанку или плед с запахом дома", order=3),
        PackingItem(text="Любимые игрушки", order=4),
        PackingItem(text="Ошейник или шлейку с поводком", order=5),
        PackingItem(text="Пелёнки и средства индивидуального ухода", order=6),
        PackingItem(text="Полотенце и одежду по сезону", order=7),
        PackingItem(text="Лекарства, если питомец принимает их регулярно", order=8),
        PackingItem(text="Ветеринарный паспорт", order=9),
    ])

    ScheduleItem.objects.bulk_create([
        ScheduleItem(icon="☀", period="Утро", order=1,
                     description="Прогулка, завтрак, гигиена глаз и лап."),
        ScheduleItem(icon="✦", period="День", order=2,
                     description="Игры, общение, вычёсывание и внимание к самочувствию."),
        ScheduleItem(icon="☾", period="Тихий час", order=3,
                     description="Спокойный сон и восстановление сил."),
        ScheduleItem(icon="⌂", period="Вечер", order=4,
                     description="Прогулка, ужин и гигиена после прогулки."),
        ScheduleItem(icon="✧", period="По запросу", order=5,
                     description="Купание, стрижка когтей и дополнительный уход."),
    ])

    KinologyTask.objects.bulk_create([
        KinologyTask(icon="✳", title="Воспитать щенка", order=1,
                     description="Приучить к правилам дома, социализировать и освоить базовые команды."),
        KinologyTask(icon="♡", title="Скорректировать поведение", order=2,
                     description="Работа со страхами, тревожностью, нежелательными реакциями на людей и других собак."),
        KinologyTask(icon="✦", title="Обучить послушанию", order=3,
                     description="Курс УГС, спокойные прогулки и выполнение команд в повседневных ситуациях."),
        KinologyTask(icon="☼", title="Наладить контакт с собакой", order=4,
                     description="Научиться понимать её поведение, правильно взаимодействовать и закреплять навыки самостоятельно."),
    ])

    istra = Location.objects.get(name="Истра")
    istra.tagline = "Простор и комфорт"
    istra.description = (
        "Загородный дом для полноценного отдыха с просторной территорией, свободными "
        "прогулками и вниманием к привычкам каждого гостя."
    )
    istra.address = "Московская область, деревня Холмы, 84"
    istra.yandex_maps_url = "https://yandex.ru/maps/?text=Московская+область,+деревня+Холмы,+84"
    istra.save()
    istra.highlights.all().delete()
    LocationHighlight.objects.bulk_create([
        LocationHighlight(location=istra, order=1, text="Для средних и крупных пород"),
        LocationHighlight(location=istra, order=2, text="Пространство для прогулок, игр и тренировок"),
        LocationHighlight(location=istra, order=3, text="Свобода движения и комфортный ритм жизни"),
        LocationHighlight(location=istra, order=4, text="Домашний уют без клеток и вольеров"),
        LocationHighlight(location=istra, order=5, text="Соблюдение привычного расписания для каждого"),
    ])

    malinki = Location.objects.get(name="Химки")
    malinki.name = "Малинки"
    malinki.tagline = "Проживание с кинологом"
    malinki.description = (
        "Здесь уютная атмосфера встречается с профессиональным кинологическим сопровождением. "
        "Работа с поведением не ограничивается занятиями, а продолжается в повседневном общении с собакой."
    )
    malinki.address = "Московская область, КДЗ Малиновка, 39"
    malinki.yandex_maps_url = "https://yandex.ru/maps/?text=Московская+область,+КДЗ+Малиновка,+39"
    malinki.save()
    malinki.highlights.all().delete()
    LocationHighlight.objects.bulk_create([
        LocationHighlight(location=malinki, order=1, text="Проживание под присмотром кинолога"),
        LocationHighlight(location=malinki, order=2, text="Воспитание и социализация щенков"),
        LocationHighlight(location=malinki, order=3, text="Индивидуальная коррекция поведения"),
        LocationHighlight(location=malinki, order=4, text="Обучение по курсу УГС"),
        LocationHighlight(location=malinki, order=5, text="Закрепление навыков в повседневной жизни"),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_giftphoto_kinologytask_scheduleitem_and_more"),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
