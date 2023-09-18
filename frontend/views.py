from django.shortcuts import render , redirect , HttpResponse
from accountss.decorators import frontend_required
from backend.models import *
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    area = Area.objects.all()
    dic = {'page': 'home','areas':area}
    return render(request,'main_web/index.html',context=dic)

def about(request):
    dic = {'page': 'about'}
    return render(request,'main_web/about.html',context=dic)

def parking(request):
    area = Area.objects.all()
    park=Parking.objects.all()
    dic = {'page': 'parking','parking':park,'areas':area}
    return render(request,'main_web/parking.html',context=dic)

def search_parking(request):
    querys = request.GET.get('q')
    area = Area.objects.all()
    park=Parking.objects.all()
    dic = {'parking':park,'areas':area,'q':querys}
    return render(request,'main_web/search_parking.html',context=dic)


@frontend_required
def booked(request,pk):
    detail = Slots.objects.get(id=pk)
    uid = request.session.get('_auth_user_id')
    user_now = CustomUser.objects.get(id = uid)
    if request.method == "POST":
        slotid=request.POST.get('slot_id')
        slot_number=request.POST.get('slot_no')
        slot_price=request.POST.get('slot_price')
        contact=request.POST.get('phone')
        number_plate=request.POST.get('num_plate')
        parking_name=request.POST.get('parking_name')
        category=request.POST.get('cat')
        add=request.POST.get('address')
        models=request.POST.get('model')
        indate = request.POST.get('in_date')
        outdate = request.POST.get('out_date')
        img= request.FILES.get('image_file')

        try:

            if img:
                bookeds=Slots_Request.objects.create(payment=img,slot_status=False,address=add,slots=detail,user=user_now,catogry=category,model=models,num_plate=number_plate,phone=contact,
                      in_date=indate,out_date=outdate)
                park=Parking.objects.get(name=parking_name)
                Slots(id=slotid,slots_price=slot_price,slots_number=slot_number,parking=park,slot_color=False).save()
                bookeds.save()
            else:

                bookeds=Slots_Request.objects.create(slot_status=False,address=add,slots=detail,user=user_now,catogry=category,model=models,num_plate=number_plate,phone=contact,
                      in_date=indate,out_date=outdate)
                park=Parking.objects.get(name=parking_name)
                Slots(id=slotid,slots_price=slot_price,slots_number=slot_number,parking=park,slot_color=False).save()
                bookeds.save()
        except Exception as e:
            print(e)
        try:
            email = request.user.email
            email_to = [email]
            email_from = settings.EMAIL_HOST_USER
            subject = f"Parking Lot Successfully BOOKED."
            message = f"""
                Hi MR {user_now}! YOUR bOOKING SLOT SATUS.
                
                PARKING     {parking_name}
                SLOTS NO.   {slot_number}
                VEHICLE     {category}
                VEHICLE NO. {number_plate}
                MODEL       {models}
                PRICE       {slot_price}
                CHECK-IN    {indate}
                CHECK-OUT   {outdate}
            
                CAR PARKING SYSTEM.
            
                THANK YOU!
                """
            send_mail(subject, message, email_from, email_to)
            return redirect('slot_order')
        except Exception as e:
            # Handle the exception here, you can log it or show an error message
            # For example:
            error_message = f"An error occurred: {str(e)}"
            return redirect('slot_order')

    
    return render(request,'main_web/booked.html',context={'details':detail})

def contact(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Message = request.POST.get('message')
        mail = Contact(name=Name,email=Email,subject=Subject,message = Message)
        mail.save()
        try:
            email_to = [Email]
            email_from = settings.EMAIL_HOST_USER
            subject = Subject
            message =  f'Hi MR.{Name}. We Have Received Your Email  THANK YOU FOR JIONING US! \n'+ Message
            send_mail(subject,message,email_from,email_to)
        except Exception as e:
            # Handle the exception here, you can log it or show an error message
            # For example:
            return HttpResponse(f"Networking Connection Error: {str(e)}")
    dic = {'page': 'contact'}
    return render(request,'main_web/contact.html',context=dic)

#@frontend_required
def slots(request,pk):
    lis=[]
    slot =Slots.objects.all()
    park=Parking.objects.get(id=pk)
    for slt in slot:
        if slt.parking == park:
            lis.append(slt)
            print('slot in parking ',slt)
    
    dic = {'page': 'parking','slots':lis,'parking':park}
    return render(request,'main_web/slots.html',context=dic)

def slot_order(request):
    users=request.user
    order = Slots_Request.objects.filter(user=users)
    print(order)
    dic = {'orders':order}
    return render(request,'main_web/slot_order.html',context=dic)

def profile(request,pk):
    users=request.user
    order = Slots_Request.objects.filter(user=users)
    print(order)
    dic = {'orders':order}
    return render(request,'main_web/profile.html',context=dic)

