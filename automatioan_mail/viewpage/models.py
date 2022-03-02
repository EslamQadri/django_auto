from asyncio.windows_events import NULL
from django.db import models

# Create your models here
class Emailsdatabase(models.Model):
    email_id = models.AutoField(primary_key=True)
    email =models.EmailField(null=False)
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    

                              

class Feedback (models.Model):
    massage_id=models.AutoField(primary_key=True)
    emailm=models.EmailField(max_length=254 ,blank = False,null = False)
    name = models.CharField(max_length=70 ,blank = True,null = False)
    subject= models.CharField(max_length=300 ,blank = True,null = False)
    message= models.TextField(max_length=1200,blank = False,null = False)
