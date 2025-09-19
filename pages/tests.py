from django.urls import reverse
from django.test import SimpleTestCase


class CustomTestCase(SimpleTestCase):

    def setUp(self):
        url=reverse('home')
        self.response=self.client.get(url)

    def test_url_at_right_path(self):
        self.assertEqual(self.response.status_code,200)
    def test_url_name_works(self):
        self.assertEqual(self.response.status_code,200)

    def test_template_contains(self):
        # response=self.client.get('/')
        self.assertContains(self.response,'home page')
    
    def test_doesnot_contain(self):
        response=self.client.get('/')
        self.assertNotContains(response,'hi,i shouldnot be there.')