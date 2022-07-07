from django.test import TestCase,Client
from django.urls import reverse ,resolve
from viewpage.views import submet_email,Contact_Us,view
from viewpage.models import Emailsdatabase ,Feedback
class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.Contact_Us=reverse('Contact_Us')
        self.view=reverse('my_page')
        self.submet_email=reverse('Ajax')
    def test_view_get(self):
        response = self.client.get(self.view)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'viewpage_app/the main page.html')
    def test_submet_email_post(self):
        response = self.client.post(self.submet_email,{
            'email': 'test@example.com'
        })
        self.assertEquals(response.status_code,200)