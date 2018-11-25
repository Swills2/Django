from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    location = ['San Jose', 'Mountain View', 'New York', 'Burbank']
    language = ['Python', 'Javascript', "PHP"]
    context = {
        'locations': location,
        'languages' : language,
    }
    print (context)
    return render(request, 'for/index.html', context)

def process(request):
    if request.method == 'POST':
        print (request.POST)
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect ('/result')
    else:
        return redirect('/')

def result(request):
    context = {
        'name' : request.session['name'],
        'location' : request.session['location'],
        'language' : request.session['language'],
        'comment' : request.session['comment'],
    }
    return render (request, 'for/result.html', context)
