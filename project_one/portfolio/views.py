from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/index.html")

# portolio html
def about(request):
    return render(request, "pages/portfolio.html")

def skills(request):
    return render(request, "pages/skills.html")

def services(request):
    return render(request, "pages/services.html")

def contact(request):
    return render(request, "pages/contact.html")