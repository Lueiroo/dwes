
from ast import If
from factorial import func_factorial
from factorial2 import func_factorial_no_recursiva
import time

def respuesta():
    print ("Desea realizar el factorial de forma recursiva ('A') o de forma no recursiva ('B'): ")
    opcion = (input("Introduzca su opción: "))
    opcion = opcion.upper()
    while(opcion != 'A' and opcion != 'B'):
        print ("")
        print ("Respuesta incorrecta, sólo se acepta 'A' o 'B' ")
        print ("")
        opcion = (input("Introduzca su opción: "))
        opcion = opcion.upper()
    return opcion

#MAIN

print ("")
n = (input("Introduzca un número: "))
print ("")

opcion = respuesta()
if (opcion == 'A'):
    print ("Elegida la opción A ('De forma recursiva')")
    print ("")
    tiempo_inicio = time.time()
    print ("El factorial del número introducido calculado de forma recursiva es: " + str(func_factorial(int(n))))
    tiempo_final = time.time()
    print ("")
    tiempo_total = tiempo_final - tiempo_inicio
    print ("El tiempo total en ejecutar la función es de: " + str(tiempo_total))

else:
    print ("Elegida la opción B ('De forma no recursiva')")
    print ("")
    tiempo_inicio = time.time()
    print ("El factorial del número introducido calculado de forma no recursiva es: " + str(func_factorial_no_recursiva(int(n))))
    tiempo_final = time.time()
    print ("")
    tiempo_total = tiempo_final - tiempo_inicio
    print ("El tiempo total en ejecutar la función es de: " + str(tiempo_total))


