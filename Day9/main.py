def read_file(file_path) -> list[tuple[int, int]]:
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                x, y = map(int, line.strip().split(','))
                points.append((x, y))
    return points

def get_area(p1: tuple, p2: tuple) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def is_point_inside(p: tuple, polygon: list[tuple]) -> bool:
    x, y = p
    n = len(polygon)
    
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        if p1[0] == p2[0] and p1[0] == x:
            if min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]):
                return True
        if p1[1] == p2[1] and p1[1] == y:
             if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]):
                return True

    inside = False
    for i in range(n):
        p1x, p1y = polygon[i]
        p2x, p2y = polygon[(i + 1) % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    inside = not inside

    return inside

def rect_crosses_polygon(r1: tuple, r2: tuple, polygon: list[tuple]) -> bool:
    rx_min, rx_max = min(r1[0], r2[0]), max(r1[0], r2[0])
    ry_min, ry_max = min(r1[1], r2[1]), max(r1[1], r2[1])
    
    n = len(polygon)
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        
        if p1[0] == p2[0]:
            edge_x = p1[0]
            if rx_min < edge_x < rx_max:
                edge_y_min, edge_y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
                if max(ry_min, edge_y_min) < min(ry_max, edge_y_max):
                    return True
                    
        elif p1[1] == p2[1]:
            edge_y = p1[1]
            if ry_min < edge_y < ry_max:
                edge_x_min, edge_x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
                if max(rx_min, edge_x_min) < min(rx_max, edge_x_max):
                    return True

    return False

def main():
    points = read_file('./input.txt')
    n = len(points)
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue
            
            c1, c2 = (p2[0], p1[1]), (p1[0], p2[1])
            
            if not is_point_inside(c1, points) or not is_point_inside(c2, points):
                continue

            if rect_crosses_polygon(p1, p2, points):
                continue
                
            max_area = max(max_area, get_area(p1, p2))

    print(max_area)

if __name__ == "__main__":
    main()
