from django.db import models


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

    quiet_hour_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    quiet_hour_heading = models.TextField("Заголовок (обычная часть)", default="")
    quiet_hour_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    quiet_hour_text = models.TextField("Текст про тихий час", default="")
    quiet_hour_photo = models.ImageField("Фото", upload_to="quiet-hour/", blank=True, null=True)

    locations_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    locations_heading = models.TextField("Заголовок (обычная часть)", default="")
    locations_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    locations_intro = models.TextField("Вводный текст про локации", default="")
    locations_choice_heading = models.CharField("Заголовок блока «Как выбрать локацию»", max_length=200, default="")
    locations_choice_apartment_title = models.CharField("Название варианта 1", max_length=100, default="Квартира")
    locations_choice_apartment_text = models.TextField("Описание варианта 1 (квартира)", default="")
    locations_choice_house_title = models.CharField("Название варианта 2", max_length=100, default="Дом")
    locations_choice_house_text = models.TextField("Описание варианта 2 (дом)", default="")

    packing_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    packing_heading = models.TextField("Заголовок (обычная часть)", default="")
    packing_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    packing_intro = models.TextField("Вводный текст", default="")

    kinology_eyebrow = models.CharField("Надпись над заголовком", max_length=200, default="")
    kinology_heading = models.TextField("Заголовок (обычная часть)", default="")
    kinology_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100, default="")
    kinology_description = models.TextField("Описание услуги", default="")
    kinology_telegram_url = models.URLField("Ссылка на Telegram", blank=True)
    kinology_instagram_url = models.URLField("Ссылка на Instagram", blank=True)

    contact_eyebrow = models.CharField("Надпись над заголовком", max_length=200)
    contact_heading = models.TextField("Заголовок (обычная часть)")
    contact_heading_accent = models.CharField("Заголовок (выделенная часть)", max_length=100)
    contact_description = models.TextField("Описание")
    phone = models.CharField("Телефон", max_length=30)
    telegram_url = models.URLField("Ссылка на Telegram", blank=True)
    whatsapp_url = models.URLField("Ссылка на WhatsApp", blank=True)
    instagram_url = models.URLField("Ссылка на Instagram", blank=True)
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


class KinologyTag(models.Model):
    text = models.CharField("Текст", max_length=100)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Услуга (тег)"
        verbose_name_plural = "Кинология — услуги (теги)"

    def __str__(self):
        return self.text
