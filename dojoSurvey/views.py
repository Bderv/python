from django.shortcuts import render, redirect


def index(request):
    context = {

        }
    return render(request,'index.html', context)


def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    loc_from_form = request.POST['location']
    lang_from_form = request.POST['language']
    sub_from_form = request.POST['subject']
    context = {
    	"name_on_template" : name_from_form,
    	"loc_on_template" : loc_from_form,
        "lang_on_form" : lang_from_form,
        "sub_on_form" : sub_from_form,
    }
    return render(request,"show.html",context)



def some_function(request):
    if request.method == "GET":
    	print(request.GET)
    if request.method == "POST":
        print(request.POST)
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]

