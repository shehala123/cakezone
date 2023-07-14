from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,DetailView,ListView,TemplateView
from django.urls import reverse_lazy
from .forms import RegForm,LogForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class LogView(View):
    def get(self,request):
        form=LogForm()
        return render(request,"log.html",{"f":form})
    def post(self,request):
        fdata=LogForm(data=request.POST)
        if fdata.is_valid():
            uname=fdata.cleaned_data.get("username")
            pswd=fdata.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Login Successfull !!")
                return redirect("ch")
            else:
                messages.error(request,"Login Failed !! Invalid username and password")
                return render(request,"log.html",{"f":fdata})
# class RegView(View):
#     def get(self,request):
#         form=RegForm()
#         return render(request,"reg.html",{"form":form})
#     def post(self,request,*args,**kwargs):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect("log")
#         else:
#             return render(request,"reg.html",{"form":form_data})

class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy("log")
  
class Logoutview(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("h")
   
class Home(TemplateView):
    template_name ="home.html"
    success_url=reverse_lazy("h")

class Gallery(TemplateView):
    template_name ="gallery.html"
    success_url=reverse_lazy("g")
   
class Contact(TemplateView):
    template_name ="contact.html"
    success_url=reverse_lazy("g")

class Aboutus(TemplateView):
    template_name ="aboutus.html"
    success_url=reverse_lazy("abt")
    
