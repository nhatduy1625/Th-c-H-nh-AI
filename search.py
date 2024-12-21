import math
import heapq

class Cell:
    def __init__(self):
        self.parent_i = 0 # Row
        self.parent_j = 0 # Column
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

ROW = 0
COL = 0

def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

def is_unblocked(grid, row, col):
    return grid[row][col] == 1

def is_end(row, col, dest):
    return row == dest[0] and col == dest[1]

def h_point(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

def trace(cell_details, dest):
    path = []
    row = dest[0]
    col = dest[1]

    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    path.append((row, col))
    path.reverse()
    return path

def dfs(grid, start, dest, visited):
    if not is_valid(start[0], start[1]) or not is_unblocked(grid, start[0], start[1]):
        return None
    
    if start == dest:
        return [start]
    
    visited.add((start[0], start[1]))
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for dir in directions:
        new_i = start[0] + dir[0]
        new_j = start[1] + dir[1]
        
        if (is_valid(new_i, new_j) and 
            is_unblocked(grid, new_i, new_j) and 
            (new_i, new_j) not in visited):
            
            path = dfs(grid, (new_i, new_j), dest, visited)
            if path:
                return [start] + path
    
    return None

def a_star(grid, src, dest, print_path=True):
    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Không hợp lệ~!!!")
        return False, []

    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Không thể di chuyển~!!!")
        return False, []

    if is_end(src[0], src[1], dest):
        print("Đã tới đích~!!!")
        return True, []

    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    found_dest = False

    while len(open_list) > 0:
        p = heapq.heappop(open_list)

        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                if is_end(new_i, new_j, dest):
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    if print_path:
                        path = trace(cell_details, dest)
                        print("->", end=" ")
                        for point in path:
                            print(point, end=" -> ")
                        print()
                    found_dest = True
                    return True, trace(cell_details, dest) if not print_path else True
                else:
                    g_new = cell_details[i][j].g + 1.0
                    h_new = h_point(new_i, new_j, dest)
                    f_new = g_new + h_new

                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

    if not found_dest:
        print("Không thể tìm đến đích~!!!")
        return False, []

def DFS_A(grid, src, dest):
    mid_row = (src[0] + dest[0]) // 2
    mid_col = (src[1] + dest[1]) // 2
    
    mid_point = None
    for i in range(-2, 3):
        for j in range(-2, 3):
            test_row = mid_row + i
            test_col = mid_col + j
            if (is_valid(test_row, test_col) and 
                is_unblocked(grid, test_row, test_col)):
                mid_point = (test_row, test_col)
                break
        if mid_point:
            break
    
    if not mid_point:
        print("Không thể tìm điểm trung gian hợp lệ!")
        return
        
    # Sử dụng DFS cho nửa đầu
    visited = set()
    dfs_path = dfs(grid, src, mid_point, visited)
    
    if not dfs_path:
        print("Không thể tìm đường đi phần đầu bằng DFS!")
        return
    
    # Sử dụng A* cho nửa sau
    success, astar_path = a_star(grid, mid_point, dest, print_path=False)
    if not success:
        print("Không thể tìm đường đi phần sau bằng A*!")
        return
    
    print("Đường đi hoàn chỉnh:")
    print(f"Phần DFS:")
    print("->", end=" ")
    for point in dfs_path:
        print(point, end=" -> ")
    print()
    
    print(f"Phần A*:")
    print("->", end=" ")
    for point in astar_path:
        print(point, end=" -> ")
    print()

def main():
    grids = [
        [
            [1, 1, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        [
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 0],
            [1, 1, 1]
        ],
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 0],
            [0, 1, 1]
        ],
        [
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ],
        [
            [1, 1, 1],
            [0, 1, 0],
            [1, 1, 1],
            [1, 0, 1]
        ]
    ]

    global ROW, COL
    ROW = 4
    COL = 3

    src = [3, 0]
    dest = [0, 2]

    for i, grid in enumerate(grids, 1):
        print(f"\n===== Grid {i} =====")
        DFS_A(grid, src, dest)

if __name__ == "__main__":
    main()