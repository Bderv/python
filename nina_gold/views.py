from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'index.html')

def process_form(request):
    print('request.POST', request.POST["places"])
    if request.POST['places'] == 'farm':
        rand_num = randint(10,20)
    elif request.POST['places'] == 'cave':
        rand_num = randint(5,10)
    elif request.POST['places'] == 'house':
        rand_num = randint(2,5)
    elif request.POST['places'] == 'casino':
        rand_num = randint(-50,50)
    print('random number is ', rand_num)
    now = datetime.now()
    current_time = now.strftime("%Y/%m/%d %I:%M %p")
    request.session['total_gold'] += rand_num
    print('total_gold', request.session['total_gold'])

    if rand_num < 0:
        request.session['activities'].append({'message': f"Entered a casino and lost{abs(rand_num)}....OUCH ({current_time})", 'action': 'lost'})
    else:
        request.session['activities'].append({'message': f"Earned {rand_num} from the {request.POST['places']}! ({current_time})", 'action': 'gain'})
    return redirect('/')

    