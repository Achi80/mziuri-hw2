from django.db import models

class Librarian(models.Model):
    User = models.CharField(max_length=20)
    Salary = models.IntegerField()
    Email = models.CharField(max_length=50)
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)

class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Genre = models.CharField(max_length=50)
    Pages = models.IntegerField()
    Is_taken = models.BooleanField(default=False)

    def return_book(self):
        self.Is_taken = False
        self.save()

class Customer(models.Model):
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    Book_Order = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)

    def return_book(self):
        if self.Book_Order and self.Book_Order.Is_taken:
            self.Book_Order.return_book()
            self.Book_Order = None
            self.save()
        else:
            raise ValueError("No book is currently borrowed.")

    