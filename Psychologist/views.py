from django.shortcuts import render,redirect
from Psychologist.models import *
from Guest.models import *
from User.models import *
def logout(request):
    del request.session['pid']
    return redirect("Guest:Login")
def HomePage(request):
    if "pid" not in request.session:
        return redirect("Guest:Login")
    else:
        return render(request,'Psychologist/HomePage.html')
def MyProfile(request):
    if "pid" not in request.session:
        return redirect("Guest:Login")
    else:
        psychologistdata=tbl_psychologist.objects.get(id=request.session["pid"])
        return render(request,'Psychologist/MyProfile.html',{"psychologistdata":psychologistdata})

  
def EditProfile(request):
    if "pid" not in request.session:
        return redirect("Guest:Login")
    psychologistdata=tbl_psychologist.objects.get(id=request.session["pid"])
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        psychologistdata.psychologist_name=name
        psychologistdata.psychologist_email=email
        psychologistdata.psychologist_contact=contact
        psychologistdata.psychologist_address=address
        psychologistdata.save()
        return render(request,'Psychologist/EditProfile.html',{"msg":"Data updated"})
    else:
        return render(request,'Psychologist/EditProfile.html',{"psychologistdata":psychologistdata})
def ChangePassword(request):
    if "pid" not in request.session:
        return redirect("Guest:Login")
    psychologistdata=tbl_psychologist.objects.get(id=request.session["pid"])
    if request.method=="POST":
        opassword=request.POST.get("o_password")
        npassword=request.POST.get("n_password")
        cpassword=request.POST.get("c_password")
        if opassword==psychologistdata.psychologist_password:
           if npassword==cpassword:
              psychologistdata.psychologist_password=cpassword
              psychologistdata.save()
              return render(request,'Psychologist/ChangePassword.html',{"msg":"Password Changed"})
           else:
              return render(request,'Psychologist/ChangePassword.html',{"msg":"Invalid Password"})
        else:
            return render(request,'Psychologist/ChangePassword.html',{"msg":"Invalid old Password"})
    else:
        return render(request,'Psychologist/ChangePassword.html',{'psychologistdata': psychologistdata})
def Complaint(request):
    if "pid" not in request.session:
        return redirect("Guest:Login")
    psychologistid=tbl_psychologist.objects.get(id=request.session["pid"])
    psychologistdata=tbl_complaint.objects.all()
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,psychologistid=psychologistid)
        return render(request,'Psychologist/Complaint.html',{"msg":"Data inserted"})
    else:
        return render(request,'Psychologist/Complaint.html', {'psychologistdata':psychologistdata})
def delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request,'Psychologist/Complaint.html',{"msg":"Data Deleted"})   
def AddSlot(request):
   if "pid" not in request.session:
        return redirect("Guest:Login")
   psychologistid=tbl_psychologist.objects.get(id=request.session["pid"])
   psychologistdata=tbl_slot.objects.all()
   if request.method=="POST":
        date=request.POST.get("txt_date")
        ftime=request.POST.get("txt_ftime")
        ttime=request.POST.get("txt_ttime")
        tbl_slot.objects.create(slot_date=date,slot_fromtime=ftime,slot_totime=ttime,psychologist_id=psychologistid)
        return render(request,'Psychologist/AddSlot.html',{"msg":"Data inserted",'psychologistdata':psychologistdata})
   else:
        return render(request,'Psychologist/AddSlot.html',{'psychologistdata':psychologistdata})
def deladdslot(request,did):
    tbl_slot.objects.get(id=did).delete()
    return render(request,'Psychologist/AddSlot.html',{"msg":"Data Deleted"})   
def ViewBooking(request):
    if "pid" not in request.session:
        return redirect("Guest:Login")
    bookingdata=tbl_booking.objects.all()
    return render(request,"Psychologist/ViewBooking.html",{'bookingdata':bookingdata})
def accept(request,id):
    bookingdata=tbl_booking.objects.get(id=id)
    bookingdata.booking_status=1
    bookingdata.save()
    return render(request,'Psychologist/ViewBooking.html',{"msg":"Verified"})
def reject(request,id):
    bookingdata=tbl_booking.objects.get(id=id)
    bookingdata.booking_status=2
    bookingdata.save()
    return render(request,'Psychologist/ViewBooking.html',{"msg":"rejected"})
def Fee(request,fid):
    user_id=tbl_booking.objects.filter(id=request.session["uid"])
    bookingdata=tbl_booking.objects.get(id=fid)
    if request.method=="POST":
        amount=request.POST.get("txt_amount")
        bookingdata.booking_status=3
        bookingdata.booking_amount=amount
        bookingdata.save()
        return render(request,'Psychologist/Fee.html',{'user_id':user_id,"msg":"Fee Added"})
    else:
        return render(request,'Psychologist/Fee.html',{'user_id':user_id})

def Complete(request,cid):
    bookingdata=tbl_booking.objects.get(id=cid)
    bookingdata.booking_status=5
    bookingdata.save()
    return render(request,'Psychologist/ViewBooking.html',{"msg":"Booking Compelted"})