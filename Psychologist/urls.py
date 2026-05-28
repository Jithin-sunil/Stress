from django.urls import path
from Psychologist import views

app_name="Psychologist"
urlpatterns = [
   path('logout/',views.logout,name='logout'),
   path('HomePage/',views.HomePage,name="HomePage"), 
   path('MyProfile/',views.MyProfile,name="MyProfile"),
   path('EditProfile/',views.EditProfile,name="EditProfile"),
   path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
   path('Complaint/',views.Complaint,name='Complaint'),
   path('delcomplaint/<int:did>/',views.delcomplaint,name="delcomplaint"),
   path('AddSlot/',views.AddSlot,name="AddSlot"),
   path('deladdslot/<int:did>/',views.deladdslot,name="deladdslot"),
   path('ViewBooking/',views.ViewBooking,name="ViewBooking"),
   path('accept/<int:id>/',views.accept,name="accept"),
   path('reject/<int:id>/',views.reject,name="reject"),
   path('Fee/<int:fid>/',views.Fee,name="Fee"),
   path('Complete/<int:cid>/',views.Complete,name="Complete"),
]
