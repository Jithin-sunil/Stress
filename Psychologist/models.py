from django.db import models
from User.models import *
class tbl_slot(models.Model):
    slot_date=models.DateField()
    slot_fromtime=models.TimeField()
    slot_totime=models.TimeField()
    psychologist_id=models.ForeignKey(tbl_psychologist,on_delete=models.CASCADE)


    

