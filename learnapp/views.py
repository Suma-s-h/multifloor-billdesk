from django.shortcuts import render,redirect
from learnapp.forms import userForm,userprofileForm,userupdateForm,userprofileupdateForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from textiles.models import TotalFloors,supervisor

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        form = userForm(request.POST)
        form1 = userprofileForm(request.POST,request.FILES)

        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
    else:           
        form = userForm()
        form1 = userprofileForm()
    context = {
        'form':form,
        'form1':form1,
        'registered' : registered
    }
    return render(request,"registered.html",context)



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return(redirect('home'))
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("please check your code.....!!!!!")
    
    return render(request,"login.html",{})

@login_required(login_url='login')
def home(request):
    floors=TotalFloors.objects.all()
    employee=supervisor.objects.filter(user_name=request.user)
    return render(request,"home.html",{'floors':floors,'employee':employee})

@login_required(login_url='login')
def userprofile(request):
    return render(request,"myprofile.html")

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def update(request):
    if request.method=='POST':
        form=userupdateForm(request.POST,instance=request.user)
        form1=userprofileupdateForm(request.POST,instance=request.user.userdetails)

        if form.is_valid() and form1.is_valid():
            user=form.save()

            profile=form1.save(commit=False)
            profile.user=user
            profile.save()
            return redirect("myprofile")
    else:
        form=userupdateForm(instance=request.user)
        form1=userprofileupdateForm(instance=request.user.userdetails)
    return render(request,"update.html",{'form':form, 'form1':form1})