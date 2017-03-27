import sys
def f(point):
    return 3*point + 2

def false_position(lo, hi, tolerance=0.001):
    k = 1
    c = 1
    while abs(f(c)) >= tolerance:
        c = (lo * f(hi) - hi * f(lo)) / (f(hi) - f(lo))
        if(f(lo) * f(c) <= 0):
            hi = c
        else:
            lo = c
        k = k + 1

    return k, c

def main():
    left, right = list(map(int, sys.argv[1:3]))
    if len(sys.argv) == 4:
        tolerance = float(sys.argv[-1])
        n, solution = false_position(left, right, tolerance)
    else:
        n, solution = false_position(left, right)
    n = 2
    print ("After " + str(n) + " iterations, solution"+ str(solution) + " was found\n")

if __name__ == '__main__':
    main()
