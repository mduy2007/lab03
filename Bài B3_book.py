class Book:
    def __init__(self, isbn: str, title: str):
        self.isbn = isbn
        self.title = title
        self.borrower = None  # Ban đầu chưa ai mượn (None)

    def is_available(self) -> bool:
        """Sách còn trống nếu chưa có ai mượn"""
        return self.borrower is None

class Member:
    MAX_BOOKS = 2  # Thuộc tính lớp: giới hạn số sách được mượn

    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.books = []  # Danh sách các object Book đang mượn

    def borrow(self, book: Book):
        # 1. Kiểm tra sách đã có ai mượn chưa
        if not book.is_available():
            raise ValueError(f"'{book.title}' is not available")
        
        # 2. Kiểm tra xem người này đã mượn đủ số sách cho phép chưa
        if len(self.books) >= self.MAX_BOOKS:
            raise ValueError(f"{self.name} reached limit")
        
        # 3. Cập nhật 2 chiều: Người mượn giữ sách, Sách ghi nhận người mượn
        self.books.append(book)
        book.borrower = self

    def give_back(self, book: Book):
        # 1. Kiểm tra xem cuốn sách này có thực sự do người này mượn không
        # (Tránh trường hợp Bình đi trả sách mà An đang mượn)
        if book.borrower != self:
            raise ValueError("Book not borrowed by this member")
        
        # 2. Cập nhật 2 chiều: Xóa khỏi list của người mượn, Xóa người mượn khỏi sách
        self.books.remove(book)
        book.borrower = None


if __name__ == "__main__":
    b1 = Book("001", "Python Basics")
    b2 = Book("002", "OOP in Python")
    b3 = Book("003", "Data Science")
    an, binh = Member("M01", "An"), Member("M02", "Binh")
    
    an.borrow(b1); an.borrow(b2)
    print([b.title for b in an.books], b1.borrower.name) 
    
    for action in (lambda: binh.borrow(b1), 
                   lambda: an.borrow(b3),   
                   lambda: binh.give_back(b2)): 
        try:
            action()
        except ValueError as e:
            print("Error:", e)
            
    an.give_back(b1); binh.borrow(b1)
    print(b1.borrower.name, len(an.books), b1.is_available(), b3.is_available())