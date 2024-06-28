from django.shortcuts import render
from django import forms

# Create your views here.
# library/views.py

from django.shortcuts import render
from .models import Book, Author,Borrower
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

def book_list(request):
    books = Book.objects.all()  
    return render(request, 'book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()  
    return render(request, 'author_list.html', {'authors': authors})

def borrower_list(request):
    borrowers = Borrower.objects.all()  # Fetch all borrowers from the database
    return render(request, 'borrower_list.html', {'borrowers': borrowers})

def add_book(request):
    if request.method == 'POST':
        isbn = request.POST.get('isbn')
        title = request.POST.get('title')
        author_name = request.POST.get('author_name')
        genre = request.POST.get('genre')
        published_year = request.POST.get('published_year')
        copies_available = request.POST.get('copies_available')

        
        author, created = Author.objects.get_or_create(author_name=author_name)

        
        book = Book.objects.create(
            isbn=isbn,
            title=title,
            author=author,
            genre=genre,
            published_year=published_year,
            copies_available=copies_available
        )
        
        return redirect('book_list')  

    return render(request, 'book_form.html')  

def add_author(request):
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        author_name = request.POST.get('author_name')
        # Create an author object
        author = Author.objects.create(author_name=author_name)
        return redirect('author_list')  

    return render(request, 'author_form.html')  

def add_borrower(request):
    if request.method == 'POST':
        borrower_id=request.POST.get('borrower_id')
        borrower_name = request.POST.get('borrower_name')
        contact_info = request.POST.get('contact_info')
        # Create a borrower object
        borrower = Borrower.objects.create(
            borrower_id=borrower_id,
            borrower_name=borrower_name,
            contact_info=contact_info
        )
        
        return redirect('borrower_list')  

    return render(request, 'borrower_form.html')  