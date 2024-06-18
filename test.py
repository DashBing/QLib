from sympy import *
from QLib import *

def main():
    print(expand_func(matrix_mul_vector(Matrix([[2,3],[1,-5]]), Matrix([[4],[1]]))))
    print(X_gate(QBit(1,0)))
    print(H_gate(QBit(1,0)))
    print(RZ_gate(QBit(1,0),pi/4))
    print(inner_product(QBit(1, 0), QBit(1, 0)))
    print(inner_product(H_gate(QBit(1,0)), QBit(1, 0))**2)
    print(QBit(sqrt(Rational(3, 5)), sqrt(Rational(2, 5))).P(QBit(sqrt(Rational(2, 5)), sqrt(Rational(3, 5)))))

if __name__ == "__main__":
    main()
