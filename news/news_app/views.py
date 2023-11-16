from django.shortcuts import render, redirect
from .forms import LoginForm, Registrationform



#royhatan otkazish va  profildan chiqib ketish
from django.contrib.auth import logout,  login, authenticate
from .models import User, UserProfile, New



# Create your views here.

def main_page(request):
    news =New.objects.all()
    return render(request,'index.html', context={'news':news})




def login_views(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
                                                            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(user)
                return redirect('/')
             
            
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', context={'form': form}) 




# registratsiya funksiyasi
def register_view(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None:
                UserProfile.objects.create(user=user)

                return redirect('login/')
        
            else:
                print('SOMETHIN WENT  WRONG')

    else:
        form = Registrationform()

    return render(request, 'registration/register.html', context={'form':form})
