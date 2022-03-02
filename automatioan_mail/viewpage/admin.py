import email
from django.contrib import admin

# Register your models here.
from .models import Emailsdatabase,Feedback


class Emy(admin.ModelAdmin):
    list_display=['email_id','email','add_date'] 
class feedy(admin.ModelAdmin):
    list_display =['massage_id','emailm','name','subject','message']

admin.site.register(Emailsdatabase,Emy)
admin.site.register(Feedback,feedy)