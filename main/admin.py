from django.contrib import admin

from .models import (
    CareFeature,
    GalleryImage,
    GiftPhoto,
    KinologyTask,
    Location,
    LocationHighlight,
    LocationPhoto,
    PackingItem,
    Review,
    ReviewPhoto,
    ScheduleItem,
    SiteContent,
    Stat,
    Tagline,
)


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Главный экран", {"fields": (
            "hero_eyebrow", "hero_heading", "hero_heading_accent", "hero_description",
            "hero_button_primary_text", "hero_button_secondary_text", "hero_proof_text",
            "hero_photo", "hero_photo_caption", "hero_sticker_text",
        )}),
        ("О нас", {"fields": (
            "about_eyebrow", "about_heading", "about_heading_accent",
            "about_paragraph_1", "about_paragraph_2", "about_image", "about_image_stamp", "about_link_text",
        )}),
        ("Предыстория", {"fields": (
            "story_eyebrow", "story_heading", "story_heading_accent", "story_text",
        )}),
        ("Забота", {"fields": ("care_eyebrow", "care_heading", "care_heading_accent", "care_description")}),
        ("Расписание дня", {"fields": (
            "schedule_eyebrow", "schedule_heading", "schedule_heading_accent",
            "schedule_intro", "schedule_note",
        )}),
        ("Локации — заголовок", {"fields": (
            "locations_eyebrow", "locations_heading", "locations_heading_accent", "locations_intro",
            "locations_cta_heading", "locations_cta_text", "locations_cta_button_text",
        )}),
        ("Галерея — заголовок", {"fields": ("gallery_eyebrow", "gallery_heading", "gallery_heading_accent", "gallery_note")}),
        ("Что взять с собой — заголовок", {"fields": (
            "packing_eyebrow", "packing_heading", "packing_heading_accent", "packing_intro",
            "packing_note_heading", "packing_note_text",
        )}),
        ("Будем знакомы", {"fields": (
            "meet_eyebrow", "meet_heading", "meet_heading_accent",
            "meet_paragraph_1", "meet_paragraph_2", "meet_button_text",
        )}),
        ("Кинология", {"fields": (
            "kinology_eyebrow", "kinology_heading", "kinology_heading_accent",
            "kinology_name", "kinology_role", "kinology_photo", "kinology_quote",
            "kinology_bio_1", "kinology_bio_2", "kinology_tasks_heading",
            "kinology_closing_1", "kinology_closing_2",
            "kinology_link_text", "kinology_telegram_url", "kinology_instagram_url",
        )}),
        ("Любовь взаимна", {"fields": (
            "gifts_eyebrow", "gifts_heading", "gifts_heading_accent", "gifts_intro",
            "gifts_from_us_heading", "gifts_from_us_text",
            "gifts_from_you_heading", "gifts_from_you_text",
        )}),
        ("Отзывы — заголовок", {"fields": (
            "reviews_eyebrow", "reviews_heading", "reviews_heading_accent", "reviews_note",
        )}),
        ("Контакты", {"fields": (
            "contact_eyebrow", "contact_heading", "contact_heading_accent", "contact_description",
            "phone", "telegram_url", "whatsapp_url", "instagram_url", "max_url", "yandex_maps_url",
            "address", "hours", "map_note",
        )}),
        ("Подвал", {"fields": ("footer_tagline", "footer_copyright")}),
    )

    def has_add_permission(self, request):
        return not SiteContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Tagline)
class TaglineAdmin(admin.ModelAdmin):
    list_display = ("text", "order")
    list_editable = ("order",)


@admin.register(CareFeature)
class CareFeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order")
    list_editable = ("order",)


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ("value", "label", "order")
    list_editable = ("order",)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "image", "order")
    list_editable = ("order",)


class LocationHighlightInline(admin.TabularInline):
    model = LocationHighlight
    extra = 1


class LocationPhotoInline(admin.TabularInline):
    model = LocationPhoto
    extra = 1


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "tagline", "address", "order")
    list_editable = ("order",)
    inlines = [LocationHighlightInline, LocationPhotoInline]


@admin.register(PackingItem)
class PackingItemAdmin(admin.ModelAdmin):
    list_display = ("text", "order")
    list_editable = ("order",)


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ("period", "icon", "order")
    list_editable = ("order",)


@admin.register(KinologyTask)
class KinologyTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order")
    list_editable = ("order",)


@admin.register(GiftPhoto)
class GiftPhotoAdmin(admin.ModelAdmin):
    list_display = ("caption", "group", "image", "order")
    list_editable = ("order",)
    list_filter = ("group",)


class ReviewPhotoInline(admin.TabularInline):
    model = ReviewPhoto
    extra = 1


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "created_at", "order")
    list_editable = ("order",)
    list_filter = ("rating",)
    inlines = [ReviewPhotoInline]
