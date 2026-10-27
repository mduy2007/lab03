import datetime

class Book:
  total_book = 0
  libary_name = 'TVU Libary'
  time = datetime.date.today()

  def __init__(self, title: str, author: str, year: int):
    self.title = title
    self.author = author
    self.year = year
    Book.total_book += 1

  def info(self):
    return (f"Name: {self.title}\nAuthor: {self.author}\nYear: {self.year}")

  def age_book(self, year):
    return year - self.year

b1 = Book("Python Crash Course", "Eric Matthes", 2019)
b2 = Book("Fluent Python", "Luciano Ramalho", 2022)

if __name__ == "__main__":
    print(b1.info())
    print(b2.age_book(Book.time.year))
    print(Book.total_book, b1.libary_name)