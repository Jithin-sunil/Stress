from django.db import models
from User.models import *
from Guest.models import *
from Psychologist.models import *
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=60)
    complaint_content=models.CharField(max_length=60)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=60,null=True)
    userid=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE,null=True)
    psychologistid=models.ForeignKey(tbl_psychologist,on_delete=models.CASCADE,null=True)
class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=60)
    feedback_date=models.DateField(auto_now_add=True)
    userid=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
class tbl_booking(models.Model):
    booking_status=models.IntegerField(default=0)
    booking_description=models.CharField(max_length=60)
    booking_date=models.DateField(auto_now_add=True)
    booking_amount=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE,null=True)
    slot_id=models.ForeignKey(tbl_slot,on_delete=models.CASCADE,null=True)

class tbl_stressresult(models.Model):
    user = models.ForeignKey(tbl_newuser, on_delete=models.CASCADE)
    total_score = models.IntegerField()
    stress_level = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)


class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    psychologist=models.ForeignKey(tbl_psychologist,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)