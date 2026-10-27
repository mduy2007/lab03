class Student:
    def __init__(self, sid: str, name: str, scores: dict = None):
        self.sid = sid
        self.name = name
        self.scores = scores if scores is not None else {}

    def add_score(self, subject, score):
       
        if score < 0 or score > 10:
            raise ValueError('Score must be in [0, 10]')
        self.scores[subject] = score

    def average(self):
        if not self.scores:
            return 0.0
        tong = sum(self.scores.values())
        so_luong = len(self.scores)
        return tong / so_luong    

    def __str__(self):
        return f'{self.sid} {self.name:<6} {self.average():.2f}'



class Classroom:
    def __init__(self, name: str):
        self.name = name
        self.students = []

    def add(self, st: Student):
        # Kiểm tra trùng mã sinh viên (st.sid)
        for s in self.students:
            if s.sid == st.sid:
                raise ValueError(f"Duplicate id {st.sid}")
        self.students.append(st)

    def find(self, sid: str):
        for s in self.students:
            if s.sid == sid:
                return s  
        return None  

    def remove(self, sid: str):
        for s in self.students:
            if s.sid == sid:
                self.students.remove(s) 
                return True
        return False

    def ranking(self):
        # Sắp xếp giảm dần theo điểm trung bình (gọi hàm average())
        return sorted(self.students, key=lambda sv: sv.average(), reverse=True)

    def report(self):
        print(f'=== {self.name} ===')
        # Lấy danh sách đã sắp xếp từ hàm ranking()
        danh_sach_xep_hang = self.ranking()
        for sv in danh_sach_xep_hang:
            print(sv) 
            
if __name__ == '__main__':
    cl = Classroom("DA24TTA")
    data = [("110001", "An",   {"OOP": 8,   "CSDL": 7}),
            ("110002", "Binh", {"OOP": 9,   "CSDL": 8.5}),
            ("110003", "Chi",  {"OOP": 6.5, "CSDL": 7.5})]
    for sid, name, scores in data:
        st = Student(sid, name)
        for subject, score in scores.items():
            st.add_score(subject, score)
        cl.add(st)

    cl.report()
    print(cl.find("110003").name, cl.remove("110009"))
    try:
        cl.add(Student("110001", "Dung"))
    except ValueError as e:
        print("Error:", e)
