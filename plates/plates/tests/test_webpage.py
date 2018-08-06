from django_webtest import WebTest
from django.urls import reverse


class IndexPageTestCase(WebTest):
    def test_index_page(self):
        response = self.app.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
