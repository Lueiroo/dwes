#FUNCIONES
def func_factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * func_factorial(num-1)

print ("")
n = (input("Introduzca un número: "))

print ("El factorial del número introducido es: " + str(func_factorial(int(n))))
print ("")