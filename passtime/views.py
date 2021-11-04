from re import L
from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.
def home(request):
    return render(request, "passtimes/home.html")

def password(request):
    the_password= ""
    chars= "abcdefghijklmnopqrstuvwxyz"
    nums= "1234567890"
    spec= "!\"£$%^&*()_-+=:;@'#~[{]}/?.><,\\|"
    length=int(request.GET.get("length",12))
    nuB = request.GET.get("nums")
    up = request.GET.get("uppercase")
    speB= request.GET.get("special")
    
    if up:
        chars+=chars.upper()
    if nuB:
        chars+=nums
    if speB:
        chars+=spec
    for i in range(length):
        the_password+=choice(list(chars))
    return render(request, "passtimes/password.html",{"password":the_password})
def about(request):
    return render(request, "passtimes/about.html")
    