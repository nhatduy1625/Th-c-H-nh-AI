# Thuật toán DFS kết hợp A*

Sử dụng DFS cho các node ở nửa đầu và A* cho các node còn lại

## 1. DFS (Depth-First Search)

DFS đi sâu vào đồ thị, ưu tiên thăm các đỉnh sâu hơn trước khi quay lại các đỉnh khác.

### Lược đồ thuật toán DFS:

1. **Bước 1**: Đánh dấu đỉnh nguồn là đã thăm.
2. **Bước 2**: In đỉnh nguồn ra.
3. **Bước 3**: Duyệt qua các đỉnh kề chưa được thăm:
    - Đối với mỗi đỉnh kề chưa thăm, gọi đệ quy hàm DFS cho đỉnh đó.
4. **Bước 4**: Tiếp tục lặp lại bước 3 cho đến khi tất cả các đỉnh kề được thăm hết.

### Cách thức hoạt động:
- DFS sẽ đi vào các nhánh của đồ thị cho đến khi không còn đỉnh kề nào để thăm, sau đó quay lại và tiếp tục duyệt các nhánh khác.
- Thường sử dụng **ngăn xếp (stack)** hoặc **đệ quy** để duy trì các đỉnh cần thăm.

---

## 2. A*

A* là thuật toán tìm đường đi tốt nhất kết hợp giữa tìm kiếm theo heuristic và chi phí thực tế từ điểm xuất phát.

### Lược đồ thuật toán A*:

1. **Bước 1**: Khởi tạo hai danh sách:
   - Open list: chứa các node cần xét
   - Closed list: chứa các node đã xét
   
2. **Bước 2**: Thêm node xuất phát vào open list với:
   - g(n) = 0 (chi phí từ điểm xuất phát)
   - h(n) = giá trị heuristic
   - f(n) = g(n) + h(n)

3. **Bước 3**: Lặp cho đến khi tìm thấy đích hoặc open list rỗng:
   - Chọn node có f(n) nhỏ nhất từ open list
   - Nếu node là đích, kết thúc
   - Di chuyển node từ open list sang closed list
   - Xét các node kề:
     + Tính g, h, f cho mỗi node kề
     + Cập nhật hoặc thêm vào open list nếu tốt hơn

4. **Bước 4**: Truy vết đường đi từ đích về điểm xuất phát

### Cách thức hoạt động:
- A* sử dụng hàm đánh giá f(n) = g(n) + h(n)
  + g(n): chi phí thực từ điểm xuất phát đến node hiện tại
  + h(n): ước lượng chi phí từ node hiện tại đến đích
  + f(n): tổng chi phí ước lượng của đường đi
- Thuật toán luôn chọn node có f(n) nhỏ nhất để xét tiếp
- Đảm bảo tìm được đường đi tốt nhất nếu h(n) không vượt quá chi phí thực tế

---

## 3. Ví dụ In-Out:

Xét ma trận 4x3 sau đây, với:
- 1: đường đi
- 0: tường
### Input: 
<pre>
Grid = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1],
        [1, 0, 1]
    ]
</pre>
### Output:
<pre>
Đường đi hoàn chỉnh:
Phần DFS:
-> [3, 0] -> (2, 0) -> (2, 1) -> (2, 2) -> (1, 1) -> (0, 1) -> (0, 0) ->
Phần A*:
-> (0, 0) -> (0, 1) -> (0, 2) ->
</pre>

## Lược đồ Code:

![Grid](https://github.com/user-attachments/assets/9ed59a00-5460-41f8-9710-c699ae793c99)
