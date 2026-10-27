class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.password = password # Gọi setter để kiểm tra pass lúc tạo

    @property
    def username(self):
        """Chỉ đọc"""
        return self.__username

    @property
    def password(self):
        """Chỉ ghi: Chặn hành vi đọc mật khẩu"""
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, value: str):
        # Kiểm tra độ dài và thành phần
        has_digit = any(c.isdigit() for c in value)
        has_alpha = any(c.isalpha() for c in value)
        
        if len(value) < 8 or not has_digit or not has_alpha:
            raise ValueError("Password needs >= 8 chars, letters and digits")
        
        # Lưu mật khẩu vào một biến private khác
        self.__password = value

    def check_password(self, value: str) -> bool:
        """Kiểm tra mật khẩu nhập vào có khớp không"""
        return self.__password == value


if __name__ == "__main__":
    u = User("an.nguyen", "tvu2026abc")
    print(u.username, u.check_password("tvu2026abc"), u.check_password("123"))
    for bad in ["short1", "onlyletters"]:
        try:
            u.password = bad
        except ValueError as e:
            print("Error:", e)      
    try:
        print(u.password)
    except AttributeError as e:
        print("AttributeError:", e)
    try:
        u.username = "x"
    except AttributeError:
        print("AttributeError: read-only")