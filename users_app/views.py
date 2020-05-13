from django.shortcuts import render, redirect
from .models import Users

def index(request):
    print(Users.objects.all())
    context = {
        "all_the_Users": Users.objects.all(),
        "user1": Users.objects.get(id=1),
        "user2": Users.objects.get(id=4),
        "user3": Users.objects.get(id=3),
        "user5": Users.objects.get(id=5)
    }
    return render(request,'index.html', context)

def process(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email_address = request.POST["email_address"]
    age = request.POST["age"]
    Users.objects.create(
        first_name=first_name,
        last_name=last_name,
        email_address=email_address,
        age=age)
    return redirect('/')
# Create your views here.