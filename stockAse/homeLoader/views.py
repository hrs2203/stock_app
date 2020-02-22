from django.shortcuts import render
from django.contrib import messages
import random
import requests
from django.http import HttpResponse, HttpResponseForbidden
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout

from .models import CustomUser, Company, Shares
from .forms import CustomUserCreationForm, CompanyRegistrationForm

# Create your views here.


def welcomePage(request):
    return render(
        request=request,
        template_name='homepage.html',
        context={}
    )


def companyPage(request):
    return render(
        request=request,
        template_name='company.html',
        context={}
    )


def newCompany(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()

            return redirect('user')

    form = CompanyRegistrationForm()
    return render(request, 'registration/company.html', {"form": form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('account/login')
    form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {"form": form})


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully!")
    return redirect('/account/login')


def userPage(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(email=request.user.email)
        return render(
            request=request,
            template_name='userDetail.html',
            context={
                "email_id": str(user),
            }
        )
    return HttpResponseForbidden('<h1>Access Denied</h1>')


def send_testGraphData(request):
	url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo"

	temp = requests.get(url).json()
	# print(temp.get("Meta Data"))
	stockData = temp.get("Time Series (5min)")
	# print(stockData)
	countLim = 10
	xData = list(stockData.keys())
	
	xTime = []
	for i in xData:
		xTime.append(i.split()[1])

	# print(xData[:countLim])
	yData = []
	y2Data = []
	y3Data = []
	
	for i in xData:
		yData.append(float(stockData.get(i).get("1. open")))
		y2Data.append(float(stockData.get(i).get("2. high")))
		y3Data.append(float(stockData.get(i).get("3. low")))
			
	print(yData[:10])

	# l = random.randint(1,30)
	# x = []
	# y = []
	# for i in range(l):
	# 	x.append(random.randint(1,5))
	# 	y.append(x[-1]**2)

	return JsonResponse({
		"x_axis" : xTime[:10],
		"y_axis" : yData[:10],
		"y2_axis": y2Data[:10],
		"y3_axis": y3Data[:10],
	})
