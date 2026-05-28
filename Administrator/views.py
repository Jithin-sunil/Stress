from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
from User.models import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def logout(request):
    del request.session['aid']
    return redirect("Guest:Login")
def District(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        districtname=request.POST.get("txt_district")
        tbl_district.objects.create(district_name=districtname)
        return render(request,'Administrator/District.html',{"msg":"Data inserted.."})
    else:
        return render(request,'Administrator/District.html',{'districtdata':districtdata})
def Category(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        categoryname=request.POST.get("txt1")
        tbl_category.objects.create(category_name=categoryname)
        return render(request,'Administrator/Category.html',{"msg":"Data inserted.."})
    else:
        return render(request,'Administrator/Category.html',{'categorydata':categorydata})
def AdminRegistration(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    admindata=tbl_admin.objects.all()
    if request.method=="POST":
        adminname=request.POST.get("txt_name")
        admincontact=request.POST.get("txt_contact")
        adminemail=request.POST.get("txt_email")
        adminpassword=request.POST.get("txt_password")
        tbl_admin.objects.create(
        admin_name=adminname,
        admin_contact=admincontact,
        admin_email=adminemail,
        admin_password=adminpassword)

        return render(request,'Administrator/AdminRegistration.html',{"msg":"Data inserted.."})
    else:
        return render(request,'Administrator/AdminRegistration.html',{'admindata':admindata})
def Brand(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    branddata=tbl_brand.objects.all()
    if request.method=="POST":
        brandname=request.POST.get("txt_brand")
        tbl_brand.objects.create(brand_name=brandname)
        return render(request,'Administrator/Brand.html',{"msg":"Data inserted.."})
    else:
        return render(request,'Administrator/Brand.html',{'branddata':branddata})
def Type(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    typedata=tbl_type.objects.all()
    if request.method=="POST":
        typename=request.POST.get("txt_type")
        tbl_type.objects.create(type_name=typename)
        return render(request,'Administrator/Type.html',{"msg":"Data inserted.."})
    else:
        return render(request,'Administrator/Type.html',{'typedata':typedata})
def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Administrator/District.html',{"msg":"Data Deleted"})
def delcategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return render(request,'Administrator/Category.html',{"msg":"Data Deleted"})
def deladmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return render(request,'Administrator/AdminRegistration.html',{"msg":"Data deleted"})
def delbrand(request,did):
    tbl_brand.objects.get(id=did).delete()
    return render(request,'Administrator/Brand.html',{"msg":"Data Deleted"})
def deltype(request,did):
    tbl_type.objects.get(id=did).delete()
    return render(request,'Administrator/Type.html',{"msg":"Data deleted"})
def Place(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    placedata=tbl_place.objects.all()
    districtdata= tbl_district.objects.all()
    if request.method=="POST":
        placename=request.POST.get("txt_pname")
        districtid=tbl_district.objects.get(id=request.POST.get("txt_name"))
        pincode=request.POST.get("txt_pincode")
        tbl_place.objects.create(
        place_name=placename,
        district=districtid,
        place_pincode=pincode)
        return render(request,'Administrator/Place.html',{"msg":"Data inserted.."})
    else:
        return render(request,'Administrator/Place.html',{'districts':districtdata,'places':placedata})
def SubCategory(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcategoryname=request.POST.get("txt_sname")
        categoryid=tbl_category.objects.get(id=request.POST.get("category"))
        tbl_subcategory.objects.create(
            subcategory_name=subcategoryname,
            category=categoryid)
        return render(request,'Administrator/SubCategory.html',{"msg":"Data inserted.."})     
    else:
        return render(request,'Administrator/SubCategory.html',{'categories':categorydata,'subcategories':subcategorydata})    
def editdistrict(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt_district")
        editdata.district_name=name
        editdata.save()
        return render(request,"Administrator/District.html",{"msg":"Data Updated"})
    else:
        return render(request,"Administrator/District.html",{'editdata':editdata})
def editadmin(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        editdata.admin_name=name
        editdata.admin_contact=contact
        editdata.admin_email=email
        editdata.admin_password=password
        editdata.save()
        return render(request,"Administrator/AdminRegistration.html",{"msg":"Data Updated"})
    else:
        return render(request,"Administrator/AdminRegistration.html",{'editdata':editdata})
def editcategory(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt1")
        editdata.category_name=name
        editdata.save()
        return render(request,"Administrator/Category.html",{"msg":"Data Updated"})
    else:
        return render(request,"Administrator/Category.html",{'editdata':editdata})
def editbrand(request,eid):
    editdata=tbl_brand.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt_brand")
        editdata.brand_name=name
        editdata.save()
        return render(request,"Administrator/Brand.html",{"msg":"Data Updated"})
    else:
        return render(request,"Administrator/Brand.html",{'editdata':editdata})
def edittype(request,eid):
    editdata=tbl_type.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt_type")
        editdata.type_name=name
        editdata.save()
        return render(request,"Administrator/Type.html",{"msg":"Data Updated.."})
    else:
        return render(request,"Administrator/Type.html",{'editdata':editdata})
def delplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return render(request,'Administrator/Place.html',{"msg":"Data Deleted"})
def editplace(request,eid):
    editdata=tbl_place.objects.get(id=eid)
    districts= tbl_district.objects.all()
    if request.method=="POST":
        districtid=tbl_district.objects.get(id=request.POST.get("txt_name"))
        placename=request.POST.get("txt_pname")
        pincode=request.POST.get("txt_pincode")
        editdata.district=districtid
        editdata.place_name=placename
        editdata.place_pincode=pincode
        editdata.save()
        return render(request,"Administrator/Place.html",{"msg":"Data Updated"})
    else:
        return render(request,"Administrator/Place.html",{'districts':districts,'editdata':editdata})
def Product(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()
    productdata=tbl_product.objects.all()
    if request.method=="POST":
        subcategoryid=tbl_subcategory.objects.get(id=request.POST.get("subcategory"))
        categoryid=tbl_category.objects.get(id=request.POST.get("category"))
        product=request.POST.get("txt_product")
        price=request.POST.get("txt_price")
        image=request.POST.get("image")
        tbl_product.objects.create(
            subcategory=subcategoryid,
            category=categoryid,
            product_name=product,
            product_price=price,
            product_image=image)
        return render(request,'Administrator/Product.html',{"msg":"Data inserted.."})     
    else:
        return render(request,'Administrator/Product.html',{'categories':categorydata,'subcategories':subcategorydata,'productdata':productdata})    
def delsubcategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return render(request,'Administrator/SubCategory.html',{"msg":"Data Deleted"})   
def editsubcategory(request,eid):
    editdata=tbl_subcategory.objects.get(id=eid) 
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        categoryid=tbl_category.objects.get(id=request.POST.get("category"))
        subcategoryname=request.POST.get("txt_sname")
        editdata.category=categoryid
        editdata.subcategory_name=subcategoryname
        editdata.save()
        return render(request,"Administrator/SubCategory.html",{"msg":"Data Updated"})
    else:
        return render(request,"Administrator/SubCategory.html",{'categories':categorydata,'editdata':editdata})
def UserList(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    userlist=tbl_newuser.objects.all()
    return render(request,"Administrator/UserList.html",{'listdata':userlist})
def AdminHome(request):
   totalpsy=tbl_psychologist.objects.all().count()
   totaluser=tbl_newuser.objects.all().count()
   totalcomp=tbl_complaint.objects.all().count()
   totalfeed=tbl_feedback.objects.all().count()
   recentfeed=tbl_feedback.objects.all()[:5]
   recentcomp=tbl_complaint.objects.all()
   return render (request,'Administrator/AdminHome.html',{'tp':totalpsy,
                                                       'tu':totaluser,
                                                       'tc':totalcomp,
                                                       'tf':totalfeed,
                                                       'rf':recentfeed,
                                                       'rc':recentcomp})
   
def ViewComplaint(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
         userdata=tbl_complaint.objects.filter(userid__isnull=False)
         psychologistdata=tbl_complaint.objects.filter(psychologistid__isnull=False)
         return render(request,'Administrator/ViewComplaint.html',{'userdata':userdata,'psychologistdata':psychologistdata})
   
def Reply(request,rid):
    replydata=tbl_complaint.objects.get(id=rid) 
    if request.method=="POST":
        reply=request.POST.get("txt_reply")
        replydata.complaint_reply=reply
        replydata.complaint_status=1
        replydata.save()
        return render(request,'Administrator/Reply.html',{'replydata':replydata,"msg":"rejected"})
    else:
         return render(request,'Administrator/Reply.html')
def ViewFeedback(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
         userdata=tbl_feedback.objects.all()
         return render(request,'Administrator/ViewFeedback.html',{'userdata':userdata})

   
def PsychologistList(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
         psychologistlist=tbl_psychologist.objects.all()
         return render(request,"Administrator/PsychologistList.html",{'listdata': psychologistlist})
def accept(request,id):
    data=tbl_psychologist.objects.get(id=id)
    email=data.psychologist_email
    data.psychologist_status=1
    data.save()
    send_mail(
    "Request Accepted",  # Subject
    "Your request has been accepted. Thank you for choosing us.",
    settings.EMAIL_HOST_USER,
    [data.psychologist_email],
    )
    return render(request,'Administrator/PsychologistList.html',{"msg":"Verified"})
def reject(request,id):
    data=tbl_psychologist.objects.get(id=id)
    email=data.psychologist_email
    data.psychologist_status=2
    data.save()
    send_mail(
            " Your request has been rejected. Try again next time.",
            settings.EMAIL_HOST_USER,
            [data.psychologist_email],
    )
    return render(request,'Administrator/PsychologistList.html',{"msg":"rejected"})


def QuestionLevel(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        LevelData=tbl_questionlevel.objects.all()
        if request.method == 'POST':
            QuestionLevel=request.POST.get('txt_questionlevelname')
            #insert qry -->
            tbl_questionlevel.objects.create(questionlevel_name=QuestionLevel)
            return render(request,'Administrator/Level.html',{'msg':"Inserted Sucessfully"})
        else:
            return render(request,'Administrator/Level.html',{'Level':LevelData})
            
def EditQuestionLevel(request,eid):
    editdata = tbl_questionlevel.objects.get(id=eid)
    if request.method =="POST":
        questionlevel_name=request.POST.get('txt_questionlevelname')
        editdata.questionlevel_name=questionlevel_name
        editdata.save()
        return render(request,'Administrator/Level.html',{'msg':"Updated Successfully"})
    else:
        return render(request,'Administrator/Level.html',{'editdata':editdata})
    
def DeleteQuestionLevel(request,qid):
    tbl_questionlevel.objects.get(id=qid).delete()
    return render(request,'Administrator/Level.html',{'msg':"Deleted Successfully"})    

def Question(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        QuestionData=tbl_question.objects.all()
        QuestionLevel=tbl_questionlevel.objects.all()
        if request.method == 'POST':
            QuestionTitle=request.POST.get('txt_questiontitle')
            QuestionDescription=request.POST.get('txt_questiondescription')
            questionlevel=tbl_questionlevel.objects.get(id=request.POST.get('sel_level'))
            #insert qry -->
            tbl_question.objects.create(question_title=QuestionTitle,
                                        question_description=QuestionDescription,
                                        questionlevel=questionlevel )
            return render(request,'Administrator/Question.html',{'msg':"Inserted Sucessfully"})
        else:
            return render(request,'Administrator/Question.html',{'QuestionData':QuestionData,'Level':QuestionLevel})
        
def EditQuestion(request,eid):
    editdata = tbl_question.objects.get(id=eid)
    QuestionLevel=tbl_questionlevel.objects.all()

    if request.method =="POST":
        Title=request.POST.get('txt_questiontitle')
        Description=request.POST.get('txt_questiondescription')
        questionlevel=tbl_questionlevel.objects.get(id=request.POST.get('sel_level'))

        editdata.question_title=Title
        editdata.question_description=Description
        editdata.questionlevel=questionlevel
        editdata.save()
        return render(request,'Administrator/Question.html',{'msg':"Updated Successfully"})
    else:
        return render(request,'Administrator/Question.html',{'editdata':editdata,'Level':QuestionLevel})
        
    
def DeleteQuestion(request,qid):
    tbl_question.objects.get(id=qid).delete()
    return render(request,'Administrator/Question.html',{'msg':"Deleted Successfully"})    

def Option(request,qid):
    Question=tbl_question.objects.get(id=qid)
    OptionData=tbl_option.objects.filter(question=qid)
    if request.method == 'POST':
        Option=request.POST.get('txt_optioncontent')
        StressWeight=int(request.POST.get('wgt'))
        #insert qry -->
        tbl_option.objects.create(option_content=Option,stress_weight=StressWeight,question=Question)
        return render(request,'Administrator/Option.html',{'msg':"Inserted Sucessfully",'qid':qid})
    else:
        return render(request,'Administrator/Option.html',{'Option':OptionData,'qid':qid})
    
def DeleteOption(request,did,qid):
    tbl_option.objects.get(id=did).delete()
    return render(request,'Administrator/Option.html',{'msg':"Deleted Successfully",'qid':qid})
def Remedy(request):
    if "aid" not in request.session:
        return redirect("Guest:Login")
    else:
        rdata=tbl_remedies.objects.all()
        if request.method=="POST":
            title=request.POST.get('txt_title')
            description=request.POST.get('txt_description')
            level=request.POST.get('txt_level')
            tbl_remedies.objects.create(remedies_title=title,remedies_description=description,remedies_stresslevel=level)
            return render(request,'Administrator/Remedy.html',{'msg':"Inserted Sucessfully",'rdata':rdata})
        else:
            return render(request,'Administrator/Remedy.html',{'rdata':rdata})

    