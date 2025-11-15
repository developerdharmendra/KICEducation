from django.conf import settings

from .models import Country, TestPreparationClass


def kic_global_context(request):
    countries = Country.objects.only('id', 'name', 'slug', 'flag')
    preparation_classes = TestPreparationClass.objects.defer('overview')

    return {
        'SITE_NAME': settings.SITE_NAME,
        'KIC_EMAIL_ADDRESS': settings.KIC_EMAIL_ADDRESS,
        'KIC_ADDRESS': settings.KIC_ADDRESS,
        'countries': countries,
        'preparation_classes': preparation_classes,
    }
