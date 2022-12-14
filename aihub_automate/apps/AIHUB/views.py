
from multiprocessing import context
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from apps.AIHUB.models import User ,CompanyInformation, ProjectTitle, CompanyCash
from apps.AIHUB.models import *
from PyPDF2 import PdfReader, PdfWriter
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from io import BytesIO
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def home(request):
    return render(request=request, template_name="AIHUB/home.html")

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index',}

    html_template = loader.get_template('AIHUB/index.html')
    return HttpResponse(html_template.render(context, request))

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})


@login_required(login_url="/login/")
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('http://localhost:8000/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request=request, template_name="password/password_change.html", context={"form":form})

@login_required(login_url="/login/")
def profile(request):
    context = {
    "email": request.user.email,
    "firstname": request.user.first_name,
    "lastname":request.user.last_name,
    "contact":request.user.Contact,
    "mailingAddress":request.user.mailingAddress
    }
    html_template = loader.get_template('accounts/profile.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def editprofile(request):
    if request.method == 'GET':
        context = {
        "email": request.user.email,
        "firstname": request.user.first_name,
        "lastname":request.user.last_name,
        "contact":request.user.Contact,
        "mailingAddress":request.user.mailingAddress
        }
        
        html_template = loader.get_template('accounts/editprofile.html')
        return HttpResponse(html_template.render(context, request))
    if request.method == 'POST':
        user = User.objects.get(email=request.user.email)
        user.first_name =  request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.Contact = request.POST.get('contact')
        user.mailingAddress = request.POST.get('mailingAddress')
        #print(request.POST.get('contact'))
        user.save()
        return redirect ("/profile/")


def companyDetails(request,company_id=""):
    context = {'segment': 'companydetails'}
    if request.method == 'POST':
        if company_id:
            objcompanyinfo  = CompanyInformation.objects.get(id=company_id)
            form = CompanyInformationForm(request.POST, instance= objcompanyinfo)
            if form.is_valid():
                form.save()
                
                return render(request,"AIHUB/Inquiry-complete.html")
        else:
            form = CompanyInformationForm(request.POST)
        
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.save()
            email = request.POST.get("Email")
            subject = "Submittion Confirmation"
            email_template_name = "password/companydetails.txt"
            c = {
            "email":email,
            'domain':'127.0.0.1:8000',
            'site_name': 'Website',
            'uid':formdata.pk,
            'protocol': 'http',
            }
            emailbody = render_to_string(email_template_name, c)
            try:
                send_mail(subject, emailbody, settings.EMAIL_HOST_USER , [email,'1hamadaslam@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect ("/password_reset/done/")
            return render(request,"AIHUB/Inquiry-complete.html")
        else:
            print(form.errors)
            return redirect(request, 'AIHUB/companydetails.html', {'form': form, 'company_id':company_id})
            
    else:
        context = {'segment': 'companydetails'}
        
        if company_id:
            objcompanyinfo = CompanyInformation.objects.get(id=company_id)
            form = CompanyInformationForm(instance=objcompanyinfo)
            
        else:
            form = CompanyInformationForm()
            
        return render(request,'AIHUB/companydetails.html',{'form': form, 'company_id':company_id }) 


def projectDetails(request,company_id):
    context = {'segment': 'projectdetails'}
    if request.method == 'POST':
        form = ProjectInfoForm(request.POST)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.companyName = (CompanyInformation.objects.get(id=company_id))
            
            formdata.save()
            return redirect(f'/companycash/{formdata.pk}')
           # return redirect(f'/projectdetailsview/{company_id}')
        else:
            return redirect(request, 'AIHUB/projectdetails.html', {'form': form, 'para':company_id})
            
    else:
        context = {'segment': 'projectdetails'}
        form = ProjectInfoForm()
        context['form'] = form
        return render(request,'AIHUB/projectdetails.html',{'form': form, 'para':company_id}) 

@login_required(login_url="/login/")
def projects(request, company_id):
    companyName = CompanyInformation.objects.get(id=company_id).companyName
    projectdetails = ProjectTitle.objects.filter(companyName_id=company_id).values()
    return render(request,'AIHUB/projects.html',{"projectdetails":projectdetails, "companyName":companyName}) 

@login_required(login_url="/login/")
def projectinfo(request, projectid):
    projectdetails = ProjectTitle.objects.get(id=projectid)
    companycashdetail = CompanyCash.objects.filter(project_id=projectid).values()
    
    return render(request,'AIHUB/projectinfo.html',{"projectdetails":projectdetails,"companycashdetails":companycashdetail})

@login_required(login_url="/login/")
def projectdetailsview(request, company_id):
   
    projectdetails = ProjectTitle.objects.filter(companyName_id=company_id).values()
    # for x in projectdetails:
    return render(request,'AIHUB/projectdetailsview.html',{"projectdetails":projectdetails}) 


def companycash(request,project_id):
    companycashdetails = CompanyCash.objects.filter(project_id=project_id).values()
    companyid = ProjectTitle.objects.get(id=project_id).companyName_id
    if request.method == 'POST':
        form = CompanyCashForm(request.POST)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.project = (ProjectTitle.objects.get(id=project_id))
            formdata.save()
            return redirect (f'/companycash/{project_id}')
        else:
            return redirect(request, 'AIHUB/companycash.html', {'form': form, 'para':project_id})
            
    else:
        context = {'segment': 'projectdetails'}
        form = CompanyCashForm()
        context['form'] = form
        return render(request,'AIHUB/companycash.html',{'form': form, 'para':project_id, 'companycashdetails':companycashdetails, 'companyid':companyid}) 

def projectinfoform(request, projectid):
    projectdetails = ProjectTitle.objects.get(id=projectid)
    if request.method == 'POST':
        form = ProjectinfoPIform(request.POST)
        if form.is_valid():
             
            formdata = form.save(commit=False)
            formdata.project = projectdetails
            formdata.projectDescription = request.POST.get("projectDescription")
            formdata.save()
            return redirect(f'/workplan/{formdata.pk}')
            # return HttpResponse("data submitted successfully")
        else:
            print(form.errors)
            return redirect(request, 'AIHUB/projectinfoform.html', {'form': form})
            
    else:
        companyName = CompanyInformation.objects.get(id=projectdetails.companyName_id).companyName
        form = ProjectinfoPIform()
        try:
            projectinfopi = projectinfoPI.objects.get(project_id=projectid)
            form = ProjectinfoPIform(instance=projectinfopi)    
            return render(request,'AIHUB/projectinfoform.html',{'projectdetails': projectdetails,'projectinfopi':projectinfopi, 'companyName':companyName, 'form':form, 'para':projectid }) 
        
        except ObjectDoesNotExist:
        
            return render(request,'AIHUB/projectinfoform.html',{'projectdetails': projectdetails,'companyName':companyName, 'form':form, 'para':projectid }) 

def projectinfoeditform(request, projectid):
    projectdetails = ProjectTitle.objects.get(id=projectid)
    companyName = CompanyInformation.objects.get(id=projectdetails.companyName_id).companyName
    projectinfopi = projectinfoPI.objects.get(project_id=projectid)
    form = ProjectinfoPIform(instance=projectinfopi)    
    return render(request,'AIHUB/projectinfoform.html',{'projectdetails': projectdetails,'projectinfopi':projectinfopi, 'companyName':companyName, 'form':form, 'para':projectid }) 


def workplan(request, projectiinfoform_id):
    workplandetails = workPlan.objects.filter(projectTitle_id=projectiinfoform_id).values()
    # companyid = ProjectTitle.objects.get(id=project_id).companyName_id
    if request.method == 'POST':
        form = workPlanForm(request.POST)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.projectTitle = (projectinfoPI.objects.get(project_id=projectiinfoform_id))
            formdata.save()
            return redirect (f'/workplan/{projectiinfoform_id}')
        else:
            print(form.errors)
            return redirect(request, 'AIHUB/workplan.html', {'form': form, 'para':projectiinfoform_id})
            
    else:
        context = {'segment': 'projectiinfoform'}
        form = workPlanForm()
        context['form'] = form
        return render(request,'AIHUB/workplan.html',{'form': form, 'para':projectiinfoform_id, 'workplandetails':workplandetails}) 

def teammembers(request, projectiinfoform_id):
    teamdetails = teamexperts.objects.filter(projectTitle_id=projectiinfoform_id).values()
    # projectinfoPI.objects.get(id = projectiinfoform_id).
    if request.method == 'POST':
        form = teamexpertsForm(request.POST)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.projectTitle = (projectinfoPI.objects.get(project_id=projectiinfoform_id))
            formdata.save()
            return redirect (f'/teammembers/{projectiinfoform_id}')
        else:
            print(form.errors)
            return redirect(request, 'AIHUB/teammembers.html', {'form': form, 'para':projectiinfoform_id})
            
    else:
        context = {'segment': 'projectiinfoform'}
        form = teamexpertsForm()
        context['form'] = form
        return render(request,'AIHUB/teammembers.html',{'form': form, 'para':projectiinfoform_id, 'teamdetails':teamdetails}) 


def projectinfopi(request, projectid):
    projectdetails = projectinfoPI.objects.get(project_id=projectid)
    workplandetail = workPlan.objects.filter(projectTitle_id=projectid).values()
    teamdetails = teamexperts.objects.filter(projectTitle_id=projectid).values()
    
    return render(request,'AIHUB/projectinfopi.html',{"projectdetails":projectdetails,"workplandetail":workplandetail,"teamdetails":teamdetails})

@login_required(login_url="/login/")
def companylist(request):
    objcompanylist = CompanyInformation.objects.filter(status="screening").values()
    return render(request,'AIHUB/companylist.html',{"companylist":objcompanylist}) 

@login_required(login_url="/login/")
def companylistscope(request):
    objcompanylist = CompanyInformation.objects.filter(status="Scoping").values()
    return render(request,'AIHUB/companylistScope.html',{"companylist":objcompanylist}) 

@login_required(login_url="/login/")
def addnotes(request, company_id):
    objcompany = CompanyInformation.objects.get(pk=company_id)
    objcompany.note = request.POST.get("notes")
    objcompany.save()
    if objcompany.status == "screening":
        return redirect("/companylist/")
    else:
        return redirect("/companylistscope/")

@login_required(login_url="/login/")
def sendforms(request, company_id):
    
    reader = PdfReader("Files/F183A_e.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    fields = reader.get_fields()

    writer.add_page(page)
    objcompanyinfo  = CompanyInformation.objects.get(id=company_id)

    writer.update_page_form_field_values(
        writer.pages[0], {
            "Name of organization": objcompanyinfo.companyName,
            "Name and title of contact person at the organization":  objcompanyinfo.contactName + " - " + objcompanyinfo.contactDesignation, 
            "Mailing address": objcompanyinfo.address,
            "Telephone number": objcompanyinfo.businessNumber,
            "Telephone number_2": objcompanyinfo.phone,
            "Email address": objcompanyinfo.Email,
            "Total number of employees in Canada": objcompanyinfo.numberOfEmployees,
            "Net profit loss for previous year If Applicable": objcompanyinfo.revenue

        }
    )

    # write "output" to PyPDF2-output.pdf
    with open("Files/" + objcompanyinfo.companyName + "-F183A_e.pdf", "wb") as output_stream:
        writer.write(output_stream)
    
    email_template_name = "password/Intake form.txt"
    c = {
            "email":objcompanyinfo.Email,
            'domain':'127.0.0.1:8000',
            'site_name': 'Website',
            'uid':company_id,
            'protocol': 'http',
            }
    emailbody = render_to_string(email_template_name, c)

    sendmail(settings.EMAIL_HOST_USER,  objcompanyinfo.Email, 'sample mail', emailbody, ["Files/" + objcompanyinfo.companyName + "-F183A_e.pdf","Files/117-RES15 ORSIE Internal Project Approval-filled.pdf"])
    messages.success(request, 'Documents sent successfully')
    return redirect("/companylistscope/")

def sendmail(send_from, send_to, subject, text, files=None,
              server=settings.EMAIL_HOST,username=settings.EMAIL_HOST_USER, password=settings.EMAIL_HOST_PASSWORD,
              use_tls=True):
    # assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    # send_mail(subject, msg.as_string(), settings.EMAIL_HOST_USER , [email,'taxil.savani@gmail.com'], fail_silently=False)
    smtp = smtplib.SMTP(server,'587')
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def changestatus(request, company_id):
    objcompany = CompanyInformation.objects.get(pk=company_id)
    objcompany.status = "Scoping"
    objcompany.save()
    return redirect ("/companylist/")

def changeprojectstatus(request, projectid, company_id):
    objproj = ProjectTitle.objects.get(pk=projectid)
    objproj.status = "Project"
    objproj.save()
    return redirect (f'/projects/{company_id}')

def sendapprovalforms(request, projectid):
    reader = PdfReader("Files/117-RES15 ORSIE Internal Project Approval.pdf")
    writer = PdfWriter()
    fields = reader.get_fields()
    projectdetails = ProjectTitle.objects.get(id=projectid)
    objcompanyinfo  = CompanyInformation.objects.get(id=projectdetails.companyName_id)
    objprojectinfo = projectinfoPI.objects.get(project_id=projectid)
    
    i = 0; 
    print(reader.resolved_objects[(0,258)].get_object)
    # print(len(reader.pages))
    for x in reader.pages:
        page = reader.pages[i]
        # print("x is", x)
        # answer = findInDict('/Kids',page.resolvedObjects).getData()
        
        writer.add_page(page)
        
        

        writer.update_page_form_field_values(
            writer.pages[i], {
                "Company Name": objcompanyinfo.companyName,
                "Contact Name":  objcompanyinfo.contactName + " - " + objcompanyinfo.contactDesignation, 
                "Mailing address": objcompanyinfo.address,
                "Telephone Number": objcompanyinfo.businessNumber,
                "Email": objcompanyinfo.Email,
                "Number of Full Time Employees": objcompanyinfo.numberOfEmployees,
                "Year of Incorporation":objcompanyinfo.incorporationYear,
                "Company Core Operations":objcompanyinfo.coreOperations,
                "Project Title":projectdetails.projectTitle,
                "Project description":projectdetails.projectDescription,
                "Other details": projectdetails.question1,
                "Novelty of Project":projectdetails.noveltyProject,
                'Economic Benefits':projectdetails.question2,

            }
        )
        
        try:
            objprojectinfo = projectinfoPI.objects.get(project_id=projectid)
            writer.update_page_form_field_values(
                writer.pages[i], {
                    "Project Objectives":objprojectinfo.projectobjectives,
                    "Results Delivery":objprojectinfo.modeofdelivery,
                    "Initiation-Risk":objprojectinfo.rf_initiation_risk,
                    "Initiation-Mitigation Strategy":objprojectinfo.rf_initiation_mitigation,
                    'Implementation-Risk': objprojectinfo.rf_implementation_risk, 
                    'Implementation-Mitigation Strategy': objprojectinfo.rf_implementation_mitigation, 
                    'Execution-Risk': objprojectinfo.rf_execution_risk, 
                    'Execution-Mitigation Strategy': objprojectinfo.rf_execution_mitigation, 
                    'Commercialization-Risk': objprojectinfo.rf_commercialization_risk, 
                    'Commercialization-Mitigation Strategy': objprojectinfo.rf_commercialization_mitigation, 
                    'Scientific-Mitigation Strategy': objprojectinfo.rf_sbe_mitigation, 
                    'Scientific-Risk': objprojectinfo.rf_sbe_risk,
                    
                }
            )
            
        except ObjectDoesNotExist:
            pass
        i = i +1
        # write "output" to PyPDF2-output.pdf
        with open("Files/117-RES15 ORSIE Internal Project Approval-filled.pdf", "wb") as output_stream:
            writer.write(output_stream)
    
 
    emailbody = "Please find attached approval document and sent it to AIHUB"
    sendmail(settings.EMAIL_HOST_USER,  objcompanyinfo.Email, 'sample mail', emailbody, ["Files/117-RES15 ORSIE Internal Project Approval-filled.pdf"])
    messages.success(request, 'Documents sent successfully')
    
    return redirect(f'/projects/{objcompanyinfo.pk}')





    
    