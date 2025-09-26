from django.test import TestCase
from django.urls import reverse
from .models import Book,Review
from django.contrib.auth import get_user_model

class Booktests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user=get_user_model().objects.create_user(username='reviewuser',
                                                 email='reviewuser@gmail.com',
                                                 password='lofi*321'
                                            
                                            )
        cls.book =Book.objects.create(title='book1',author='harry',price='29.00')
        cls.reviewbook=Review.objects.create(
            book=cls.book,
            review='Excellent book',
            user=cls.user

        )

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
        self.assertContains(response,'Excellent book')