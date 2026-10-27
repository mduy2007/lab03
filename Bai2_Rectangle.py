class Rectangle:
    count = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height

        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be > 0")

        Rectangle.count += 1

    def area(self):
        return self.width * self.height
    

    def perimeter(self):
        return 2 * (self.width + self.height)
    

    def is_square(self):
        return self.width == self.height
    

    def scale(self, k):
        if k <= 0:
            raise ValueError('K must be > 0')

        self.width *=k
        self.height *=k


    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


    #2 hình = nhau khi cùng area()
    def __eq__(self, other):
        return Rectangle.area(self) == other.area()


    #hình có area() lớn nhất
    @classmethod
    def largest(cls,rects: list):
        if rects is None:
            raise ValueError
        
        i = 0
        temp = rects[0].area()

        for i in rects:
            if i.area() > temp:
                temp = i.area

        for i in rects:
            if i.area() == temp:
                return f"{i.width} x {i.height}"


if __name__ == "__main__":
    r = Rectangle(3, 4)
    r2 = Rectangle(3,6)
    r3 = Rectangle(3,6)
    print(r, r.area(), r.perimeter(), r.is_square())
    r.scale(2)
    print(r, r.area())
    print(Rectangle(5, 5).is_square())
    try:
        Rectangle(0, 3)
    except ValueError as e:
        print("Error:", e)

    print(r2.__eq__(r3))

    lst = [r,r2,r3]
    print(Rectangle.largest(lst))
