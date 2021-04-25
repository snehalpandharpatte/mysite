from Book.models import Book

# ORM queries:

# to run python file in db shell
# exec(open("H:\\snehal\\Django\\Library\\Book\\db_shell.py").read())
'''
#all data
all_data = Book.objects.all()
print(all_data)
print('-' * 50)

#single data
sid = 3
b2 = Book.objects.get(id=sid)
print(b2)
print("-" * 50)

#create data
b3 = Book.objects.create(name='oracle',author='fgfecg', qty=15, price=450)
print(b3.id)
print("-" * 50)

#update data
sid = 4
b4 = Book.objects.get(id=sid)
b4.name = 'LMN'
b4.author = 'FGJNNB'
b4.qty=75
b4.save()
print("-" * 50)

#delete data
sid = 4
b5 = Book.objects.get(id=sid)
b5.delete()

'''

# all_data = Book.objects.all()  # len(all_data)
# print(all_data) 
# for book in all_data:
#     print("---------------Details for id number:- ", book.id,"----------")
#     print("Book name:-", book.name)
#     print("Author name:-", book.author)
#     print("Quantity :-", book.qty)
#     print("Price per book:-", book.price)
    
# for updating and deleting books:  
# for book in all_data:
#     book.qty = 15
#     book.save()
    # book.delete()

# all_data = Book.objects.all()  # len(all_data)
# for i in all_data:
#     print(i.__dict__)


# all_data = Book.objects.values("id", "name", "qty")  # len(all_data)
# print(list(all_data))
# for i in all_data:
#     print(i)

# all_data = Book.objects.values_list()  # len(all_data)
# print(all_data)  #it gives list of tuple
# for i in all_data:
#     # print(i)
#     print(i[0])
# import random
# for i in range(1,36):
#     b = Book.objects.create(name=chr(random.randint(65,90)) * 5, author= chr(random.randint(65,90)) * 3, qty=random.randint(15,85), price=random.randint(200,900))
#     b.save()


# books = Book.objects.filter(id__gt=15)  # len(all_data)
# for i in books:
#     print(i.__dict__)

# books = Book.objects.filter(id__gte=15)  # len(all_data)
# for i in books:
#     print(i.__dict__)

# books = Book.objects.filter(id__lt=15)  # len(all_data)
# for i in books:
#     print(i.__dict__)

# books = Book.objects.filter(id__lte=15)  # len(all_data)
# for i in books:
#     print(i.__dict__)


# name- starswith. endswith, istartswith(case insensitive)
# books = Book.objects.filter(name__startswith='E').values("id","name")  
# for i in books:
#     print(i)

# books = Book.objects.filter(name__endswith='G').values("id","name")  
# for i in books:
#     print(i)   

# python django case insensitive
# books = Book.objects.filter(name__istartswith='e').values("id","name")  
# for i in books:
#     print(i)

#  order ascending and descending order:
# Ascending order:
# b = Book.objects.all().order_by("name") 
# print(b)

# Descending order:
# b = Book.objects.all().order_by("-name") 
# print(b)

# b = Book.objects.count() # .count(), len(), count()
# print(b)

# b = Book.objects.all()[34] 
# print(b)

# b = Book.objects.all()[0:5] 
# print(b)

# l = [i for i in range(1,16)]
# b = Book.objects.filter(id__in=l)  
# print(b)

# l = [i for i in range(1,16)]
# b = Book.objects.all().exclude(id__in=l)  
# print(b)

# Book.objects.bulk_create([
# Book(name = 'Java', author = 'ABCD',qty= 45,price=550),
# Book(name = 'Python', author = 'DEFG',qty= 55,price=450),
# Book(name = 'oracle', author = 'GHIJ',qty= 40,price=350),
# Book(name = 'DEF', author = 'Qerty',qty= 45,price=550),
# Book(name = 'LMNO', author = 'PQRS',qty= 30,price=250)
# ])

# objs = Book.objects.filter(id__in=[36,37,38,39,40])
# Book.objects.bulk_update(objs)

# in bulk values are changed:

# Book.objects.filter(id__in=[36,37,38,39,40]).update(price=900)




# --------------details for id number------------
# book name:-
# author name:-
# qty:-
# price per book:-
# -----------------details for id number-------------


# Book.objects.bulk_create([
# Book(name = 'Java', author = 'ABCD',qty= 45,price=550),
# Book(name = 'Python', author = 'DEFG',qty= 55,price=450),
# Book(name = 'oracle', author = 'GHIJ',qty= 40,price=350),
# Book(name = 'DEF', author = 'Qerty',qty= 45,price=550),
# Book(name = 'LMNO', author = 'PQRS',qty= 30,price=250)])
