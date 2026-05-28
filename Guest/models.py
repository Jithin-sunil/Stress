from django.db import models
from Administrator.models import *
# Create your models here.
class tbl_newuser(models.Model):
    user_name=models.CharField(max_length=60)
    user_gender=models.CharField(max_length=60)
    user_dob=models.DateField()
    user_contact=models.CharField(max_length=60)
    user_email=models.CharField(max_length=60)
    user_password=models.CharField(max_length=60)
    user_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_address=models.CharField(max_length=60)
    user_proof=models.FileField(upload_to='Assets/UserDocs/')
    user_photo=models.FileField(upload_to='Assets/UserDocs/')
class tbl_psychologist(models.Model):
    psychologist_name=models.CharField(max_length=60)
    psychologist_email=models.CharField(max_length=60)
    psychologist_contact=models.CharField(max_length=60)
    psychologist_address=models.CharField(max_length=60)
    psychologist_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    psychologist_photo=models.FileField(upload_to='Assets/UserDocs/')
    psychologist_proof=models.FileField(upload_to='Assets/UserDocs/')
    psychologist_password=models.CharField(max_length=60)
    psychologist_status=models.IntegerField(default=0)