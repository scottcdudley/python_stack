from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    
    
    return render(request, "first_app/index.html")

def submit(request):
    print(request.POST)
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['dojo_location']
    request.session['fav_lang'] = request.POST['fav_lang']
    request.session['comment'] = request.POST['comment']
    print("user submitted information")
    return redirect('/result')

def result(request):
    request.session['count']+=1
    context = {
        'name': request.session['name'],
        'location' : request.session['location'],
        'lang' : request.session['fav_lang'],
        'comment' : request.session['comment'],
        'count' : request.session['count']
    }

    print("user is at results")
    return render(request,'first_app/results.html', context)
