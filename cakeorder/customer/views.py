from typing import Any,Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView
from django.utils.decorators import method_decorator
from store.models import Product
from django.contrib import messages
from customer.models import Cart,Order
from django.db.models import Sum



# Create your views here.


def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
           return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Please Login First!!!")
            return redirect('log')
    return inner



@method_decorator(signin_required,name="dispatch")    
class CustHomeView(ListView):
    
    template_name="custhome.html"
    model=Product
    context_object_name="data"
    
@method_decorator(signin_required,name="dispatch")     
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
    
@method_decorator(signin_required,name="dispatch")     
class AddCart(DetailView):
    
    def get(self,request,*args,**kwargs):
        prod=Product.objects.get(id=kwargs.get("id"))
        quantity=request.POST.get("qtyprice")
        
        
        user=request.user
        Cart.objects.create(product=prod,user=user,quantity=quantity,description=description)
        messages.success(request,"Product added to cart!!!")
        return redirect("ch")
    
    # def total_price(self):
    #     return self.total_quantity * product.price
    # qty=print(product)
@method_decorator(signin_required,name="dispatch")     
class Cartlistview(ListView):
    
    template_name="cartlist.html"
    model=Cart
    context_object_name="cartitem"
    
    
    def get_queryset(self):
        
        cart=Cart.objects.filter(user=self.request.user,status='cart')
        total=Cart.objects.filter(user=self.request.user,status='cart').aggregate(tot=Sum("product__price"))
        return {"items":cart,"total":total}
    
    
@signin_required
def deletecart(request,id):
    
    cart=Cart.objects.get(id=id)
    cart.delete()
    messages.error(request,"cart item removed!!!")
    return redirect("vcart")

@method_decorator(signin_required,name="dispatch")  
class Checkout(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"checkout.html")
    def post(self,request,*args,**kwargs):
        id=kwargs.get("cid")
        cart=Cart.objects.get(id=id)
        prod=cart.product
        user=request.user
        # quantity=Cart.quantity
        description=request.POST.get("description")
        print(description)
        address=request.POST.get("address")
        phone=request.POST.get("phone") 
        Order.objects.create(product=prod,user=user,address=address,phone=phone,description=description)
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
@method_decorator(signin_required,name="dispatch")  
class Search(View):
   
    def get(self,request,*args,**kwargs):
        search=request.GET.get("search")
        product=Product.objects.filter(name__icontains=search)
        cat=Product.objects.filter(category__icontains=search)
        
        context={"searchpro":product,"searchcat":cat}
        return render (request,'search.html',context)

@method_decorator(signin_required,name="dispatch")  
class OrderView(ListView):
   template_name='orders.html'
   model=Order
   context_object_name="order"
   def get_queryset(self):
       order=Order.objects.filter(user=self.request.user)
       return {'order':order}
   
@signin_required
def cancel_order(request,id):
    order=Order.objects.get(id=id)
    order.status="Cancel"
    order.save()
    messages.success(request,"Order Cancelled")
    return redirect('order')




