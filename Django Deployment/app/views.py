import numpy as np
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from . forms import CreateUserForm
from django.contrib import messages
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import joblib
from . import forms
from .models import UserImageModel
from . import forms
from .models import UserImageModel


model = joblib.load('F:/Modified UI/crop prediction modification/Deploy/app/dt.pkl')



def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR Password incorrect')
    context = {}
    return render(request,'registration/login.html', context)

def predict_crop(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features)]
        print(final_features)
        prediction = model.predict(final_features)
        print(prediction)
        output = prediction[0]
        if output== 0:
            output='APPLE'
        elif output== 1:
            output='BANANA'
        elif output== 2:
            output='BLACK GRAM'
        elif output== 3:
            output='CHICKPEA'
        elif output== 4:
            output='COCONUT'
        elif output== 5:
            output='COFFEE'
        elif output== 6:
            output='COTTON'
        elif output== 7:
            output='GRAPES'
        elif output== 8:
            output='JUTE'
        elif output== 9:
            output='KIDNEY BEANS'
        elif output== 10:
            output='LENTIL'
        elif output== 11:
            output='MAIZE'
        elif output== 12:
            output='MANGO'
        elif output==13:
            output='MOTH BEANS'
        elif output== 14:
            output='MUNG BEAN'
        elif output== 15:
            output='MUSK MELON'
        elif output== 16:
            output='ORANGE'
        elif output== 17:
            output='PAPAYA'
        elif output== 18:
            output='PIGEON PEAS'
        elif output== 19:
            output='POMEGRANATE'
        elif output== 20:
            output="RICE"
        else:
            output="WATER MELON"
        return render(request, 'crop_prediction.html', {'prediction_text': output})
    else:
        return render(request, 'crop_prediction.html')

def logoutusers(request):
    logout(request)
    return redirect('login')

def index(request):
    context = {}
    return render(request, 'index.html', context)

def landingpage(request):
    context = {}
    return render(request, 'landingpage.html', context)
