
### **Câu 1**
*   **Kết quả dự đoán:** `[1, 2, 3, 4]`
*   **Giải thích:**
    *   `x = [1, 2, 3]` tạo một list.
    *   `y = x` không tạo bản sao. Cả `x` và `y` đều đang trỏ đến **cùng một đối tượng list** trong bộ nhớ (tham chiếu).
    *   Toán tử `+=` trên list là phép toán tại chỗ (in-place), tức là nó thay đổi trực tiếp nội dung của list hiện tại (tương đương `y.extend([4])`).
    *   Vì `x` và `y` trỏ cùng một chỗ, nên khi `y` thay đổi, `x` cũng thay đổi theo.

### **Câu 2**
*   **Kết quả dự đoán:** `PYTHON PYTHON!`
*   **Giải thích:**
    *   `s = "PYTHON"` tạo một chuỗi (string).
    *   `t = s` khiến `t` trỏ đến cùng chuỗi đó.
    *   Tuy nhiên, trong Python, **chuỗi (string) là bất biến (immutable)**. Phép toán `t += "!"` không làm thay đổi chuỗi ban đầu mà nó tạo ra một **đối tượng chuỗi mới** là `"PYTHON!"` và gán lại cho biến `t`.
    *   Do đó, `s` vẫn giữ nguyên giá trị `"PYTHON"`, còn `t` mang giá trị mới.

### **Câu 3**
*   **Kết quả dự đoán:** `2 1 3`
*   **Giải thích:**
    *   `total = 0` là **biến lớp (class variable)**, dùng chung cho tất cả các đối tượng của lớp `Counter`.
    *   `self.value = 0` là **biến instance**, mỗi đối tượng `c1`, `c2` sẽ có một biến `value` riêng.
    *   `c1.inc()` chạy 2 lần: `c1.value` tăng lên 2, `Counter.total` tăng lên 2.
    *   `c2.inc()` chạy 1 lần: `c2.value` tăng lên 1, `Counter.total` tiếp tục tăng lên 3.
    *   Kết quả in ra lần lượt là `value` của `c1` (2), `value` của `c2` (1), và `total` của lớp (3).

### **Câu 4**
*   **Kết quả dự đoán:** `False True`
*   **Giải thích:**
    *   `p = P(1)` và `q = P(1)` tạo ra 2 đối tượng hoàn toàn khác nhau trong bộ nhớ, dù chúng có cùng giá trị `x=1`. Toán tử `==` mặc định sẽ so sánh địa chỉ vùng nhớ (vì lớp `P` không định nghĩa lại hàm `__eq__`), nên `p == q` trả về `False`.
    *   `r = p` khiến `r` và `p` trỏ đến cùng một địa chỉ bộ nhớ. Toán tử `is` dùng để kiểm tra xem 2 biến có trỏ đến cùng một đối tượng không. Do đó, `p is r` trả về `True`.

### **Câu 5**
*   **Kết quả dự đoán:** `['a', 'b'] ['a', 'b']`
*   **Giải thích:**
    *   Đây là "bẫy" kinh điển với **đối số mặc định có thể thay đổi (mutable default arguments)**.
    *   Giá trị mặc định `bag=[]` chỉ được khởi tạo **một lần duy nhất** khi định nghĩa hàm.
    *   Lần gọi 1: `add_item("a")` thêm "a" vào list mặc định, trả về `['a']`.
    *   Lần gọi 2: `add_item("b")` tiếp tục dùng cái list mặc định đó (đang chứa `['a']`), thêm "b" vào thành `['a', 'b']`.
    *   Hàm `print` đánh giá các đối số từ trái sang phải. Khi cả hai hàm chạy xong, danh sách mặc định cuối cùng là `['a', 'b']`. Vì cả 2 kết quả trả về đều trỏ đến cùng một list này, nên in ra cả hai đều là `['a', 'b']`.

### **Câu 6**
*   **Lưu ý:** Câu này sử dụng lại ngữ cảnh của Câu 4 (biến `P`, `p`, `r`).
*   **Kết quả dự đoán:** `99 99`
*   **Giải thích:**
    *   Truyền `p` (đang trỏ cùng chỗ với `r` ở Câu 4) vào hàm.
    *   Bên trong hàm: `p.x = 99` thay đổi thuộc tính `x` của đối tượng gốc. Lúc này cả `p` và `r` bên ngoài đều thấy `x = 99`.
    *   Tiếp theo: `p = P(0)` gán lại biến local `p` để trỏ sang một đối tượng mới. Biến `p` và `r` ở phạm vi bên ngoài (global) không bị ảnh hưởng bởi phép gán này.
    *   Dòng `p.x = 5` chỉ thay đổi đối tượng mới bên trong hàm, không ảnh hưởng ra ngoài.
    *   Kết quả in ra cả `p.x` và `r.x` đều là 99.

### **Câu 7**
*   **Kết quả dự đoán:**
    ```text
    A ['An', 'Binh', 'Chi']
    ['An', 'Binh']
    ```
*   **Giải thích:**
    *   `t2 = copy.copy(t1)`: Tạo **shallow copy** (bản sao nông). Đối tượng `t2` là mới, nhưng thuộc tính `members` của `t2` vẫn trỏ đến **cùng một list** với `t1`.
    *   `t3 = copy.deepcopy(t1)`: Tạo **deep copy** (bản sao sâu). `t3` và các thuộc tính bên trong nó (bao gồm cả list `members`) là hoàn toàn độc lập với `t1`.
    *   `t2.name = "B"` tạo ra một chuỗi mới, không ảnh hưởng tới `t1.name` (vẫn là "A").
    *   `t2.members.append("Chi")`: Vì `t2.members` và `t1.members` dùng chung list, nên list của `t1` cũng bị thêm "Chi".
    *   `t3` được copy độc lập từ trước khi thêm "Chi", nên `t3.members` vẫn giữ nguyên.

### **Câu 8**
*   **Kết quả dự đoán:** `[[1, 0], [1, 0]]`
*   **Giải thích:**
    *   `[0] * 2` tạo ra list `[0, 0]`.
    *   `[[0, 0]] * 2` không tạo ra 2 list con độc lập. Nó tạo ra một list lớn chứa **2 tham chiếu đến cùng một list con** `[0, 0]`.
    *   Khi bạn thực hiện `nums[0][0] = 1`, bạn đang truy cập vào list con bên trong và sửa phần tử đầu tiên của nó thành 1.
    *   Vì cả 2 phần tử của `nums` đều trỏ đến cùng một list con đó, nên cả hai đều hiển thị sự thay đổi: `[[1, 0], [1, 0]]`. (Để tạo mảng 2 chiều độc lập, nên dùng list comprehension: `[[0]*2 for _ in range(2)]`).

