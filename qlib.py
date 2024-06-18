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
    def set_from_matrix(self, matrix:sympy.Matrix):
        self.low_bit = matrix[0, 0]
        self.high_bit = matrix[1, 0]
        return(self)
    def P(self, target:"QBit") -> float|sympy.Rational:
        return(inner_product(self, target)**2)
    def __add__(self, other:"QBit"):
        return(QBit().set_from_matrix(self.matrix + other.matrix))
    def __sub__(self, other:"QBit"):
        return(QBit().set_from_matrix(self.matrix - other.matrix))
    def __mul__(self, other:"QBit"):
        return(tensor_product(self, other))

def matrix_mul_vector(matrix:sympy.Matrix, vector:sympy.Matrix):
    k = sympy.symbols("k")
    return(sympy.Matrix([sympy.summation(matrix[i,k]*vector[k,0], (k, 0, vector.shape[0]-1)) for i in range(matrix.shape[0])]))

def inner_product(bra:QBit, ket:QBit) -> float|sympy.Rational:
    tmp = sympy.conjugate(bra.matrix.T) * ket.matrix
    return(tmp[0, 0])

def tensor_product(a:QBit, b:QBit) -> QBit:
    return(QBit().set_from_matrix(sympy.tensorproduct(a.matrix, b.matrix)))

def H_gate(input:QBit) -> QBit:
    tmp = sympy.sqrt(2)**(-1) * matrix_mul_vector(sympy.Matrix([[1, 1], [1, -1]]), input.matrix)
    return(QBit().set_from_matrix(tmp))

def X_gate(input:QBit) -> QBit:
    tmp = matrix_mul_vector(sympy.Matrix([[0, 1], [1, 0]]), input.matrix)
    return(QBit().set_from_matrix(tmp))

def Y_gate(input:QBit) -> QBit:
    tmp = matrix_mul_vector(sympy.Matrix([[0, -sympy.I], [sympy.I, 0]]), input.matrix)
    return(QBit().set_from_matrix(tmp))

def Z_gate(input:QBit) -> QBit:
    tmp = matrix_mul_vector(sympy.Matrix([[1, 0], [0, -1]]), input.matrix)
    return(QBit().set_from_matrix(tmp))

def RX_gate(input:QBit, theta:float|sympy.Rational) -> QBit:
    tmp = matrix_mul_vector(sympy.Matrix([[sympy.cos(theta/2), -sympy.I*sympy.sin(theta/2)], [-sympy.I*sympy.sin(theta/2), sympy.cos(theta/2)]]), input.matrix)
    return(QBit().set_from_matrix(tmp))

def RY_gate(input:QBit, theta:float|sympy.Rational) -> QBit:
    tmp = matrix_mul_vector(sympy.Matrix([[sympy.cos(theta/2), -sympy.sin(theta/2)], [sympy.sin(theta/2), sympy.cos(theta/2)]]), input.matrix)
    return(QBit().set_from_matrix(tmp))

def RZ_gate(input:QBit, theta:float|sympy.Rational) -> QBit:
    tmp = matrix_mul_vector(sympy.Matrix([[sympy.exp(-sympy.I*theta/2), 0], [0, sympy.exp(-sympy.I*theta/2)]]), input.matrix)
    return(QBit().set_from_matrix(tmp))
