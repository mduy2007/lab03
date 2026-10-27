class Employee:
    raise_limit = 0.3 # Thuộc tính lớp

    def __init__(self, emp_id: str, name: str, salary: float):
        self.__emp_id = emp_id # Private
        self.name = name
        self.salary = salary   # Gọi setter để kiểm tra

    @property
    def emp_id(self):
        """Chỉ đọc, không có setter"""
        return self.__emp_id

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary must be >= 0")
        self.__salary = value

    def raise_salary(self, percent: float):
        """Tăng lương với điều kiện 0 < percent <= 0.3"""
        if percent <= 0 or percent > self.raise_limit:
            raise ValueError(f"Invalid raise percent") 
        
        # Tính lương mới và làm tròn đến hàng đơn vị
        new_salary = round(self.salary * (1 + percent))
        self.salary = new_salary # Gán qua setter cho an toàn


if __name__ == "__main__":
    e = Employee("E01", "An", 12_000_000)
    e.raise_salary(0.1)
    print(e.emp_id, f"{e.salary:,}") 
    try:
        e.salary = -1
    except ValueError as er:
        print("Error:", er) 