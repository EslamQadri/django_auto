from django.test import TestCase
from viewpage.forms import GetData,GetMessageData
class TestForms(TestCase):
    #test 4
    def test_GetData_form_is_valid(self):
        form= GetData(data={
            'email':'kalba@dogs.com'
        })
        self.assertTrue(form.is_valid())
    #Test 5 
    def test_GetData_form_NO_Data(self):
        form= GetData(data={})
        self.assertFalse(form.is_valid()) 
        self.assertEqual(len(form.errors), 1
        )
    #Test 6
    def test_GetMessageData_is_valid(self):  
        form =GetMessageData(data={
            'emailm':'kalba@dogs.com',
            'name':'Test Or die ',
            'subject':'thanks',
            'message':'why !!!!!!!!!!!!!!!!!!!!!!!!!!!'

            })
        self.assertTrue(form.is_valid())
    #Test 7
    def test_GetMessageData_no_data(self):  
        form =GetMessageData(data={})
        self.assertFalse(form.is_valid()) 
        self.assertEqual(len(form.errors), 2)