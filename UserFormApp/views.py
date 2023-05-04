from django.shortcuts import render
from .models import UserDetail, country
from datetime import datetime
from django.http import JsonResponse
from utils.regex import email_regex, name_regex
from utils.comman_function import getResponse, get_exception_Responses, validation_inputs
import re


def index(request):
    try:
        userobj = UserDetail.objects.all()
        
        countries = country.objects.all()

        return render(request, "home.html", {"user_data": userobj,"country":countries})

    except Exception as e:
        print(e)
        return render(request, "home.html")


def registration_form_page(request):
    try:
        countries = country.objects.all()
       
        return render(request, "user.html",{"country":countries})

    except Exception as e:
        print(e)
        return render(request, "user.html")


def create_form(request):
    try:
        if request.method == "POST":
            FisrtName = request.POST.get("FisrtName")
            lastName = request.POST.get("lastName")
            cmp = request.POST.get("cmp")
            Suffix = request.POST.get("Suffix")
            country = request.POST.get("country")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            if validation_inputs(email, email_regex) == False:
                response = getResponse(False, "Please Enter Valid Email Address")
                return JsonResponse(response)
            elif validation_inputs(FisrtName, name_regex) == False:
                response = getResponse(False, "Please Enter Valid First Name")
                return JsonResponse(response)
            elif validation_inputs(lastName, name_regex) == False:
                response = getResponse(False, "Please Enter Valid Last Name")
                return JsonResponse(response)
            elif validation_inputs(phone, '^\d{10}$') == False:
                response = getResponse(False, "Please Enter Valid mobile Name")
                return JsonResponse(response)
            dup_email = UserDetail.objects.filter(email=email)
            dup_mobile_no = UserDetail.objects.filter(phone_number=phone)
            if dup_email.first() :
                response = getResponse(False, "Email Address Already Exists")
                return JsonResponse(response)
            if dup_mobile_no.first() :
                response = getResponse(False, "Mobile No Already Exists")
                return JsonResponse(response)
            add_industry_objet = UserDetail(
                email=email,
                phone_number=phone,
                first_name=FisrtName,
                last_name=lastName,
                is_active=1,
                is_delete=0,
                joining_date=datetime.now(),
                
                country=country,
                suffix=Suffix,
                user_company_name=cmp,
            )

        add_industry_objet.save()

        return JsonResponse({"status": True, "Response": "User Added Successfully"})

    except Exception as e:
        print(e)
        return render(request, "home.html")


def update_user(request):
    get_datas = UserDetail.objects.filter(id=request.GET.get("id"))
    countries = country.objects.all()
    data = {
        "email": get_datas.first().email,
        "contact_no": get_datas.first().phone_number,
        "first_name": get_datas.first().first_name,
        "last_name": get_datas.first().last_name,
        "Suffix": get_datas.first().suffix,
        "CompanyName": get_datas.first().user_company_name,
        "country": get_datas.first().country
    }

    return render(request, "update_user.html", {"user_data": data,"country":countries})


def update_user_data(request):
    try:
        id = request.POST.get("id")
        FisrtName = request.POST.get("FisrtName")
        lastName = request.POST.get("lastName")
        cmp = request.POST.get("cmp")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        country = request.POST.get("country")
        Suffix = request.POST.get("Suffix")
        dup_email = UserDetail.objects.filter(email=email)
        dup_mobile_no = UserDetail.objects.filter(phone_number=phone)
        updaed_data = UserDetail.objects.filter(id=id)
        if validation_inputs(email, email_regex) == False:
            response = getResponse(False, "Please Enter Valid Email Address")
            return JsonResponse(response)
        elif validation_inputs(FisrtName, name_regex) == False:
            response = getResponse(False, "Please Enter Valid First Name")
            return JsonResponse(response)
        elif validation_inputs(lastName, name_regex) == False:
            response = getResponse(False, "Please Enter Valid Last Name")
            return JsonResponse(response)
        elif validation_inputs(phone, '^\d{10}$') == False:
            response = getResponse(False, "Please Enter Valid Mobile Name")
            return JsonResponse(response)
        if dup_email.first() and updaed_data.first().email != email:
            response = getResponse(False, "Email Address Already Exists")
            return JsonResponse(response)
        if dup_mobile_no.first() and updaed_data.first().phone_number != phone:
            response = getResponse(False, "Mobile No Already Exists")
            return JsonResponse(response)
        # roleid=UserRole.objects.filter(role_type=accountType).first().role_id
        # countryid=CountryMaster.objects.filter(country_name=country).first().country_id
        updaed_data.update(
            email=email,
            phone_number=phone,
            first_name=FisrtName,
            last_name=lastName,
            joining_date=datetime.now(),
            updated_on=datetime.now(),
            country=country,
            suffix=Suffix,
            user_company_name=cmp,
        )

        response = getResponse(True, "Data Updated Successfully")
        return JsonResponse(response)
    except Exception as _err:
        response = get_exception_Responses(False, str(_err.args))
        return JsonResponse(response)


def delete_user(request):
    try:
        id = request.POST.get("id")
        roleid = UserDetail.objects.filter(id=id)
        if roleid.first():
            roleid.update(is_active=0)

        response = getResponse(True, "Data Deleted Successfully")

        return JsonResponse(response)
    except Exception as _err:
        response = get_exception_Responses(False, str(_err.args))

        return JsonResponse(response)



def add_country(request):
   
        
        co=["India","Japan","Rusia","America"]
   
        for i in co:
            add_industry_objet = country(
                country_name=i,
                is_Active=1,
                
            )

            add_industry_objet.save()

        return JsonResponse({"status": True, "Response": "User Added Successfully"})