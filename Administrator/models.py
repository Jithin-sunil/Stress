from django.db import models
from Administrator.models import *
# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=60)
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=60)
    admin_email=models.CharField(max_length=60)
    admin_contact=models.CharField(max_length=60)
    admin_password=models.CharField(max_length=60)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=60)   
class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=60)
class tbl_type(models.Model):
    type_name=models.CharField(max_length=60)
class tbl_place(models.Model):
    place_name=models.CharField(max_length=60)
    place_pincode=models.CharField(max_length=60)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=60)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_questionlevel(models.Model):
    questionlevel_name=models.CharField(max_length=50)

class tbl_question(models.Model):
    question_title=models.CharField(max_length=50)
    question_description=models.CharField(max_length=50)
    questionlevel=models.ForeignKey(tbl_questionlevel,on_delete=models.CASCADE)
                   
class tbl_option(models.Model):
    option_content=models.CharField(max_length=50)
    question=models.ForeignKey(tbl_question,on_delete=models.CASCADE)
    stress_weight = models.IntegerField(null=True)

class tbl_product(models.Model):
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=60)
    product_price=models.IntegerField(default=0)
    product_image=models.FileField(upload_to='Assets/UserDocs/')

class tbl_remedies(models.Model):
     remedies_title=models.CharField(max_length=50)
     remedies_description=models.CharField(max_length=50)
     remedies_stresslevel=models.CharField(max_length=50)