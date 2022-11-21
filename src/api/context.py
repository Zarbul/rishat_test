from django.conf import settings


def stripe_api_public_key(request):
    return {
        'PK_STRIPE_KEY': settings.PK_STRIPE_KEY,
    }
