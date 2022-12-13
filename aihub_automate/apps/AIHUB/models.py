#from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

# AccountType_choice = (
#     ('student','Student'),
#     ('admin', 'Admin'),
#     ('PI','PI')
# )

# class User(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     accountType = models.CharField(max_length=7, choices=AccountType_choice, default='student')

from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField 


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
            
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
               
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
AccountType_choice = (
    ('student','Student'),
    ('admin', 'Admin'),
    ('PI','PI'),
    ('client_admin','Client_Admin'),
    ('client_team','Client_Team')
)

class User(AbstractUser):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    accountType = models.CharField(max_length=25, choices=AccountType_choice, default='student')
    Contact = PhoneNumberField(default = None, blank=True, null=True)
    mailingAddress = models.CharField(max_length = 250, null = True, blank = True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def save(self, *args, **kwargs):
        if self.mailingAddress:
            pass
        else:
            self.mailingAddress = self.email

        return super(User, self).save()

class CompanyInformation(models.Model): 
    companyName = models.CharField(max_length = 50)
    contactName = models.CharField(max_length = 30)
    contactDesignation = models.CharField(max_length = 30, blank=True, null=True)
    address = models.CharField(max_length = 250, blank=True, null=True)
    Email= models.EmailField(_('email address'))
    phone = PhoneNumberField()
    incorporationYear = models.IntegerField()
    businessNumber = models.IntegerField()
    numberOfEmployees = models.IntegerField()
    coreOperations = models.CharField(max_length = 100)
    revenue =  models.FloatField()
    potentialProjects = models.TextField()
    status = models.CharField(max_length = 50, default="screening", blank = True, null = True)
    files = models.FileField(upload_to ='Files/', max_length = 250, null = True, blank = True)
    note = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.companyName

class ProjectTitle(models.Model):
    companyName = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE)
    projectTitle = models.CharField(max_length = 30,blank=True, null=True)
    projectDescription = models.TextField()
    noveltyProject = models.TextField(blank=True, null=True)
    question1 = models.TextField(blank=True, null=True)
    question2 = models.TextField(blank=True, null=True)
    status = models.CharField(max_length = 50,default = "prospect", blank = True)


    def __str__(self):
        return self.companyName

class CompanyCash(models.Model):
    project = models.ForeignKey(ProjectTitle, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)
    designation = models.CharField(max_length = 50)
    hours = models.IntegerField()

    def __str__(self):
        return self.project



class projectinfoPI(models.Model):
    projectTitle = models.CharField(max_length = 50)
    companyName = models.CharField(max_length = 50)
    projectDescription = models.TextField()
    projectobjectives = RichTextField(blank=True, null=True)
    modeofdelivery = models.CharField(max_length=100,blank=True, null=True)
    rf_initiation_risk = models.CharField(max_length=1000,blank=True, null=True)
    rf_initiation_mitigation = models.CharField(max_length=1000,blank=True, null=True)
    rf_implementation_risk = models.CharField(max_length=1000,blank=True, null=True)
    rf_implementation_mitigation = models.CharField(max_length=1000,blank=True, null=True)
    rf_execution_risk = models.CharField(max_length=1000,blank=True, null=True)
    rf_execution_mitigation = models.CharField(max_length=1000,blank=True, null=True)
    rf_commercialization_risk = models.CharField(max_length=1000,blank=True, null=True)
    rf_commercialization_mitigation = models.CharField(max_length=1000,blank=True, null=True)
    rf_sbe_risk = models.CharField(max_length=1000,blank=True, null=True)
    rf_sbe_mitigation = models.CharField(max_length=1000,blank=True, null=True)
    project = models.OneToOneField(
        ProjectTitle,
        on_delete=models.CASCADE,
        primary_key=True,
    )

   


class workPlan(models.Model):
    projectTitle = models.ForeignKey(projectinfoPI, on_delete=models.CASCADE)
    milestone = models.CharField(max_length = 100)
    description = models.TextField(blank=True, null=True)
    week = models.IntegerField(blank=True, null = True)

    

class teamexperts(models.Model):
    projectTitle = models.ForeignKey(projectinfoPI, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)








    
    





    









   
