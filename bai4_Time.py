from datetime import timedelta

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

        #kiểm tra số giờ, phút, giây hợp lệ hay không
        if 0 > self.hour > 23 or 0 > self.minute > 60 or 0 > self.second > 60:
            raise ValueError('Invalid Time')

    @staticmethod
    def is_valid(h, m, s):
        if 0 > h > 23 or 0 > m > 60 or 0 > s > 60:
            return False
        return True

    #chuyển tổng số giây thành giờ
    @classmethod
    def from_seconds(cls,total):
        total %= 86400  #phần dư ra còn lại là thời gian của 1 ngày
        hour,temp = divmod(total, 3600) #láy giờ, phần temp là phần còn lại là phần của m,s(hour là phần nguyên, temp là phần dư)
        minute, second = divmod(temp, 60)
          
        return cls(hour, minute, second)

    #hàm chuyển đổi giờ/phút/giây thành giây
    @staticmethod
    def to_seconds(h,m,s):
        if 0 > h > 23 or 0 > m > 60 or 0 > s > 60:
            raise ValueError('Invalid Time')
        
        time = timedelta(hours=h, minutes=m,seconds=s)
        total = time.total_seconds()
        
        return total

    #hàm thêm số giây vào giờ hiện tại -> tính giờ tiếp theo
    def add_seconds(self, n):
        time = timedelta(hours=self.hour,minutes=self.minute,seconds=self.second)   
        total = time.total_seconds() + n    #chuyển đổi tất cả(giờ mới, cũ) thành tổng số giây
        value = self.from_seconds(total) #sử dụng lại hàm trên để tính toán và chuyển đổi về đúng định dạng
        
        return value

    def __lt__(self, other):
        time_self = timedelta(hours=self.hour,minutes=self.minute,seconds=self.second)
        time_other = timedelta(hours=other.hour,minutes=other.minute,seconds=other.second)

        total_self, total_other = time_self.total_seconds(), time_other.total_seconds()

        return total_self < total_other

    def __sub__(self, other):
        time_self = timedelta(hours=self.hour,minutes=self.minute,seconds=self.second)
        time_other = timedelta(hours=other.hour,minutes=other.minute,seconds=other.second)
        
        total_self, total_other = time_self.total_seconds(), time_other.total_seconds()

        return int(total_self - total_other)


    def __str__(self):
        return f"{int(self.hour):02d}:{int(self.minute):02d}:{int(self.second):02d}"

        
if __name__ == "__main__":
    t1 = Time(7, 30, 0)
    t2 = Time.from_seconds(41_400)
    print(t1, t2, t1 < t2)
    print(t1.add_seconds(5_000), Time(23, 59, 50).add_seconds(15))
    print(t2 - t1, Time.is_valid(24, 0, 0))