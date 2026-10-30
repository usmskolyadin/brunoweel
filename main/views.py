from django.shortcuts import render

from .models import (
    CareFeature,
    GalleryImage,
    GiftPhoto,
    KinologyTask,
    Location,
    PackingItem,
    ScheduleItem,
    SiteContent,
    Stat,
    Tagline,
)


def home(request):
    context = {
        "content": SiteContent.load(),
        "care_features": CareFeature.objects.all(),
        "stats": Stat.objects.all(),
        "taglines": Tagline.objects.all(),
        "gallery_images": GalleryImage.objects.all(),
        "locations": Location.objects.prefetch_related("highlights", "photos").all(),
        "packing_items": PackingItem.objects.all(),
        "schedule_items": ScheduleItem.objects.all(),
        "kinology_tasks": KinologyTask.objects.all(),
        "gifts_from_us": GiftPhoto.objects.filter(group=GiftPhoto.Group.FROM_US),
        "gifts_from_you": GiftPhoto.objects.filter(group=GiftPhoto.Group.FROM_YOU),
    }
    return render(request, "main/index.html", context)
