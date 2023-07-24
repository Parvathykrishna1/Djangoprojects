from django.db.models import Q
from django.shortcuts import render

from shop.models import Product


# Create your views here.
def searchresult(request):
    query=""
    products=None
    if(request.method=="POST"):
        query=request.POST.get('q')
        if(query):
            products=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return render(request,'searchresult.html',{'query':query,'products':products})