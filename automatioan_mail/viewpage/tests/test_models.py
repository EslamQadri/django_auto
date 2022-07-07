from django.test import TestCase
from viewpage.models import Emailsdatabase,Feedback

class TestModels(TestCase):
    # test 8
    def test_Emailsdatabase(self):
        q=Emailsdatabase.objects.create(email='kalba@dog.eg')
        self.assertEqual(q.email,'kalba@dog.eg')
    