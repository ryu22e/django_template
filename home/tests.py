from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeViewTest(TestCase):
    def test_show_page(self):
        r = self.client.get(reverse('home'))
        self.assertEqual(r.status_code, 200)
