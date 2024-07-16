from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home_page.html')

def about(request):
    return render(request, 'pages/about_page.html')