
from django.urls import path,include
from User import views 
app_name='User'
urlpatterns = [
    path('logout/',views.logout,name='logout'),
    path('HomePage/',views.HomePage,name='HomePage'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('Complaint/',views.Complaint,name='Complaint'),
    path('delcomplaint/<int:did>/',views.delcomplaint,name="delcomplaint"),
    path('Feedback',views.Feedback,name="Feedback"),
    path('delfeedback/<int:did>/',views.delfeedback,name="delfeedback"),
    path('ViewPsychologist/',views.ViewPsychologist,name="ViewPsychologist"),
    path('ViewSlot/<int:pid>/',views.ViewSlot,name="ViewSlot"),
    path('Ajaxdate/',views.Ajaxdate,name="Ajaxdate"),
    path('MyBooking/',views.MyBooking,name="MyBooking"),
    path('Payment/<int:pid>/',views.Payment,name="Payment"),
    path('Ajaxpsychologist/',views.Ajaxpsychologist,name="Ajaxpsychologist"),
    path('choosetest/',views.choosetest,name="choosetest"),
    path('ViewQuestion/<int:lvl>/',views.ViewQuestion,name="ViewQuestion"), 
    path('ViewStressResult/',views.viewstressresult, name="ViewStressResult"),
    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path("breathex/",views.breathex,name="breathex"),


    

]
