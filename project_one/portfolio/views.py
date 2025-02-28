from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/index.html")
    
def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
        ]
    return render(request, "pages/dashboard.html", context={"data": data})

def reports(request):
    return render(request, "pages/reports.html")

def settings(request):
    return render(request, "pages/settings.html")

# portolio html
def about(request):
    return render(request, "pages/portfolio.html")

def skills(request):
    return render(request, "pages/skills.html")

def services(request):
    return render(request, "pages/services.html")

def contact(request):
    return render(request, "pages/contact.html")