"""
Class RATES
thuộc tính lớp: 'VND' = 25_000 | 'USD' = 1 -> quy đổi
thuộc tính object: amount(>=0): tiền, currency:đơn vị --> mandatory: True | if not ['VNĐ','USD', ''] --> ValueError
logic đầu vào:
--> nhận giá trị đầu vào(mặc định):nếu int < 1000 --> USD | int > 1000 --> VNĐ
--> nhận giá trị đầu vào(có đơn vị cố định): tách chuỗi dựa vào kí tự " "(cách), quy ước [0] -> giá tiền [1] -> đơn vị
logic xử lí:
theo quy ước 1 'USD' = 25_000 'VNĐ'

Các Hàm và cách hoạt động:
from_string(text):
    if not isintance(text, str) --> ValueError('Dữ liệu đầu vào không hợp lệ)   // Nhận diện đầu vào
    // tách đơn vị amount,currency = split(' ')
    return amount, currency

to(currency):
    if not isintance(currency, str) --> valueError
    self.amount ==> self.amount.currency // xử lí chuyển đổi giá trị(với USD -> VND == amount.USD * self.amount.VND <==> tương tự ngược lại)
    return amount, currency


...
"""

class Rates:
    VND = 25_000
    USD = 1   #đơn vị tiền tệ

    def __init__(self, amount: int, currency = ''):

        self.amount = amount
        self.currency = currency

        if self.amount < 0:
            raise ValueError('Invalid amount')

        if self.currency not in ['VND', 'USD', '']:
            raise ValueError(f'Unsuported currency {currency}')
        
        if self.currency == '':
            if self.amount < 1000:
                self.currency = 'USD'
            else:
                self.currency = 'VND'

        
    #hàm chuyển đổi từ type str sang type int - str
    @classmethod
    def from_string(cls, text):
        if not isinstance(text, str) or len(text.split(' ')) > 2:   #xác nhận xem đầu vào có hợp lệ/đúng định dạng không
            raise ValueError('Invalid input')
        
        amount, currency = text.split(' ')

        return cls(int(amount), currency)


    #chuyển đơn vị theo giá trị
    def to(self,currency):
        if currency not in ['VND', 'USD']:
            raise ValueError(f'Unsupported Currency {currency}')    #báo lỗi nếu đơn vị không hợp lệ
        
        if currency == self.currency:   #nếu đơn vị 2 bên giống nhau trả về số tiền mặc định
            return self
        
        if currency == 'VND':   #chuyển từ USD -> VND
            new_amount = self.amount * Rates.VND
            new_currency = currency

        else:   #ngược lại từ VND -> USD
            new_amount = self.amount / Rates.VND
            new_currency = currency

        return Rates(new_amount, new_currency)  #trả về giá trị mới


    def __add__(self,other):    
        
        if self.currency == "VND":
            other = other.to('VND')
            new_amount = self.amount + other.amount
        else:
            other = other.to('USD')
            new_amount = self.amount + other.amount
        
        return Rates(new_amount, self.currency) #return lại giá trị mới và tạm thời gán, không ghi đè

    
    def __eq__(self, value):
        """1: Chuyển đổi đơn vị và tiền về VND
            2: lấy 2 số so sánh với nhau và return về True False
             """
        self = self.to('VND')  
        value = value.to('VND') #gọi hàm to() để xử lí

        return self.amount == value.amount

    def __lt__(self, other):
        self = self.to('VND')  
        other = other.to('VND') #gọi hàm to() để xử lí

        return self.amount < other.amount


    def __str__(self):
        if self.currency == 'VND':
            return f'{self.amount:,.0f} {self.currency}'
        return f'{self.amount:,.2f} {self.currency}'
    

if __name__=='__main__':
    a = Rates(150_000)
    b = Rates.from_string("10 USD")
    print(a, b)
    print(a + b, b + a)
    print(b.to("VND"), Rates(250_000) == b, a < b)
    try:
        Rates(5, "EUR")
    except ValueError as e:
        print("Error:", e)