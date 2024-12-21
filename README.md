# Thuật toán DFS và BFS

DFS và BFS là các thuật toán tìm kiếm cơ bản.

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

## 2. BFS (Breadth-First Search)

BFS duyệt theo chiều rộng, ưu tiên thăm các đỉnh ở cùng cấp độ, sau đó mới đi xuống các cấp độ tiếp theo.

### Lược đồ thuật toán BFS:

1. **Bước 1**: Đánh dấu đỉnh nguồn là đã thăm và thêm vào hàng đợi.
2. **Bước 2**: Lấy đỉnh đầu tiên trong hàng đợi ra và in đỉnh đó.
3. **Bước 3**: Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại:
    - Đối với mỗi đỉnh kề chưa thăm, đánh dấu là đã thăm và thêm vào hàng đợi.
4. **Bước 4**: Lặp lại bước 2 và 3 cho đến khi hàng đợi trống.

### Cách thức hoạt động:
- BFS sẽ thăm tất cả các đỉnh ở cùng cấp độ trước, sau đó mới tiếp tục duyệt các cấp độ sâu hơn.
- Thường sử dụng **hàng đợi (queue)** để quản lý các đỉnh cần thăm.

---

## 3. Ví dụ, demo

Giả sử ta có đồ thị sau:

<pre>
graph = {
    {1, 2},       // Đỉnh 0 kề với 1, 2
    {0, 2},       // Đỉnh 1 kề với 0, 2
    {0, 1, 3, 4}, // Đỉnh 2 kề với 0, 1, 3, 4
    {2},          // Đỉnh 3 kề với 2
    {2}           // Đỉnh 4 kề với 2
}
</pre>

Đồ thị sẽ được duyệt và xử lý qua từng đỉnh, sau đó trả về kết quả bằng `cout`:
<pre>
Test do thi 1:
DFS tu dinh 1: 1 0 2 3 4 
BFS tu dinh 1: 1 0 2 3 4
</pre>
