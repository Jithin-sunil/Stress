from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.

def NewUser(request):
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("gender")
        dob=request.POST.get("txt_dob")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        confirmpassword=request.POST.get("txt_confirmpassword")
        placeid=tbl_place.objects.get(id=request.POST.get("sel_place"))
        address=request.POST.get("txt_address")
        proof=request.FILES.get("proof")
        photo=request.FILES.get("photo")
        if password == confirmpassword:
            tbl_newuser.objects.create(
            user_name=name,
            user_gender=gender,
            user_dob=dob,
            user_contact=contact,
            user_email=email,
            user_password=password,
            user_place=placeid,
            user_address=address,
            user_photo=photo,
            user_proof=proof
             )
            # return redirect('Guest:NewUser')
            return render(request,'Guest/NewUser.html',{"msg":"data inserterd"})
        else:
            return render(request,'Guest/NewUser.html',{"msg":"password missmatch"})
    else:
        return render(request,'Guest/NewUser.html',{'districts':district})
def Ajaxplace(request):
    district=request.GET.get("did")
    placedata=tbl_place.objects.filter(district=district)
    return render(request,"Guest/Ajaxplace.html",{'places':placedata})
def Login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        usercount=tbl_newuser.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        psychologistcount=tbl_psychologist.objects.filter(psychologist_email=email,psychologist_password=password).count()
        if usercount>0:
            userdata=tbl_newuser.objects.get(user_email=email,user_password=password)
            request.session["uid"]=userdata.id
            return redirect("User:HomePage")
        elif admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["aid"]=admindata.id
            return redirect("Administrator:AdminHome")
        elif psychologistcount>0:
            psychologistdata=tbl_psychologist.objects.get(psychologist_email=email,psychologist_password=password)
            request.session["pid"]=psychologistdata.id
            return redirect("Psychologist:HomePage")

        else:
            return render(request,"Guest/Login.html",{'msg':"invalid email or password"})
         
    else:
         return render(request,"Guest/Login.html")
def PsychologistRegistration(request):
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        placeid=tbl_place.objects.get(id=request.POST.get("sel_place"))
        photo=request.FILES.get("photo")
        proof=request.FILES.get("proof")
        password=request.POST.get("txt_password")
        tbl_psychologist.objects.create(
        psychologist_name=name,
        psychologist_email=email,
        psychologist_contact=contact,
        psychologist_address=address,
        psychologist_place=placeid,
        psychologist_photo=photo,
        psychologist_proof=proof,
        psychologist_password=password
        )
        return render(request,'Guest/PsychologistRegistration.html',{"msg":"data inserterd"})
    else:
        return render(request,'Guest/PsychologistRegistration.html',{'districts':district})
def Index(request):
    
    return render(request,'Guest/Index.html')
    

def forgotpassword(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")
        usercount = tbl_newuser.objects.filter(user_email=email).count()
        psychologistcount = tbl_psychologist.objects.filter(psychologist_email=email).count()
        otp = random.randint(111111,999999)
        request.session['otp'] = otp
        if usercount>0:
            userdata = tbl_newuser.objects.get(user_email=email)
            request.session['userid'] = userdata.id
            send_mail(
            "Forgot password Otp ",
            "\r Hello \r" + str(otp) + "\r the recovery otp \r",

            settings.EMAIL_HOST_USER,
            [email],
            )
            return redirect("Guest:otp")
        elif psychologistcount > 0:
             psychologistdata = tbl_psychologist.objects.get(psychologist_email=email)
             request.session['psychologistid'] = psychologistdata.id
             request.session['otp'] = otp
             send_mail(
              "Forgot password otp",
                "\r Hello \r" + str(otp) + "\r the recovery otp \r",
             settings.EMAIL_HOST_USER,
             [email],
              )
             return redirect("Guest:otp")
            
        else:
            return render(request,"Guest/ForgotPassword.html",{'msg':"Account Not Found"})
    else:
        return render(request,"Guest/ForgotPassword.html")

def otp(request):
    if request.method == "POST":
        int_otp=int(request.POST.get("txt_otp"))
        if int_otp ==  request.session['otp']:
            return redirect("Guest:newpassword")
        else:
            return render(request,'Guest/otp.html',{'msg':"the give otp is not matching"})
    else:
        return render(request,'Guest/OTP.html')


def newpassword(request):
    if request.method == "POST":
        if request.POST.get("txt_newpass") == request.POST.get("txt_confirmpass"):
            if "userid" in request.session:
               userdata= tbl_newuser.objects.get(id=request.session['userid'])
               userdata.user_password =  request.POST.get("txt_newpass")
               userdata.save()
               del request.session['userid']
               return  redirect("Guest:Login") 
            elif "psychologistid" in request.session:
                psychologistdata = tbl_psychologist.objects.get( id=request.session['psychologistid'] )
                psychologistdata.psychologist_password = request.POST.get("txt_newpass")
                psychologistdata.save()
                del request.session['psychologistid']
                return redirect("Guest:Login")
        else:
            return render(request,"Guest/NewPassword.html",{'msg':"Password Doesnt Match.."})
    else:
        return render(request,"Guest/NewPassword.html")