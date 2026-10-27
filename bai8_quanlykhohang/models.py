class Product:
    def __init__(self, code: str, name: str, price: float, quantity: int):
        self.__code = code  # Thuộc tính private, chỉ đọc
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def code(self):
        return self.__code

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be >= 0")
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity must be >= 0")
        self.__quantity = value

    @property
    def value(self):
        return self.price * self.quantity

    def __str__(self):
        # Định dạng một dòng của bảng tồn kho
        return f"{self.code:<6} | {self.name:<15} | {self.price:>10,.0f} | {self.quantity:>5} | {self.value:>12,.0f}"


class Inventory:
    def __init__(self):
        self.__products = {}  # Dict: mã hàng -> đối tượng Product

    def add(self, p: Product):
        if p.code in self.__products:
            raise ValueError("Duplicate code")
        self.__products[p.code] = p

    def import_stock(self, code: str, qty: int):
        if code not in self.__products:
            raise KeyError(f"Product {code} not found")
        if qty <= 0:
            raise ValueError("Quantity must be > 0")
        self.__products[code].quantity += qty

    def export_stock(self, code: str, qty: int):
        if code not in self.__products:
            raise KeyError(f"Product {code} not found")
        
        product = self.__products[code]
        if product.quantity < qty:
            raise ValueError("Not enough stock")
        
        product.quantity -= qty

    def search(self, keyword: str):
        keyword = keyword.lower()
        
        return [p for p in self.__products.values() 
                if keyword in p.code.lower() or keyword in p.name.lower()]

    def low_stock(self, threshold: int = 5):
        # Trả về danh sách các sản phẩm có số lượng <= ngưỡng
        return [p for p in self.__products.values() if p.quantity <= threshold]

    @property
    def total_value(self):
        # Tính tổng giá trị tồn kho
        return sum(p.value for p in self.__products.values())

    def __len__(self):
        return len(self.__products)

    def __contains__(self, code: str):
        return code in self.__products