from django.contrib import admin
from Book.models import Book
# Register your models here.

admin.site.register(Book)



class Student:
  def __init__(self, name):
    self.name = name
    
 
s1 = Student("ABC")
s1 = Student("XYZ")
s1 = Student("PQR")
