from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(username='will',
                                      email='will@email.com',
                                      password='test123')
        self.assertEqual(user.username,'will')
        self.assertEqual(user.email,'will@email.com')
        self.assertTrue(user.check_password('test123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)


    def test_create_superuser(self):
        User=get_user_model()
        user=User.objects.create_superuser(username='boss',
                                           email='boss@email.com',
                                           password='boss123')
        self.assertEqual(user.username,'boss')
        self.assertEqual(user.email,'boss@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
