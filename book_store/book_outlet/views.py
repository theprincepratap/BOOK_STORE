from django.shortcuts import render , get_object_or_404
from .models import Book
# Create your views here.

def index(request):
    Book_list = Book.objects.all()
    return render(request, 'book_outlet/index.html',{
        "books":Book_list
    })

def  book_detail(request, slug):
    bd = get_object_or_404(Book, slug=slug)
    return render(request , 'book_outlet/details.html' , {
    "title": bd.title,
    "rating": bd.rating,
    "author": bd.author,
    "is_bestseller" : bd.is_bestselling 
    })
   
    
    