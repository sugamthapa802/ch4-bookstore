from django.test import TestCase
from django.urls import reverse
from .models import Book

class Booktests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book =Book.objects.create(title='book1',author='harry',price='29.00')
    
    def test_book_title(self):
        self.assertEqual(f'{self.book.title}','book1')
        self.assertEqual(f'{self.book.author}','harry')
        self.assertEqual(f'{self.book.price}','29.00')
    
    def test_book_list_view(self):
        response=self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'book1')
        self.assertTemplateUsed(response,'books/book_list.html')
    
    def test_book_detail_view(self):
        response=self.client.get(self.book.get_absolute_url())
        no_response=self.client.get('book/12345')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'book1')
        self.assertTemplateUsed(response,'books/book_detail.html')