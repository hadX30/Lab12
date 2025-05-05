from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Book,department,card,course, product,company,student2,student1,address1,address2,register1
from django.db.models import Count, Min, Max, Sum, Avg , Q
from django import forms
from .forms import BookForm,StudentForm1,StudentForm2,registration1
from django.contrib.auth.decorators import login_required
import os
from django.core.files.storage import FileSystemStorage
#import BookForm
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodules/index.html" , {"name": name})  #your render line
 
def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodules/show.html', context)

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def index(request):
    return render(request, "bookmodules/index.html")
def list_books(request):
    return render(request, 'bookmodules/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodules/one_book.html')
def aboutus(request):
    return render(request, 'bookmodules/aboutus.html') 
def links(request):
    return render(request, 'bookmodules/links.html') 
def formatting(request):
    return render(request, 'bookmodules/formatting.html') 
def listing(request):
    return render(request, 'bookmodules/listing.html') 
def tables(request):
    return render(request, 'bookmodules/tables.html') 
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodules/bookList.html', {'books':newBooks})

    return render(request, 'bookmodules/search.html') 

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodules/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodules/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodules/index.html')
    
#def task1(request):
    mybooks=Book.objects.filter(Q(price__gte = 80 )) # <- multiple objects
    return render(request, 'bookmodules/bookList.html', {'books':mybooks})

#def task2(request):
    mybooks=Book.objects.filter(Q(edition__gte = 3 ) & (Q(title__icontains ='co')) | (Q(author__icontains ='co'))) # <- multiple objects
    return render(request, 'bookmodules/bookList.html', {'books':mybooks})
#def task3(request):
    mybooks=Book.objects.filter(~Q(edition__gte = 3 ) & (~Q(title__icontains ='co')) | (~Q(author__icontains ='co'))) # <- multiple objects
    return render(request, 'bookmodules/bookList.html', {'books':mybooks})
#def task4(request):
    mybooks=Book.objects.order_by('title')
    return render(request, 'bookmodules/bookList.html', {'books':mybooks})
#def task5(request):
    Query = Book.objects.aggregate(NumBooks = Count('id'),total = Sum('price',default=0), average = Avg('price',default=0),max = Max('price',default=0), min = Min('price',default=0) )
    print(Query)
    return render(request, 'bookmodules/task5.html',{'Query':Query})

#def students(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodules/students.html', {'cities': cities})
def task1(request):
    departments = department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodules/department_student_count.html', {'departments': departments})
def task2(request):
    courses = course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodules/course_student_count.html', {'courses': courses})

def task3(request):
    # For each department, find the student with the lowest ID
    #departments = department.objects.all()
    #department_students = []

    #for dept in departments:
     #   oldest_student = student.objects.filter(department=dept).order_by('id').first()
      #  if oldest_student:
       #     department_students.append({
        #        'department': dept.name,
         #       'student': oldest_student.name,
          #      'student_id': oldest_student.id
           # })
    department_students = department.objects.annotate(student_count=Min('student__id'))
    
    print(department_students)
    return render(request, 'bookmodules/oldest_student_per_department.html', {'data': department_students})

def task4(request):
    departments = department.objects.annotate(student_count=Count('student')) \
                                    .filter(student_count__gt=2) \
                                    .order_by('-student_count')
    return render(request, 'bookmodules/departments_with_many_students.html', {'departments': departments})


def listbooks(request):
    
    books = Book.objects.all()
    return render(request, 'bookmodules/listbooks.html', {'books': books})
 
 
def addbook(request):
    #obj = None
    if request.method == 'POST':
       title = request.POST.get('title')
       price = request.POST.get('price')
       edition = request.POST.get('edition')
       author = request.POST.get('author')
       #authorObj = author.objects.get(id =author_id)
       
       obj = Book(title = title, price = price, edition = edition, author = author)
       obj.save()
       return redirect('listbooks')
    #authors= author.objects.all().order_by('fullname')
   
   
    return render(request, 'bookmodules/addbook.html')


def editbook(request, bID):
    book = Book.objects.get(id = bID)
    if request.method == 'POST':
       title = request.POST.get('title')
       price = request.POST.get('price')
       edition = request.POST.get('edition')
       author = request.POST.get('author')
       #authorObj = author.objects.get(id =author_id)
      
       
       book.title = title
       book.price = float(price)
       book.edition = int(edition)
       book.author = author
       book.save()
       return redirect('listbooks')
    #authors= author.objects.all().order_by('fullname')
   
   
    return render(request, 'bookmodules/editbook.html', {'book':book})

def deletebook(request, bID):
    obj = Book.objects.get(id = bID)
   # if request.method == 'POST':
    obj.delete()
    return redirect('listbooks')
   
   
   # return render(request, 'bookmodules/deleteBook.html', {'authors': authors})
   
   
def listbooks2(request):
    
    books = Book.objects.all()
    return render(request, 'bookmodules/listbooks2.html', {'books': books})

   

def addbook2(request):
   
    if request.method == 'POST':
      
        form = BookForm(request.POST)
        if form.is_valid():
          obj = form.save()
          return redirect('listbooks2')
    else:
        form = BookForm()

    #authors = author.objects.all().order_by('fullname')  
    return render(request, 'bookmodules/addbook.html', {'form': form})


def editbook2(request, bID):
    book = Book.objects.get(id=bID)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
          form.save()
          return redirect('listbooks2')
    else:
        form = BookForm(instance=book)
    #authors = author.objects.all().order_by('fullname')  
    return render(request, 'bookmodules/editbook.html', {'form': form,})
   

def deletebook2(request, bID):
    obj = Book.objects.get(id = bID)
   # if request.method == 'POST':
    obj.delete()
    return redirect('listbooks2')


 #-----------------------------Practice section-----------------
 
def index3(request):
     
     return render(request, 'bookmodules/homepage.html')
 
def listproduct(request):
    products = product.objects.all()
    return render(request, 'bookmodules/listproduct.html', {'products': products})
def viewproduct(request,pID):
    pro = product.objects.get(id = pID)
    return render(request, 'bookmodules/viewproduct.html', {'pro': pro})
def editproduct(request,pID):
    pro = product.objects.get(id = pID)
    if request.method == 'POST':
        
        kind = request.POST.get('kind')
        company_id = request.POST.get('company_id')
        companyObj = company.objects.get(id = company_id)
        expire_year = request.POST.get('expire_year')
        
        print(companyObj)
        pro.kind = kind
        pro.expire_year =expire_year
        pro.company= companyObj
        print(pro.kind)
        print(pro.company)
        pro.save()
        return redirect('listproduct')
        
    companys = company.objects.all().order_by('name')
    return render(request, 'bookmodules/editproduct.html', {'pro': pro, 'companys':companys})

def delproduct(request,pID):
    pro = product.objects.get(id = pID)
    pro.delete()
    return redirect('listproduct')
 
 
  #-----------------------------Practice section-----------------
  
  
  
#------------------------------------LAB11 Task 1-----------------------------------
def list_students(request):
    students = student1.objects.all()
    return render(request, 'bookmodules/list_students.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm1()
    return render(request, 'bookmodules/add_student.html', {'form': form})

@login_required 
def edit_student(request, sID):
    student = student1.objects.get( id=sID)
    print(student)
    if request.method == 'POST':
        form = StudentForm1(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm1(instance=student)
    return render(request, 'bookmodules/edit_student.html', {'form': form})

@login_required
def delete_student(request, sID):
    student = student1.objects.get( id=sID)
    student.delete()
    return redirect('list_students')

#------------------------------------LAB11 Task 2-----------------------------------

def list_students2(request):
    studentss = student2.objects.all()
    return render(request, 'bookmodules/list_students2.html', {'studentss': studentss})

@login_required(login_url='login')
def add_student2(request):
    if request.method == 'POST':
        form = StudentForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = StudentForm2()

    return render(request, 'bookmodules/add_student2.html', {'form': form})

@login_required(login_url='login')
def edit_student2(request, sID):
    student = student2.objects.get( id=sID)
    if request.method == 'POST':
        form = StudentForm2(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = StudentForm2(instance=student)
   # address = address2.objects.all().order_by('city')
    return render(request, 'bookmodules/edit_student2.html', {'form': form})
@login_required(login_url='login')
def delete_student2(request, sID):
    student = student2.objects.get( id=sID)
    student.delete()
    return redirect('list_students2')
#------------------------------------LAB11 Task 3-----------------------------------
def register_page(request):
    if request.method == 'POST':
        form = registration1(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return render(request, 'bookmodules/index.html')
    else:
        form = registration1()

    return render(request, 'bookmodules/register.html', {'form': form})

            
# def list_documents(request):
#     documents = Document.objects.all()
#     return render(request, 'bookmodules/list_documents.html', {'documents': documents})

# def add_document(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES) 
#         if form.is_valid():
#             form.save()
#             return redirect('list_documents')  
#     else:
#         form = DocumentForm()
#     return render(request, 'bookmodules/add_document.html', {'form': form})
   
        