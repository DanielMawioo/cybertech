from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mysite/index.html', {})


def aboutUs(request):
    return render(request, 'mysite/about.html', {})


def services(request):
    return render(request, 'mysite/services.html', {})


def portfolio(request):
    return render(request, 'mysite/portfolio.html', {})


def pricing(request):
    return render(request, 'mysite/pricing.html', {})


def contact(request):
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    return render(request, 'mysite/contact.html', {})

