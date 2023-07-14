from typing import Any,Dict
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView
# from django.utils.decorators import method_decorator
from store.models import Product
from django.contrib import messages
from customer.models import Cart,Order
from django.db.models import Sum

# Create your views here.


# def signin_reqyired(fn):
#     def inner(request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return fn(request,*args,**kwargs)
#         else:
#             return red

# @method_decorator(login_required,name='dispatch')    
class CustHomeView(ListView):
    
    template_name="custhome.html"
    model=Product
    context_object_name="data"
    
class Productdetailview(DetailView):
    
    template_name="productdetails.html"
    model=Product
    context_object_name="product"
    pk_url_kwarg="pid"
    def post(self,request,*args,**kwargs):
        prod=Product.objects.get(id=kwargs.get("pid"))
        quantity=request.POST.get("quantity")
        
        user=request.user
        Cart.objects.create(product=prod,user=user,quantity=quantity)
        messages.success(request,"Product added to cart!!!")
        return redirect("ch")
    
class AddCart(DetailView):
    
    def get(self,request,*args,**kwargs):
        prod=Product.objects.get(id=kwargs.get("id"))
        quantity=request.POST.get("qtyprice")
        
        user=request.user
        Cart.objects.create(product=prod,user=user,quantity=quantity)
        messages.success(request,"Product added to cart!!!")
        return redirect("ch")
    
    # def total_price(self):
    #     return self.total_quantity * product.price
    # qty=print(product)
    
class Cartlistview(ListView):
    
    template_name="cartlist.html"
    model=Cart
    context_object_name="cartitem"
    
    def get_queryset(self):
        
        cart=Cart.objects.filter(user=self.request.user,status='cart')
        total=Cart.objects.filter(user=self.request.user,status='cart').aggregate(tot=Sum("product__price"))
        return {"items":cart,"total":total}
    
    

def deletecart(request,id):
    
    cart=Cart.objects.get(id=id)
    cart.delete()
    messages.error(request,"cart item removed!!!")
    return redirect("vcart")

class Checkout(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"checkout.html")
    def post(self,request,*args,**kwargs):
        id=kwargs.get("cid")
        cart=Cart.objects.get(id=id)
        prod=cart.product
        user=request.user
        # weight=request.POST.get("weight")
        # description=request.POST.get("description")
        address=request.POST.get("address")
        phone=request.POST.get("phone") 
        Order.objects.create(product=prod,user=user,address=address,phone=phone)
        cart.status="order placed"
        cart.save()
        messages.success(request,"order placed successfully!!!")
        return redirect("ch")
    
    
# def search(request):
#     q=request.POST.get("q")
#     data=Product.objects.filter(name_icontains=q).order_by("id")
#     return render(request,"search.html",{"data":data})
# class Search(ListView):
#     model = Product
#     template_name = 'search.html'
#     queryset = Product.objects.filter(name__icontains=' Choco Flake')

class Search(View):
   
    def get(self,request,*args,**kwargs):
        search=request.GET.get("search")
        product=Product.objects.filter(name__icontains=search)
        cat=Product.objects.filter(category__icontains=search)
        
        context={"searchpro":product,"searchcat":cat}
        return render (request,'search.html',context)
        