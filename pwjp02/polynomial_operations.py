class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)

    def __add__(self, poly):
        new_coef = []
        poly1 = self.coefficients.copy()
        poly2 = poly.coefficients.copy()
        while len(poly1) < len(poly2):
            poly1.insert(0,0)
        while len(poly1) > len(poly2):
            poly2.insert(0,0)
        for i in range(len(poly1)):
            new_coef.append(poly1[i] + poly2[i])
        return Polynomial(*new_coef)

    def __sub__(self, poly):
        new_coef = []
        poly1 = self.coefficients.copy()
        poly2 = poly.coefficients.copy()
        while len(poly1) < len(poly2):
            poly1.insert(0, 0)
        while len(poly1) > len(poly2):
            poly2.insert(0, 0)
        for i in range(len(poly1)):
            new_coef.append(poly1[i] - poly2[i])
        return Polynomial(*new_coef)

    def __mul__(self, poly):
        poly1 = self.coefficients.copy()
        poly2 = poly.coefficients.copy()
        new_coef = [0 for i in range(len(poly1) + len(poly2))]
        while len(poly1) < len(poly2):
            poly1.insert(0, 0)
        while len(poly1) > len(poly2):
            poly2.insert(0, 0)
        for i in range(len(poly1)):
            for j in range(len(poly2)):
                if poly1[i] != 0 and poly2[j] != 0:
                    new_coef[len(new_coef) - (i + j) - 1] += poly1[i] * poly2[j]
        return Polynomial(*new_coef)



if __name__ == '__main__':
    p1 = Polynomial(1, 1, 0, 0)
    p2 = Polynomial(2)
    print('Wynikiem dodawania jest wielomian o następujących współczynnikach:')
    print((p1 + p2).coefficients)
    print('Wynikiem odejmowania jest wielomian o następujących współczynnikach:')
    print((p1 - p2).coefficients)
    print('Wynikiem mnożenia jest wielomian o następujących współczynnikach:')
    print((p1 * p2).coefficients)