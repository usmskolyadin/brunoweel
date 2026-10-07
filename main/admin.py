from django.contrib import admin

from .models import (
    CareFeature,
    GalleryImage,
    KinologyTag,
    Location,
    LocationHighlight,
    LocationPhoto,
    PackingItem,
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
        ("Забота", {"fields": ("care_eyebrow", "care_heading", "care_heading_accent", "care_description")}),
        ("Тихий час", {"fields": (
            "quiet_hour_eyebrow", "quiet_hour_heading", "quiet_hour_heading_accent",
            "quiet_hour_text", "quiet_hour_photo",
        )}),
        ("Локации — заголовок", {"fields": (
            "locations_eyebrow", "locations_heading", "locations_heading_accent", "locations_intro",
            "locations_choice_heading",
            "locations_choice_apartment_title", "locations_choice_apartment_text",
            "locations_choice_house_title", "locations_choice_house_text",
        )}),
        ("Галерея — заголовок", {"fields": ("gallery_eyebrow", "gallery_heading", "gallery_heading_accent", "gallery_note")}),
        ("Что взять с собой — заголовок", {"fields": ("packing_eyebrow", "packing_heading", "packing_heading_accent", "packing_intro")}),
        ("Кинология (услуга)", {"fields": (
            "kinology_eyebrow", "kinology_heading", "kinology_heading_accent", "kinology_description",
            "kinology_telegram_url", "kinology_instagram_url",
        )}),
        ("Контакты", {"fields": (
            "contact_eyebrow", "contact_heading", "contact_heading_accent", "contact_description",
            "phone", "telegram_url", "whatsapp_url", "instagram_url", "address", "hours", "map_note",
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


@admin.register(KinologyTag)
class KinologyTagAdmin(admin.ModelAdmin):
    list_display = ("text", "order")
    list_editable = ("order",)
