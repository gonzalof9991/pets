from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Category, Rescued


# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    rescueds = Rescued.objects.all()
    context = {"products": products,
               "categories": categories,
               "rescueds": rescueds
               }
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


def cat(request):
    return render(request, "cats.html")


def dog(request):
    return render(request, "dogs.html")
