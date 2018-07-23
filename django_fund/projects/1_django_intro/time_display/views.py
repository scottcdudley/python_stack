from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

# Create your vies here.
def index(request):
	context = {
		'date': strftime("%b %d, %Y", localtime()),
		'time': strftime("%H:%M:%S %p", localtime())
	}
	return render(request, 'time_display/index.html', context)
