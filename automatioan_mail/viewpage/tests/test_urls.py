from viewpage.views import submet_email,Contact_Us,view
from django.test import SimpleTestCase
from django .urls import reverse,resolve

class TestUrls(SimpleTestCase):
    #test 1 : 
    def test_view(self):
        url = reverse('my_page')
        self.assertEqual(resolve(url).func,view)
    #test 2:
    def test_submet_email(self):
        url=reverse('Ajax')
        self.assertEqual(resolve(url).func,submet_email)
    #test 3 : 
    def test_Contact_Us(self):
        url=reverse('Contact_Us')
        self.assertEqual(resolve(url).func,Contact_Us)
