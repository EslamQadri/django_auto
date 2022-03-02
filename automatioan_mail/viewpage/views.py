from MySQLdb import DATE
from django.shortcuts import render
from viewpage.models import Emailsdatabase
from .forms import GetData,GetMessageData
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
def submet_email(request):
    print("Please work")
    if request.method== 'POST':
        email = request.POST['email'] #the main mail
        if email:

            if email!=None and email!= '':
                
                qwery =Emailsdatabase.objects.filter(email=email).exists()
                db =Emailsdatabase()

                if qwery :#if the email get email Previously 
                    #Send anther mail remmber him 
                    smail= EmailMessage(
                    'To Remember',
                    'You are Subscribed Previously \n',
                    settings.EMAIL_HOST_USER,
                    [email]
                    )
                    smail.send(fail_silently= False)
                    return HttpResponse("i will work 1")
                else :
                    #save in my data base 
                    #and sent to him message
                    db.email=email
                    db.save()
                    smail= EmailMessage(
                    'Congratulation',
                    'You Are Subscribe Now \n',
                    settings.EMAIL_HOST_USER,
                    [email]
                    )                
                    smail.send(fail_silently= False)
                return HttpResponse("i will work 2 ")
    return HttpResponse("i will work 3")            
        
def Contact_Us(request):
    
    message= request.POST['message']
    subject=request.POST['subject']
    name=request.POST['name']
    emailm=request.POST['emailm']
    db = GetMessageData(request.POST)
    print(db.is_valid())
    
    if db.is_valid():

        db.message=message
        db.subject=subject
        db.emailm=emailm
        db.name=name
        db.save()

    return HttpResponse("Done") 

def view(request):
    return render(request,'viewpage_app/the main page.html'
    ,{'emailform':GetData,'MessageForm':GetMessageData})
