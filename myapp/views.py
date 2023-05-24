
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 時間函數
from datetime import datetime

import random

def students(request):
	std1 = {"name":"小明", "sid":"01", "age":12}
	std2 = {"name":"小美", "sid":"02", "age":13}
	std3 = {"name":"大明", "sid":"03", "age":14}
	stds = [std1, std2, std3]
	return render(request,'myapp/std.html',locals())

def hello(request):
	# return HttpResponse("Hello World")
	return render(request, 'myapp/hello.html')

def hello1(request, username):
	now = datetime.now()
	#                                     傳遞的資料
	return render(request, 'myapp/hello1.html', locals())


times = 0

def hello2(request, username):
	global times
	times = times + 1
	local_times = times

	now = datetime.now()

	score = random.randint(1,100)

	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	dice3 = random.randint(1,6)
	dict1 = {"random1": dice1, "random2": dice2, "random3": dice3}

	#                                     傳遞的資料
	return render(request, 'myapp/hello2.html', locals())
