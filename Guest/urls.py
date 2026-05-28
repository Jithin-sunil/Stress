from django.urls import path,include
from Guest import views
app_name='Guest'
urlpatterns = [

    path('NewUser/',views.NewUser,name="NewUser"),
    path('Ajaxplace/',views.Ajaxplace,name="Ajaxplace"),
    path('Login/',views.Login,name="Login"),
    path('PsychologistRegistration/',views.PsychologistRegistration,name="PsychologistRegistration"),
    path('Index/',views.Index,name="Index"),
    path("forgotpassword/",views.forgotpassword,name="forgotpassword"),
    path("otp/",views.otp,name="otp"),
    path("newpassword/",views.newpassword,name="newpassword")
]
