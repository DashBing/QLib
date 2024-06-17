import sympy
import sympy.vector

class QBit:
    def __init__(self, low_bit:float|sympy.Rational=1, high_bit:float|sympy.Rational=0):
        self.low_bit = low_bit
        self.high_bit = high_bit
    def __repr__(self) -> str:
        return(repr(self.matrix).replace("Matrix", "QBit"))
    def __str__(self) -> str:
        return(str(self.matrix).replace("Matrix", "QBit"))
    @property
    def matrix(self) -> sympy.Matrix:
        return(sympy.Matrix([self.low_bit, self.high_bit]))

def matrix_mul_vector(matrix:sympy.Matrix, vector:sympy.Matrix):
    k = sympy.symbols("k")
    return(sympy.Matrix([sympy.summation(matrix[i,k]*vector[k,0], (k, 0, vector.shape[0]-1)) for i in range(matrix.shape[0])]))

def X_door(input:QBit) -> QBit:
    tmp = matrix_mul_vector(sympy.Matrix([[0, 1], [1, 0]]), input.matrix)
    return(QBit(tmp[0, 0], tmp[1, 0]))

def Y_door(input:QBit) -> QBit:
    tmp = matrix_mul_vector(sympy.Matrix([[0, -sympy.I], [sympy.I, 0]]), input.matrix)
    return(QBit(tmp[0, 0], tmp[1, 0]))

def Z_door(input:QBit) -> QBit:
    tmp = matrix_mul_vector(sympy.Matrix([[1, 0], [0, -1]]), input.matrix)
    return(QBit(tmp[0, 0], tmp[1, 0]))

def H_door(input:QBit) -> QBit:
    tmp = sympy.sqrt(2)**(-1) * matrix_mul_vector(sympy.Matrix([[1, 1], [1, -1]]), input.matrix)
    return(QBit(tmp[0, 0], tmp[1, 0]))

if __name__ == "__main__":
    print(sympy.expand_func(matrix_mul_vector(sympy.Matrix([[2,3],[1,-5]]), sympy.Matrix([[4],[1]]))))
    print(X_door(QBit(1,0)))
    print(H_door(QBit(1,0)))
