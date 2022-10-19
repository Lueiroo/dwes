#FUNCIONES
from unittest import result


def func_factorial_no_recursiva(num):
    resultado = num
    while num > 1:
        resultado = resultado * (num-1)
        num = num -1
    return resultado
