from django.urls import reverse,resolve
from django.test import SimpleTestCase
from .views import AboutPageView

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

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url=reverse('about')
        self.response=self.client.get(url)
    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code,200)
    def test_about_uses_correct_template(self):
        self.assertTemplateUsed(self.response,'about.html')
    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response,'About page')
    def test_about_url_resolves_AboutPageView(self):
        view=resolve('/about/')
        self.assertEqual(view.func.__name__,AboutPageView.as_view().__name__)
