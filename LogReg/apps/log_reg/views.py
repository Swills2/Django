from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def home(request):
    return render(request,'home.html')

def reg(request):
    form = request.POST
    error = []
    exist_email = User.objects.filter(email=form['email'])
    if len(form['first_name'])<3:
        error.append("First name must have at least 3 characters.")
    if len(form['last_name'])<3:
        error.append("Last name must have at least 3 characters.")
    if len(form['password'])<8:
        error.append("Password must have at least 8 characters.")
    if not form['password'] == form['password_comfirm']:
        error.append('Password did not match password comfirmation')
    if len(exist_email)>0:
        error.append('This email is already exist')
    if error:
        for e in error:
            messages.error(request, e)
    
    else:
        hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        correct_hashed_pw = hashed_pw.decode('utf-8')
        new_user = User.objects.create(first_name=form['first_name'],last_name=form['last_name'],email=form['email'],password=correct_hashed_pw)
        request.session['userID']=new_user.id

    return redirect('/')

def log(request):
    form = request.POST
    try:
        user = User.objects.get(email=form['email'])
    except:
        messages.error(request, 'This email is not registered')
        return redirect('/')
    check = bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())
    if check:
        request.session['userID'] = user.id
    else:
        messages.error(request,'Wrong password!')
        return redirect('/')

    return redirect('/info/{}'.format(request.session['userID']))

def info(request,userID):
    if not 'userID' in request.session:
        messages.error(request, 'You need to login.')
        return redirect('/')

    if not request.session['userID'] == userID:
        messages.error(request, 'You do not have access to this page.')
        return redirect('/info/{}'.format(request.session['userID']))

    user = User.objects.get(id=userID)
    context={
        'thisGuy':user
    }

    return render(request,'info.html',context)

def logout(request,userID):
    request.session.clear()
    return redirect('/')