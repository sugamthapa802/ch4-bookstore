from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from .forms import CustomUserCreationForm
from .views import SignUpView
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

class SignUpPageTests(TestCase):
    def setUp(self):
        url=reverse('signup')
        self.response=self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertContains(self.response,'Sign Up')
        self.assertTemplateUsed(self.response,'registration/signup.html')
        self.assertNotContains(self.response,"hi,i shouldn't be here")
    
    def test_signup_form(self):
        form=self.response.context.get('form')
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response,'csrfmiddlewaretoken')
    
    def test_signup_view(self):
        view=resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__,SignUpView.as_view().__name__)