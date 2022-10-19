
from factorial import func_factorial
from factorial2 import func_factorial_no_recursiva

n = (input("Introduzca un número: "))

print ("El factorial del número introducido calculado de forma recursiva es: " + str(func_factorial(int(n))))
print ("")

print ("El factorial del número introducido calculado de forma no recursiva es: " + str(func_factorial_no_recursiva(int(n))))
print ("")