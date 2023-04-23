class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)

class Line:
    def __init__(self, point1, point2):
        self.A = point1
        self.B = point2

    def __str__(self) -> str:
        return "(A{}, B{})".format(self.A, self.B)

class Rectangle:
    def __init__(self, point1, point2):
        if point1.x > point2.x:
            p11 = Point(point1.x, point2.y)
            p12 = Point(point2.x,point1.y)
        else:
            p11 = Point(point2.x,point1.y)
            p12 = Point(point1.x,point2.y)
        x = [point1.x, p11.x, p12.x, point2.x]
        y = [point1.y, p11.y, p12.y, point2.y]
        dictionary = {0: point1, 1: p11, 2: p12, 3: point2}
        sum = []
        for i in range(4):
            sum.append(x[i] + y[i])
        self.A = dictionary[sum.index(min(sum))]
        for i in range(4):
            if x[i] == min(x) and y[i] != min(x):
                self.B = dictionary[i]
            if x[i] != min(x) and y[i] != min(y):
                self.C = dictionary[i]
            if x[i] != min(x) and y[i] == min(y):
                self.D = dictionary[i]

    def __str__(self) -> str:
        return "(A{}, B{}, C{}, D{})".format(self.A, self.B, self.C, self.D)

def get_common_part(r1, r2):
    if r1.A.x > r2.C.x or r1.A.y > r2.C.y or r1.C.x < r2.A.x or r1.C.y < r2.A.y:
        return 'Brak wspólnej części'
    bl = Point(max(r1.A.x, r2.A.x), max(r1.A.y, r2.A.y))
    tr = Point(min(r1.C.x, r2.C.x), min(r1.C.y, r2.C.y))

    if bl == tr:
        return bl

    if bl.x == tr.x or bl.y == tr.y:
        return Line(bl, tr)

    return Rectangle(bl, tr)

if __name__ == '__main__':
    r1 = Rectangle(Point(0, 10), Point(5, 8))
    r2 = Rectangle(Point(3, 3), Point(10, 10))
    print('Częścią wspólną podanych prostokątów jest figura o danych współrzędnych:')
    print(get_common_part(r1, r2))