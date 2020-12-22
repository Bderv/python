from django.shortcuts import render, redirect
from .models import Books

def index(request):
    all_books = Books.objects.all()
    context = {
        'books': all_books
    }
    return render(request, "index.html", context)

def create(request):
    print(request.POST)
    Books.objects.create(title=request.POST['btitle'], desc=request.POST['bdesc'])
    return redirect('/')