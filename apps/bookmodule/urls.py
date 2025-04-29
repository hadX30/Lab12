from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.formatting, name="books.formatting"),
    path('html5/listing', views.listing, name="books.listing"),
    path('html5/tables', views.tables, name="books.tables"),
    path('search/', views.search, name="books.search"),
    path('simple/query', views.simple_query, name="books.simple_query"),
    path('complex/query', views.complex_query, name="books.complex_query"),
    #path('lab8/task1', views.task1, name="books.task1"),
    #path('lab8/task2', views.task2, name="books.task2"),
    #path('lab8/task3', views.task3, name="books.task3"),
    #path('lab8/task4', views.task4, name="books.task4"),
    #path('lab8/task5', views.task5, name="books.task5"),
    #path('lab8/students', views.students, name="books.students"),
    path('lab9/task1', views.task1, name="books.task1"),
    path('lab9/task2', views.task2, name="books.task2"),
    path('lab9/task3', views.task3, name="books.task3"),
    path('lab9/task4', views.task4, name="books.task4"),
    path('lab10_part1/listbooks', views.listbooks, name="listbooks"),
    path('lab10_part1/addbook', views.addbook, name="addbook"),
    path('lab10_part1/editbook/<int:bID>', views.editbook, name="editbook"),
    path('lab10_part1/deletebook/<int:bID>', views.deletebook, name="deletebook"),
    path('lab10_part2/listbooks2', views.listbooks2, name="listbooks2"),
    path('lab10_part2/addbook2', views.addbook2, name="addbook2"),
    path('lab10_part2/editbook2/<int:bID>', views.editbook2, name="editbook2"),
    path('lab10_part2/deletebook2/<int:bID>', views.deletebook2, name="deletebook2"),
    
#___________________________________________LAB 11_____________________________________________________________
    path('lab11_task1/list_students',views.list_students, name ="list_students"),
    path('lab11_task1/add_student',views.add_student, name ="add_student"),
    path('lab11_task1/edit_student/<int:sID>/',views.edit_student, name ="edit_student"),
    path('lab11_task1/delete_student/<int:sID>/',views.delete_student, name ="delete_student"),
    path('lab11_task2/list_students2',views.list_students2, name ="list_students2"),
    path('lab11_task2/add_student2',views.add_student2, name ="add_student2"),
    path('lab11_task2/edit_student2/<int:sID>/',views.edit_student2, name ="edit_student2"),
    path('lab11_task2/delete_student2/<int:sID>/',views.delete_student2, name ="delete_student2"),
    path('register_page/',views.register_page, name ="register_page"),
    # path('add_document/', views.add_document, name='add_document'),
    # path('list_documents/', views.list_documents, name='list_documents'),

    
    
    
    #-----------------------------Practice section-----------------
    path('practise/index3', views.index3, name= "index3"),
    path('practise/listproduct', views.listproduct, name= "listproduct"),
    path('practise/viewproduct/<int:pID>', views.viewproduct, name= "viewproduct"),
    path('practise/editproduct/<int:pID>', views.editproduct, name= "editproduct"), 
    path('practise/delproduct/<int:pID>', views.delproduct, name= "delproduct"), 
    #-----------------------------Practice section-----------------

]
