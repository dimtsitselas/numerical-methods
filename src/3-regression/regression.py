from sympy import Matrix, ones

def regression(n, points, values):
    """Finds the n degree polynomial being closest to the given points.
    
    Args:
        n (int): degree of regression polynomial
        points (list): m x-axis coordinates
        values (list): m y-axis coordinates
    """
    m = len(points)

    a = []
    for i in range(m):
        for j in range(n+1):
            a.append(points[i]**j)
    
    A = Matrix(m, n+1, a)
    B = Matrix(m, 1, values)

    x = ((A.T*A).inv()*A.T*B)  # regression coefficients

    return [x[i, 0] for i in range(n+1)]

if __name__ == "__main__":
    n = int(input("Enter regression polynomial degree: "))
    points = [float(x) for x in input("Enter x coordinates: ").split(" ")]
    values = [float(x) for x in input("Enter y coordinates: ").split(" ")]

    coeff = regression(n, points, values)

    if coeff[1] > 0:
        poly = str(coeff[0]) + ' + ' + str(coeff[1]) + '*x'
    elif coeff[1] < 0:
        poly = str(coeff[0]) + ' - ' + str(-coeff[1]) + '*x'
    for i in range(2, n+1):
        if coeff[i] > 0:
            poly += ' + ' + str(coeff[i]) + '*x**' + str(i)
        elif coeff[i] < 0:
            poly += ' - ' + str(-coeff[i]) + '*x**' + str(i)

    print(poly)
