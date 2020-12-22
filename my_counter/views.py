from django.shortcuts import render, redirect

def index(request):
    if 'Visitcount' not in request.session:
        request.session['Visitcount'] = 0
    request.session['Visitcount'] += 1
    if 'Realcount' not in request.session:
        request.session['Realcount'] = 0
    request.session['Realcount'] += 1
    return render(request,'index.html')

def destroy(request):
    del request.session['Visitcount']
    del request.session['Realcount']	# clears a specific key
    return redirect('/')

def addTwo(request):
    request.session['Visitcount'] += 2
    return render(request,'index.html')

def addby(request):
    print(request.GET['amount'])
    request.session['Visitcount'] += int(request.GET['amount'])
    return render(request,'index.html')