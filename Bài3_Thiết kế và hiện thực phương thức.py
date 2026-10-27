import math

class Fraction:
    def __init__(self, num, den=1): #num = tu so/ den = mau so
        self.num = num
        self.den = den

        if self.den == 0:
            raise ValueError('Zero denominator')
        elif self.den < 0:
            self.num = -self.num
            self.den = -self.den
        #rút gọn
        x = math.gcd(self.num, self.den)

        self.num = self.num // x
        self.den = self.den // x    #phân số sau rút gọn


    @classmethod
    def from_string(cls, text):
        n = (text.split('/'))  #'3/4' -> [3.0, 4.0]

        num = int(n[0])
        den = int(n[1])

        return cls(num, den)
    
    def __add__(self, other):   #+

        if isinstance(other, int):
             other = Fraction(other, 1)

        num = (self.num * other.den) + (other.num * self.den)
        den = self.den * other.den
        return Fraction(num,den)

    def __sub__(self, other):   #-
            num = (self.num * other.den) - (other.num * self.den)
            den = self.den * other.den
            return Fraction(num,den)

    def __mul__(self, other):   #*
         return Fraction((self.num * other.num), (self.den * other.den))

    def __truediv__(self, other):   #/
         if other.num == 0:
              raise ZeroDivisionError
         return Fraction((self.num * other.den),(self.den * other.num))

    def __eq__(self, other):    #==
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):    # <
         return self.num * other.den < other.num * self.den

    def __str__(self):      #print
         if self.den == 1:
              return f'{self.num}'
         return f"{self.num}/{self.den}"

    def __repr__(self):
         return f'Fraction({self.num},{self.den})'

    def to_float(self):
         return self.num / self.den

    def __radd__(self, other):
         return self.__add__(other)

 
if __name__ == "__main__":
    a = Fraction(1, 2)
    b = Fraction.from_string("3/4")
    print(a + b, a - b, a * b, a / b)
    print(Fraction(2, -4), Fraction(6, 3), repr(a))
    print(Fraction(1, 2) == Fraction(2, 4), a < b)
    fs = [Fraction(3, 4), Fraction(1, 3), Fraction(1, 2)]
    print(*sorted(fs))
    print(b.to_float())

    print(a + 1)
    print(1 + a)