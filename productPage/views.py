from django.shortcuts import render


# Create your views here.
def product_page(request):
    return render(request, 'product_main_page.html')
