from django.db import models
from django.utils import timezone


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SiteContent(SingletonModel):
    hero_eyebrow = models.CharField("Надпись над заголовком", max_length=200)
    hero_heading = models.TextField("Заголовок (обычная часть)", help_text="Перенос строки — новая строка в заголовке.")
    hero_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100)
    hero_description = models.TextField("Описание под заголовком")
    hero_button_primary_text = models.CharField("Текст основной кнопки", max_length=100)
    hero_button_secondary_text = models.CharField("Текст второй ссылки", max_length=100)
    hero_proof_text = models.CharField("Текст про количество собак", max_length=200)
    hero_photo = models.ImageField("Главное фото", upload_to="hero/", blank=True, null=True)
    hero_photo_caption = models.CharField("Подпись на фото", max_length=200, blank=True)
    hero_sticker_text = models.CharField("Текст на наклейке", max_length=100, blank=True)

    about_eyebrow = models.CharField("Надпись над заголовком", max_length=200)
    about_heading = models.TextField("Заголовок (обычная часть)")
    about_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100)
    about_paragraph_1 = models.TextField("Первый абзац")
    about_paragraph_2 = models.TextField("Второй абзац")
    about_image = models.ImageField("Фото", upload_to="about/", blank=True, null=True)
    about_image_stamp = models.CharField("Текст на фото", max_length=100, blank=True)
    about_link_text = models.CharField("Текст ссылки вниз", max_length=200)

    care_eyebrow = models.CharField("Надпись над заголовком", max_length=200)
    care_heading = models.TextField("Заголовок (обычная часть)")
    care_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100)
    care_description = models.TextField("Описание")

    gallery_eyebrow = models.CharField("Надпись над заголовком", max_length=200)
    gallery_heading = models.TextField("Заголовок (обычная часть)")
    gallery_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100)
    gallery_note = models.TextField("Текст-примечание")

    schedule_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    schedule_heading = models.TextField("Заголовок (обычная часть)", default="")
    schedule_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    schedule_intro = models.TextField("Вводный текст", default="")
    schedule_note = models.TextField("Подпись под карточками", default="")

    locations_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    locations_heading = models.TextField("Заголовок (обычная часть)", default="")
    locations_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    locations_intro = models.TextField("Вводный текст про локации", default="")
    locations_cta_heading = models.CharField("Заголовок блока-подсказки", max_length=200, default="")
    locations_cta_text = models.TextField("Текст блока-подсказки", default="")
    locations_cta_button_text = models.CharField("Текст кнопки блока-подсказки", max_length=100, default="")

    packing_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    packing_heading = models.TextField("Заголовок (обычная часть)", default="")
    packing_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    packing_intro = models.TextField("Вводный текст", default="")
    packing_note_heading = models.CharField("Заголовок пометки «Что важно знать заранее»", max_length=200, default="")
    packing_note_text = models.TextField("Текст пометки «Что важно знать заранее»", default="")

    meet_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    meet_heading = models.TextField("Заголовок (обычная часть)", default="")
    meet_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    meet_paragraph_1 = models.TextField("Первый абзац", default="")
    meet_paragraph_2 = models.TextField("Второй абзац", default="")
    meet_button_text = models.CharField("Текст кнопки", max_length=100, default="")

    kinology_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    kinology_heading = models.TextField("Заголовок (обычная часть)", default="")
    kinology_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    kinology_name = models.CharField("Имя", max_length=100, default="")
    kinology_role = models.CharField("Роль/подпись", max_length=200, default="")
    kinology_photo = models.ImageField("Фото", upload_to="kinology/", blank=True, null=True)
    kinology_quote = models.TextField("Цитата", default="")
    kinology_bio_1 = models.TextField("Первый абзац биографии", default="")
    kinology_bio_2 = models.TextField("Второй абзац биографии", default="")
    kinology_tasks_heading = models.CharField("Заголовок списка задач", max_length=200, default="")
    kinology_closing_1 = models.TextField("Заключительная фраза 1", default="")
    kinology_closing_2 = models.TextField("Заключительная фраза 2", default="")
    kinology_link_text = models.CharField("Текст ссылки «подробнее»", max_length=200, default="")
    kinology_telegram_url = models.URLField("Ссылка на Telegram", blank=True)
    kinology_instagram_url = models.URLField("Ссылка на Instagram", blank=True)

    gifts_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    gifts_heading = models.TextField("Заголовок (обычная часть)", default="")
    gifts_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    gifts_intro = models.TextField("Вводный текст", default="")
    gifts_from_us_heading = models.CharField("Заголовок «Подарки от нас»", max_length=200, default="")
    gifts_from_us_text = models.TextField("Текст «Подарки от нас»", default="")
    gifts_from_you_heading = models.CharField("Заголовок «Подарки от вас»", max_length=200, default="")
    gifts_from_you_text = models.TextField("Текст «Подарки от вас»", default="")

    reviews_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    reviews_heading = models.TextField("Заголовок (обычная часть)", default="")
    reviews_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    reviews_note = models.TextField("Текст-примечание", default="")

    contact_eyebrow = models.CharField("Надпись над заголовком", max_length=200)
    contact_heading = models.TextField("Заголовок (обычная часть)")
    contact_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100)
    contact_description = models.TextField("Описание")
    phone = models.CharField("Телефон", max_length=30)
    telegram_url = models.URLField("Ссылка на Telegram", blank=True)
    whatsapp_url = models.URLField("Ссылка на WhatsApp", blank=True)
    instagram_url = models.URLField("Ссылка на Instagram", blank=True)
    max_url = models.URLField("Ссылка на MAX", blank=True)
    yandex_maps_url = models.URLField("Ссылка на Яндекс Карты", blank=True)
    address = models.TextField("Адрес")
    hours = models.TextField("Часы приёма")
    map_note = models.CharField("Короткая фраза под адресом", max_length=300)

    footer_tagline = models.CharField("Фраза в подвале", max_length=200)
    footer_copyright = models.CharField("Копирайт в подвале", max_length=200)

    class Meta:
        verbose_name = "Контент сайта"
        verbose_name_plural = "Контент сайта"

    def __str__(self):
        return "Контент сайта"

    @property
    def phone_digits(self):
        return "".join(ch for ch in self.phone if ch.isdigit() or ch == "+")


class Tagline(models.Model):
    text = models.CharField("Текст", max_length=100)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Короткая фраза"
        verbose_name_plural = "Бегущая строка (короткие фразы)"

    def __str__(self):
        return self.text


class CareFeature(models.Model):
    icon = models.CharField("Значок (эмодзи/символ)", max_length=10, default="✳")
    title = models.CharField("Заголовок карточки", max_length=100)
    description = models.TextField("Описание")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Карточка заботы"
        verbose_name_plural = "Карточки заботы"

    def __str__(self):
        return self.title


class Stat(models.Model):
    value = models.CharField("Значение", max_length=20)
    label = models.CharField("Подпись", max_length=100)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Цифра"
        verbose_name_plural = "Цифры (статистика)"

    def __str__(self):
        return f"{self.value} — {self.label}"


class GalleryImage(models.Model):
    image = models.ImageField("Фото", upload_to="gallery/")
    caption = models.CharField("Подпись", max_length=200, blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Фото в галерее"
        verbose_name_plural = "Галерея"

    def __str__(self):
        return self.caption or f"Фото #{self.pk}"


class Location(models.Model):
    name = models.CharField("Название", max_length=100)
    tagline = models.CharField("Короткая фраза", max_length=200, blank=True)
    description = models.TextField("Описание", blank=True)
    address = models.CharField("Адрес", max_length=300)
    yandex_maps_url = models.URLField("Ссылка на Яндекс.Карты", blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class LocationHighlight(models.Model):
    location = models.ForeignKey(Location, related_name="highlights", on_delete=models.CASCADE, verbose_name="Локация")
    text = models.CharField("Текст", max_length=200)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Особенность локации"
        verbose_name_plural = "Особенности локации"

    def __str__(self):
        return self.text


class LocationPhoto(models.Model):
    location = models.ForeignKey(Location, related_name="photos", on_delete=models.CASCADE, verbose_name="Локация")
    image = models.ImageField("Фото", upload_to="locations/")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Фото локации"
        verbose_name_plural = "Фото локации"

    def __str__(self):
        return f"Фото #{self.pk}"


class PackingItem(models.Model):
    text = models.CharField("Текст", max_length=150)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Пункт списка"
        verbose_name_plural = "Что взять с собой"

    def __str__(self):
        return self.text


class ScheduleItem(models.Model):
    icon = models.CharField("Значок (эмодзи/символ)", max_length=10, default="✳")
    period = models.CharField("Период дня", max_length=50)
    description = models.TextField("Описание")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Пункт расписания"
        verbose_name_plural = "Расписание дня"

    def __str__(self):
        return self.period


class KinologyTask(models.Model):
    icon = models.CharField("Значок (эмодзи/символ)", max_length=10, default="✳")
    title = models.CharField("Заголовок", max_length=150)
    description = models.TextField("Описание")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Задача"
        verbose_name_plural = "Кинология — с какими задачами помогает"

    def __str__(self):
        return self.title


class GiftPhoto(models.Model):
    class Group(models.TextChoices):
        FROM_US = "from_us", "Подарки от нас"
        FROM_YOU = "from_you", "Подарки от вас"

    group = models.CharField("Группа", max_length=20, choices=Group.choices)
    image = models.ImageField("Фото", upload_to="gifts/")
    caption = models.CharField("Подпись", max_length=200, blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["group", "order"]
        verbose_name = "Фото подарка"
        verbose_name_plural = "Любовь взаимна — подарки"

    def __str__(self):
        return self.caption or f"Фото #{self.pk}"


class Review(models.Model):
    RATING_CHOICES = [(i, "★" * i) for i in range(1, 6)]

    name = models.CharField("Имя и фамилия", max_length=150)
    rating = models.PositiveSmallIntegerField("Оценка", choices=RATING_CHOICES, default=5)
    text = models.TextField("Текст отзыва")
    created_at = models.DateTimeField("Дата и время отзыва", default=timezone.now)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["-created_at", "-order"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.name} ({self.rating}★)"


class ReviewPhoto(models.Model):
    review = models.ForeignKey(Review, related_name="photos", on_delete=models.CASCADE, verbose_name="Отзыв")
    image = models.ImageField("Фото", upload_to="reviews/")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Фото к отзыву"
        verbose_name_plural = "Фото к отзыву"

    def __str__(self):
        return f"Фото #{self.pk}"
