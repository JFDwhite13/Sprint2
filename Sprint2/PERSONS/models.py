from pyclbr import Class
from re import T
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.
class persons(models.Model):
    pid=models.BigIntegerField(primary_key=True, unique=True)
    pfirstname= models.CharField(max_length=60)
    plastname= models.CharField(max_length=60)
    pemail=models.CharField(max_length=90)
    ppassword=models.CharField(max_length=20)

class patients(models.Model):
    patientid = models.BigIntegerField(primary_key=True, unique=True)
    patientfirstname = models.CharField(max_length=60)
    patientlastname = models.CharField(max_length=60)
    patientphonenumber = models.BigIntegerField(default=0)
    patientgender= models.CharField(max_length=20)
    patientaddress = models.CharField(max_length=200)
    patientcity = models.CharField(max_length=200)
    patientBirthday = models.CharField(max_length=50)
    patientLatitude = models.CharField(max_length=200, null=True)
    patientLongitude = models.CharField(max_length=200, null=True)

class doctorandnurse(models.Model):
    dnid = models.BigIntegerField(primary_key=True,unique=True)
    dFirstname = models.CharField(max_length=60)
    dLastname = models.CharField(max_length=60)
    dPhoneNumber= models.BigIntegerField(default=0)
    dgender=models.CharField(max_length=60)
    dspecialty = models.CharField(max_length=60)
    dresgister=models.CharField(max_length=60)
    isdoctor= models.BooleanField(default=False)


class helper(models.Model):
    hid = models.BigIntegerField(primary_key=True,unique=True)
    hfirstname = models.CharField(max_length=60)
    hlastname = models.CharField(max_length=60)
    hphoneNumber = models.BigIntegerField(default=0)
    hgender= models.CharField(max_length=60)
    hidpatient = models.ForeignKey(patients, related_name='helperpatientid', on_delete=models.DO_NOTHING)
    hkinship = models.CharField(max_length=60)
    hemail = models.CharField(max_length=80)

class asigned(models.Model):
    adoctor= models.ForeignKey(doctorandnurse, related_name='asigneddnid', on_delete=models.DO_NOTHING)
    apatient = models.ForeignKey(patients, related_name='asignedpatientid', on_delete=models.DO_NOTHING)

class vitalsigns(models.Model):
    vsidpatient	= models.ForeignKey(patients, related_name='vitalpatientid', on_delete=models.DO_NOTHING)
    vsdatetime = models.DateTimeField(default="0000-00-00")
    oximetry= models.CharField(max_length=60)
    respiratoryrate = models.CharField(max_length=60)
    heartrate = models.CharField(max_length=60)
    temperature = models.CharField(max_length=60)
    bloodpressure = models.CharField(max_length=60) 
    bloodglucose = models.CharField(max_length=60)

class suggest(models.Model):
    spatientid = models.ForeignKey(patients, related_name='suggestpatientid', on_delete=models.DO_NOTHING)
    sdoctor = models.ForeignKey(doctorandnurse, related_name='suggestdnid', on_delete=models.DO_NOTHING)
    nsuggest = models.AutoField(primary_key=True)
    datesuggest = models.DateTimeField(default="0000-00-00")
    suggest =  models.CharField(max_length=800)

class diagnosis(models.Model):
    diagpatientid = models.ForeignKey(patients, related_name='diagpatientid', on_delete=models.DO_NOTHING)
    diag =  models.CharField(max_length=800)