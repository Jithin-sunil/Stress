from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Administrator.models import*
from Psychologist.models import*

from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Count
from django.http import JsonResponse
import random
import joblib
import numpy as np
from datetime import datetime

# Load model once (outside function)
model = joblib.load("Assets/Model/stress_model.pkl")


def logout(request):
    del request.session['uid']
    return redirect("Guest:Login")

def HomePage(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        return render(request,'User/HomePage.html')
def MyProfile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        userdata=tbl_newuser.objects.get(id=request.session["uid"])
        return render(request,'User/MyProfile.html',{"userdata":userdata})
   
     
def EditProfile(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        userdata.user_name=name
        userdata.user_email=email
        userdata.user_contact=contact
        userdata.user_address=address
        userdata.save()
        return render(request,'User/EditProfile.html',{"msg":"Data updated"})
    else:
        return render(request,'User/EditProfile.html',{"userdata":userdata})
def ChangePassword(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    if request.method=="POST":
        opassword=request.POST.get("o_password")
        npassword=request.POST.get("n_password")
        cpassword=request.POST.get("c_password")
        if opassword==userdata.user_password:
           if npassword==cpassword:
              userdata.user_password=cpassword
              userdata.save()
              return render(request,'User/ChangePassword.html',{"msg":"Password Changed"})
           else:
              return render(request,'User/ChangePassword.html',{"msg":"Invalid Password"})
        else:
            return render(request,'User/ChangePassword.html',{"msg":"Invalid old Password"})
    else:
        return render(request,'User/ChangePassword.html',{'userdata':userdata})
def Complaint(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    userid=tbl_newuser.objects.get(id=request.session["uid"])
    userdata=tbl_complaint.objects.all()
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,userid=userid)
        return redirect('User:Complaint')
    else:
        return render(request,'User/Complaint.html', {'userdata':userdata})
def delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request,'User/Complaint.html',{"msg":"Data Deleted"})   
def Feedback(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    userid=tbl_newuser.objects.get(id=request.session["uid"])
    userdata=tbl_feedback.objects.all()
    if request.method=="POST":
        content=request.POST.get("txt_content")
        tbl_feedback.objects.create(feedback_content=content,userid=userid)
        return redirect('User:Feedback')
    else:
        return render(request,'User/Feedback.html', {'userdata':userdata})
def delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return render(request,'User/feedback.html',{"msg":"Data Deleted"}) 
def ViewPsychologist(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    psychologistdata=tbl_psychologist.objects.all()
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    parry = []
    ar = [1, 2, 3, 4, 5]  
    tot = 0
    for i in psychologistdata:
        ratecount = tbl_rating.objects.filter(psychologist=i.id).count()
        if ratecount > 0:
            ratedata = tbl_rating.objects.filter(psychologist=i.id)
            for j in ratedata:
                tot += j.rating_data
            avg = tot // ratecount
            parry.append(avg)
        else:
            parry.append(0)
    datas = zip(psychologistdata, parry)
    if request.method=="POST":
        placeid=tbl_place.objects.get(id=request.POST.get("sel_place"))
        psychologistdata=tbl_psychologist.objects.filter(psychologist_place=place)
        tot = 0
        for i in psychologistdata:
            ratecount = tbl_rating.objects.filter(psychologist=i.id).count()
            if ratecount > 0:
                ratedata = tbl_rating.objects.filter(psychologist=i.id)
                for j in ratedata:
                    tot += j.rating_data
                avg = tot // ratecount
                parry.append(avg)
            else:
                parry.append(0)
        datas = zip(psychologistdata, parry)
        return render(request,'User/ViewPsychologist.html',{'psychologistdata':datas,'ar':ar,'districts':district})
    else:
        return render(request,'User/ViewPsychologist.html',{'psychologistdata':datas,'ar':ar,'districts':district})
def ViewSlot(request,pid):
   user_id=tbl_newuser.objects.get(id=request.session["uid"])
   slotdata=tbl_slot.objects.all()
   bookingdata=tbl_booking.objects.all()
   if request.method=="POST":
        slotid=tbl_slot.objects.get(id=request.POST.get("sel_time"))
        description=request.POST.get("txt_description")
        tbl_booking.objects.create(slot_id=slotid,booking_description=description,user_id=user_id)
        return render(request,'User/ViewSlot.html',{'bookingdata':bookingdata,'slotdata':slotdata,'pid':pid,"msg":"slot booked"})
   else:
        return render(request,'User/ViewSlot.html',{'bookingdata':bookingdata,'slotdata':slotdata,'pid':pid})
def Ajaxdate(request):
    date=request.GET.get("did")
    pid=request.GET.get("pid")
    slot=tbl_slot.objects.filter(psychologist_id=pid,slot_date=date)
    booking = tbl_booking.objects.all()

    booked = []

    for i in booking:
        booked.append(i.slot_id.id)

    return render(request, 'User/Ajaxdate.html', {
        'slot': slot,
        'booked': booked
    })
    return render(request,"User/Ajaxdate.html",{'slot':slot})
def MyBooking(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    bookingdata=tbl_booking.objects.all()
    return render(request,"User/MyBooking.html",{'bookingdata':bookingdata})
def Payment(request,pid):
    bookingdata=tbl_booking.objects.get(id=pid)
    if request.method=="POST":
       bookingdata.booking_status=4
       bookingdata.booking_amount
       bookingdata.save()
       return render(request,'User/Payment.html',{"msg":"Payment Done"})
    else:
        return render(request,'User/Payment.html',{'bookingdata':bookingdata})



def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(psychologist=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(psychologist=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_newuser.objects.get(id=request.session['uid']),user_review=user_review,rating_data=rating_data,psychologist=tbl_psychologist.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(psychologist=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(psychologist=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(psychologist=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

    
    
def Ajaxpsychologist(request):
    disid = request.GET.get('disid')
    pid = request.GET.get('pid')
    if disid:
        data = tbl_psychologist.objects.filter(psychologist_place__district=disid)
    elif disid and pid:
        data = tbl_psychologist.objects.filter(psychologist_place=pid)
    else:
        data = tbl_psychologist.objects.all()
    return render(request, 'User/Ajaxpsychologist.html', {'data': data})

def choosetest(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    return render(request,'User/StressTest.html')

def ViewQuestion(request,lvl):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        data=tbl_questionlevel.objects.get(id=lvl)
        ViewQuesData = tbl_question.objects.filter(questionlevel=data).order_by('?')[:10]
        # print(ViewQuesData)
        return render(request,'User/ViewQuestion.html',{'questions':ViewQuesData})


def ViewQuestion(request, lvl):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    data = get_object_or_404(tbl_questionlevel, id=lvl)

    # FIXED: Get same 10 questions always for this level
    questions = list(tbl_question.objects.filter(questionlevel=data).order_by('id')[:10])

    if request.method == "POST":

        answers = []

        for q in questions:
            value = request.POST.get(f"question_{q.id}")

            if value is None:
                # If any question not answered, reject submission
                return render(request, "User/ViewQuestion.html", {
                    "questions": questions,
                    "error": "Please answer all questions."
                })

            answers.append(int(value))

        # Ensure exactly 10 features
        if len(answers) != 10:
            return render(request, "User/ViewQuestion.html", {
                "questions": questions,
                "error": "Invalid submission."
            })

        input_data = np.array(answers).reshape(1, -1)

        print("Answers:", answers)
        print("Shape:", input_data.shape)

        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        print("Prediction:", prediction)
        print("Probabilities:", probabilities)


        result_map = {
            0: "Low Stress",
            1: "Moderate Stress",
            2: "High Stress",
            3: "Severe Stress"
        }

        # Score ranges for each level
        score_range = {
            "Low Stress": (0, 25),
            "Moderate Stress": (26, 50),
            "High Stress": (51, 75),
            "Severe Stress": (76, 100)
        }

        result = result_map.get(prediction, "Unknown")

        # Assign random score based on result
        if result in score_range:
            score = random.randint(*score_range[result])
        else:
            score = 0  # fallback
        remedies = tbl_remedies.objects.filter(remedies_stresslevel=result).order_by('?')[:4]

        confidence = round(max(probabilities) * 100, 2)

        userid=tbl_newuser.objects.get(id=request.session['uid'])
        tbl_stressresult.objects.create(user=userid,total_score=score,stress_level=result)

        return render(request, "User/Result.html", {
            "result": result,
            "confidence": confidence,
            "remedies":remedies

        })

    return render(request, "User/ViewQuestion.html", {
        "questions": questions
    })

def SubmitStressTest(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    if request.method == "POST":
        total_score = 0
        
        for key, value in request.POST.items():
            if key.startswith("question_"):
                option = tbl_option.objects.get(id=value)
                total_score += option.stress_weight
        
        # classify stress level
        if total_score <= 5:
            level = "Low Stress"
        elif total_score <= 25:
            level = "Moderate Stress"
        else:
            level = "Extreme Stress"
        
        userid=tbl_newuser.objects.get(id=request.session['uid'])
        tbl_stressresult.objects.create(user=userid,total_score=total_score,stress_level=level)

        
        return render(request, "User/Result.html", {
            "score": total_score,
            "level": level.capitalize,
        })

def viewstressresult(request):
    if "uid" not in request.session:
        return redirect("Guest:Login")
    else:
        data=tbl_stressresult.objects.filter(user=request.session['uid'])
        return render(request,"User/ViewStressResult.html",{"data" :data})


def breathex(request):
    return render(request,'User/BreathingExcercise.html')