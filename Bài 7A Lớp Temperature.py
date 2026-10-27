class Temperature:
    def __init__(self, celsius: float = 0):
        # Gọi setter để nó kiểm tra luôn giá trị lúc khởi tạo
        self.celsius = celsius 

    @property
    def celsius(self):
        """Trả về độ C"""
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        """Kiểm tra điều kiện trước khi gán"""
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self.__celsius = value

    @property
    def fahrenheit(self):
        """Getter: Tính từ độ C"""
        return self.__celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter: Đổi từ F sang C, rồi gán qua setter của C"""
        c_val = (value - 32) * 5 / 9
        self.celsius = c_val  # Tự động được kiểm tra bởi celsius.setter

    @property
    def kelvin(self):
        """Read-only: Chỉ có getter, không có setter"""
        return self.__celsius + 273.15


if __name__ == "__main__":
    t = Temperature(25)
    print(t.celsius, t.fahrenheit, t.kelvin) 
    t.fahrenheit = 212
    print(t.celsius) 
    try:
        t.celsius = -300
    except ValueError as e:
        print("Error:", e) 
    try:
        t.kelvin = 0 
    except AttributeError:
        print("AttributeError")