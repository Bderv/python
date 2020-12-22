from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users, Quotes
from django.db.models import Q
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    print(request.POST)
    validationErrors = Users.objects.regValidator(request.POST)
    print("***********")
    print(validationErrors)
    print("***********")
    if len(validationErrors)>0:
        for key, value in validationErrors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        pwhash = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        newUser = Users.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email_address = request.POST['email'], password = pwhash)
        request.session['loggedInID'] = newUser.id
        return redirect("/success")

def success(request):
    if 'loggedInID' not in request.session:
        for message in messages.get_messages(request):
            print("here's an error")
        messages.error(request, "You must login")
        return redirect("/")
    context = {
        'loggedinuser' : Users.objects.get(id=request.session['loggedInID'])
    }
    return render(request, "success.html", context)

def login(request):
    print(request.POST)
    validerrors = Users.objects.loginValidator(request.POST)
    if len(validerrors)>0:
        for key, value in validerrors.items():
            messages.error(request, value)
        return redirect("/")
    else: 
        print(validerrors)
        usersWithemail = Users.objects.filter(email_address = request.POST['email'])
        request.session['loggedInID'] = usersWithemail[0].id
    return redirect("/success")

def addQuote(request):
    if 'loggedInID' not in request.session:
        for message in messages.get_messages(request):
            print("here's an error")
        messages.error(request, "You must login")
        return redirect("/")
    context = {
        'loggedinuser' : Users.objects.get(id=request.session['loggedInID']),
        'allquotes' : Quotes.objects.all(),
        'likedquotes' : Quotes.objects.filter(favorites=Users.objects.get(id=request.session['loggedInID'])),
        'notlikedquotes' : Quotes.objects.exclude(favorites=Users.objects.get(id=request.session['loggedInID'])) 
    }
    return render(request, "quotes.html", context)

def createQuote(request):
    print(request.POST)
    validerrors = Quotes.objects.postValidator(request.POST)
    if len(validerrors)>0:
        for key, value in validerrors.items():
            messages.error(request, value)
        return redirect("/quotes")
    Quotes.objects.create(content = request.POST['content'], uploader= Users.objects.get(id=request.session['loggedInID']))
    return redirect("/quotes")

def likeContent(request, contentId):
    print(contentId)
    liker = Users.objects.get(id=request.session['loggedInID'])
    rant = Quotes.objects.get(id=contentId)
    liker.quotes_liked.add(contentId)
    return redirect("/quotes")

def unlikeContent(request, contentId):
    print(contentId)
    liker = Users.objects.get(id=request.session['loggedInID'])
    rant = Quotes.objects.get(id=contentId)
    liker.quotes_liked.remove(contentId)
    return redirect("/quotes")

def delete(request, contentId):
    c = Quotes.objects.get(id=contentId)
    c.delete()
    return redirect("/quotes")

def showUser(request, uploaderId):
    context = {
        'qPoster' : Users.objects.get(id=uploaderId),
        'allquotes' : Quotes.objects.all(),
    }
    return render(request, "users.html", context)



def logout(request):
    request.session.clear()
    return redirect("/")