from asyncio.windows_events import NULL
from dataclasses import fields
import email
from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import Feedback


class GetData(forms.Form):
    email=forms.EmailField(label=(''),required = True)





class GetMessageData(forms.ModelForm):
    
    class Meta :
       # write the name of models for which the form is made
        model = Feedback
            # Custom fields
        widgets =  {
            'emailm':forms.EmailInput(
                attrs={'class':'form-control','placeholder':"Your Email" ,'id':"email"}),
            'name':forms.TextInput(
                attrs={ 'class':"form-control",'id':"name" ,'placeholder':"Your Name"})
            ,'subject':forms.TextInput(
                attrs={'class':"form-control" ,'id':"subject", 'placeholder':"Subject"})
            ,'message':forms.Textarea(
                attrs={ 'class':"form-control",'rows':5,'placeholder':"Message"}
            )
   }
        
        fields=["emailm","name",'subject','message']
        def clean (self):
            super(GetMessageData,self).clean()
            name = self.cleaned_data.get('name')
            message = self.cleaned_data.get('message')

            if len(name) < 2:
                self._errors['name'] = self.error_class([
                    'Minimum 2 characters required'])
                if len(message) <10:
                    self._errors['message'] = self.error_class([
                        'Post Should Contain a minimum of 10 characters'])

                # return any errors if found
                return self.cleaned_data()
   



        