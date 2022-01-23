from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from .models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

def loginUser(request):

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        print(request.POST.get('password'))

        try:
            user = User.objects.get(email=email)
            print(user.id)
        except:
            print ('User does not exist')

        user = authenticate(username=email, password=password)
        #print(user.id)

        if user is not None:
            login(request, user)
            token = Token.objects.get_or_create(user=user)
            print(token[0])
            return JsonResponse({'status': "user logged in", 'token':str(token[0])})
        else:
            messages.error(request, 'Username OR password does not exit')

    return JsonResponse({'status': "oops this user does not exist"})

"""
def logoutUser(request):
    logout(request)
    return redirect('home')
"""

def registerUser(request):
    print(request)
    if request.method == 'POST':
        u = User.objects.create(username=request.POST.get('username'), email=request.POST.get('email').lower())
        print(request.POST.get('password'))
        u.set_password(request.POST.get('password'))
        u.save()
        token = Token.objects.create(user=u)

        return JsonResponse({'status': "user added", 'token':str(token[0])})

    return {'status':'Only post requests accepted'}

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def testPermission(request):
    return JsonResponse({'status': "you should be logged in for this"})