from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Category


# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {"products": products,
               "categories": categories}
    return render(request, "index.html", context)


def detail(request, product_id):
    print(product_id)
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, "detail.html", context)


def contact(request):
    return render(request, "contact.html")


def login(request):
    return render(request, "login.html")
