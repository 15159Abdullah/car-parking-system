from django.shortcuts import render
from accountss.decorators import *
from accountss.models import CustomUser
from backend.models import *
from django.contrib import messages

@backend_required 
def index(request):
    user = len(CustomUser.objects.all())
    area = len(Area.objects.all())
    park = len(Parking.objects.all())
    req = Slots_Request.objects.all()
    lenth = len(req)
    return render(request,'admin_site/index.html', context={'length':lenth,'users':user,'areas':area,'parking':park,'slots_request':req})
 
#__________________User INfo___________________

@backend_required
def user_list(request):
    user = CustomUser.objects.all()
    return render(request,'admin_site/user/user_list.html',context={'users':user})

@backend_required
def delete_user(request,pk):
    user = CustomUser.objects.get(id=pk)
    CustomUser.delete(user)
    return redirect('user_list')



#__________________Contact INfo___________________

@backend_required
def contact_list(request):
    contact = Contact.objects.all()
    return render(request,'admin_site/contact/contact_list.html',context={'contacts':contact})

def delete_contact(request,pk):
    Contact.objects.get(id=pk).delete()
    return redirect('contact_list')

#__________________Area INfo___________________

@backend_required
def area_list(request):
    area = Area.objects.all()
    return render(request,'admin_site/area/area_list.html',context={'areas':area})

@backend_required
def add_area(request):
    if request.method=='POST':
        countrry = request.POST.get('country')
        area = request.POST.get('area')
        if Area.objects.filter(area_name=area):
            messages.warning(request,"Area Is Already Available!")
        else:
            Area(country=countrry,area_name=area).save()
    return render(request,'admin_site/area/add_area.html')

@backend_required
def update_area(request,pk):
    if request.method=='POST':
        are_id = request.POST.get('area_id')
        contry = request.POST.get('country')
        area = request.POST.get('area')
        Area(id=are_id,country=contry,area_name=area).save()
        return redirect('area_list')
    area = Area.objects.get(id=pk)
    return render(request,'admin_site/area/update_area.html',context={'areas':area})

@backend_required
def delete_area(request,pk):
    area = Area.objects.get(id=pk).delete()
    return redirect('area_list')

#__________________Parking INfo___________________

@backend_required
def parking_list(request):
    parking = Parking.objects.all()
    return render(request,'admin_site/parking/parking_list.html',context={'parkings':parking})

@backend_required
def add_parking(request):
    if request.method=='POST':
        area_n = request.POST.get('select_area_name')
        parking = request.POST.get('parking_name')
        addresss = request.POST.get('parking_address')

        area_instance = Area.objects.get(area_name=area_n)
        Parking(area=area_instance,name=parking,address=addresss).save()
    area = Area.objects.all()
    return render(request,'admin_site/parking/add_parking.html',context={'areas':area})

@backend_required
def update_parking(request,pk):
    if request.method=='POST':
        park_id = request.POST.get('parking_id')
        area_n = request.POST.get('select_area_name')
        parking = request.POST.get('parking_name')
        addresss = request.POST.get('parking_address')
        try:
            area_instance = Area.objects.get(area_name=area_n)
        except Area.DoesNotExist:
            return redirect('parking_list')
        Parking(id =park_id,area=area_instance,name=parking,address=addresss).save()
        return redirect('parking_list')     
    park = Parking.objects.get(id=pk)
    area = Area.objects.all()
    return render(request,'admin_site/parking/update_parking.html',context={'parking':park,'areas':area})

@backend_required
def delete_parking(request,pk):
    Parking.objects.get(id=pk).delete()
    return redirect('parking_list')



 
#__________________Slots INfo___________________
@backend_required
def confirm_slot(request,pk):
    slot = Slots_Request.objects.get(id=pk)
    slot.slot_status=True
    slot.save()
    return redirect('slots_request')


@backend_required
def checked(request,pk):
    slot = Slots.objects.get(id=pk)
    slot.slot_color=True
    slot.save()
    return redirect('slots_list')

@backend_required
def slots_list(request):
    slot = Slots.objects.all()
    return render(request,'admin_site/slots/slots_list.html',context={'slots':slot})

@backend_required
def add_slot(request):
    if request.method=='POST':
        parking_n = request.POST.get('select_parking_name')
        slotnumber = request.POST.get('number')
        slotprice = request.POST.get('price')

        
        if Slots.objects.filter(slots_number=slotnumber,parking__name =parking_n):
            messages.warning(request,"Slots Number Already Exist!")
        else:
            parking_instance = Parking.objects.get(name=parking_n)
            Slots(parking=parking_instance,slots_number=slotnumber,slots_price=slotprice).save()
    parking = Parking.objects.all()
    return render(request,'admin_site/slots/add_slot.html',context={'parkings':parking})

@backend_required
def update_slot(request,pk):
    if request.method=='POST':
        slotid = request.POST.get('slot_id')
        parking_n = request.POST.get('select_parking_name')
        slotnumber = request.POST.get('number')
        slotprice = request.POST.get('price')
        checked =  request.POST.get('check')
       

        try:
            parking_instance = Parking.objects.get(name=parking_n)
        except Parking.DoesNotExist:
            return redirect('slots_list')
        Slots(id=slotid,parking=parking_instance,slots_number=slotnumber,slots_price=slotprice).save()
        return redirect('slots_list')
    slot = Slots.objects.get(id=pk)
    park = Parking.objects.all()
    return render(request,'admin_site/slots/update_slot.html',context={'slots':slot,'parking':park})
 
@backend_required
def delete_slot(request,pk):
    Slots.objects.get(id=pk).delete()
    return redirect('slots_list')

@backend_required
def slots_request(request):
    req = Slots_Request.objects.all()
    return render(request,'admin_site/slots/slots_request.html',context={'requests':req})

def delete_slots_request(request,pk):
    reqs = Slots_Request.objects.get(id=pk).delete()
    return redirect('slots_request')

#____________________Invoice_______________

def invoice(request,pk):
    req=Slots_Request.objects.get(id=pk)
    return render(request,'admin_site/invoice/invoice_view.html',context={'requests':req}) 