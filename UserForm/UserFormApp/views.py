from django.shortcuts import render
from .models import UserDetails


def index(request):
    try:
        userobj = UserDetails.objects.all()
        return render(request, 'home.html', {'user_data': userobj})
    
    except Exception as e:
        print(e)
        return render(request, 'home.html')