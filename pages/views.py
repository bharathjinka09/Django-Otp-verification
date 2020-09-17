from django.shortcuts import render,redirect
from .models import Contact1
from random import randint
from django.contrib import messages
import requests
# Create your views here.


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

x = random_with_N_digits(6)
 


def index(request):
    return render(request, 'pages/index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        last_name = request.POST['last_name']
        mobile_number = request.POST['mobile_number']
        Blood_type = request.POST['Blood_type']
        City = request.POST['City']
        email_id = request.POST['email_id']
        date_day = request.POST['date_day']
        Sample_text = request.POST['Sample_text']
        gender = request.POST['gender']

        otp = x
        print(otp)

        sms = 'http://mobicomm.dove-sms.com/mobicomm//submitsms.jsp?user=MOSLTD&key=de5a73a623XX&mobile='+mobile_number+'&message=The OTP for your plasma donation is '+str(otp)+'&senderid=INFOSM&accusage=1'
        receive = requests.get(sms)                

        contact = Contact1(name=name, last_name=last_name, mobile_number=mobile_number, Blood_type=Blood_type, City=City,
        email_id=email_id, date_day=date_day, Sample_text=Sample_text,gender=gender,otp=x)
        
        contact.save()

        return redirect('new')


def new(request):
    contacts = Contact1.objects.all()

    context = {
        'contacts' : contacts
    }
    return render(request,'pages/new.html',context)
    

def verification(request):      
    
    if request.method == "POST":
        otp_1 = int(request.POST['otp'])
        
        # print(otp_1)
    
    # mobile_number = request.POST['mobile_number']
   
    
    # print(mobile_number)

        print('This is the value of x :',x)     
        print('Variable verification of otp_1', otp_1)

        if (otp_1 == x):        
            messages.success(request, 'Your OTP has been verified and you are registered Succesfully!')

            mn = Contact1.objects.latest('mobile_number').mobile_number
            print(mn)
            print('mn')
            Contact1.objects.filter(mobile_number=mn).update(is_verified=True)
            print('Verified Succesfully !')

                
            
        else:
            messages.warning(request, 'The OTP entered is invalid')
        
        
    


    return render(request,'pages/new.html')    

        
        
