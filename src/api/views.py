import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from src.api.models import Item




class ItemList(ListView):

    model = Item
    template_name = 'item_list.html'
    context_object_name = 'item_list'


class ItemView(DetailView):

    model = Item
    template_name = 'item.html'
    context_object_name = 'item'


class ItemBuy(View):
    stripe.api_key = settings.SK_STRIPE_KEY

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        stripe_session = stripe.checkout.Session.create(
            success_url='http://127.0.0.1:8000/',
            cancel_url='http://127.0.0.1:8000/',
            mode='payment',
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price * 100,
                },
                'quantity': 1,
            }],
        )
        return JsonResponse({'id': stripe_session.id})
