from django.db import models

# Create your models here.
# app name - Book, model name -Book
class BookActiveManager(models.Manager):  #custom manager
    def get_queryset(self):
        return super(BookActiveManager, self).get_queryset().filter(is_deleted='N')

class BookInactiveManager(models.Manager):  #custom manager
    def get_queryset(self):
        return super(BookInactiveManager, self).get_queryset().filter(is_deleted='Y')

class Book(models.Model):
    # id === by default
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    is_Published = models.BooleanField(default=False)
    is_deleted = models.CharField(max_length=1, default='N')
    active_objects = BookActiveManager() 
    inactive_objects = BookInactiveManager() 
    objects = models.Manager()
    
    def __str__(self):
        return f"{self.id}---{self.name} ---{self.author}"

    class Meta:
        
        db_table = "bookinfo"

# app name - small case
# create table book_book(id unique AUTO-INCREMENT, name varchar(100), author varchar(100), qty int, price float)

'''
(denv) H:\snehal\Django\Library>python manage.py shell
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from Book.models import Book
>>> Book.objects.all()
<QuerySet [<Book: wings of fire ---APJ Kalam>, <Book: python ---xyz>]>
>>> b = Book.objects.all()
>>> type(b)
<class 'django.db.models.query.QuerySet'>
>>> list(b)
[<Book: wings of fire ---APJ Kalam>, <Book: python ---xyz>]
>>> b1 = list(b)
>>> type(b1)
<class 'list'>
>>> Book.objects.get(id=3)
<Book: python ---xyz>
>>> b2 = Book.objects.get(id=3)
>>> b2
<Book: python ---xyz>
>>> type(b2)
<class 'Book.models.Book'>
>>> Book.objects.create(name = 'DEF', author = 'Qerty',qty= 45,price=550)
<Book: DEF ---Qerty>
>>> b4 = Book(name = 'DEF', author = 'Qerty',qty= 45,price=55)
>>> b4.save()
>>> b5 = Book.objects.get(id=5)
>>> b5
<Book: DEF ---Qerty>
>>> b5.name = 'PQR'
>>> b5.save()
>>> b6 = Book.objects.get(id=6)
>>> b6
<Book: DEF ---Qerty>
>>> b6.delete()
(1, {'Book.Book': 1})

'''
def my_custom_sql():
    from django.db import connection, transaction
    cursor = connection.cursor()

    # Data modifying operation - commit required
    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    transaction.commit_unless_managed()

    # Data retrieval operation - no commit required
    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchone()

    return row


from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...

from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...