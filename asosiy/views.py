from django.shortcuts import render
from django.views import View
from .models import *

class Index2View(View):
    def get(self, request):
        data = {
            "bolimlar": Bolim.objects.all()[:5]
        }
        return render(request, "page-index-2.html", data)

class IndexView(View):
    def get(self, request):
        data = {"bolimlar": Bolim.objects.all()}
        return render(request, "page-index.html", data)

class IchkiView(View):
    def get(self, request, pk):
        b = Bolim.objects.get(id=pk)
        data = {
            "ichki": Ichki.objects.filter(bolim=b)
        }
        return render(request, "ichki.html", data)

class MahsulotlarView(View):
    def get(self,request, pk):
        i = Ichki.objects.get(id=pk)
        data = {"mahsulotlar": Mahsulot.objects.filter(ichki=i)[:5]}
        return render(request, "page-listing-grid.html", data)

class BolimlarView(View):
    def get(self, request):
        data = {"h_bolimlar": Bolim.objects.all()}
        return render(request, "page-category.html", data)

class MahsulotView(View):
    def get(self, request, pk):
        data = {"mahsulot":Mahsulot.objects.get(id=pk)}
        return render(request, "page-detail-product.html", data)

class TanlanganView(View):
    def get(self, request):
        return render(request, "page-profile-wishlist.html")

class SavatView(View):
    def get(self, request):
        return render(request, "page-shopping-cart.html")

class BuyurtmaView(View):
    def get(self, request):
        return render(request, "page-profile-orders.html")
