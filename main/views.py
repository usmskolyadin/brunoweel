from django.shortcuts import render

from .models import (
    CareFeature,
    GalleryImage,
    KinologyTag,
    Location,
    PackingItem,
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
        "kinology_tags": KinologyTag.objects.all(),
    }
    return render(request, "main/index.html", context)
