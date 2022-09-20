from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestCartView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django intermediate', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django advanced', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')
        self.client.post(
            reverse('cart:cart-add'), {"productId": 1, "productQty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('cart:cart-add'), {"productId": 2, "productQty": 2, "action": "post"}, xhr=True)

    def test_cart_url(self):
        response = self.client.get(reverse('cart:cart-summary'))
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        response = self.client.post(
            reverse('cart:cart-add'), {"productId": 3, "productQty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('cart:cart-add'), {"productId": 2, "productQty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 5})

    def test_cart_delete(self):
        response = self.client.post(
            reverse('cart:cart-delete'), {"productId": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '20.00'})

    def test_cart_update(self):
        response = self.client.post(
            reverse('cart:cart-update'), {"productId": 2, "productQty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.00'})
