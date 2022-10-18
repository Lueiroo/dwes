#FUNCIONES
def respuesta():
    r = input("¿Cúal es tu respuesta?")
    return r


print ("")
print ("********** CONCURSO **********")
print ("")

print ("-------------------------------------------------------------------------------------------")
print ("¿Cuál es objetivamente (siendo yo el baremo) la mejor canción del nuevo álbum del Ferxxo?")
print ("-------------------------------------------------------------------------------------------")
print ("")

print ("Respuestas posibles: ")
print ("A) Lady mi amor.")
print ("B) Nieve.")
print ("C) Si te la encuentras por ahí.")
print ("")

r = respuesta()
re = r.upper()
while (re != 'A' and re != 'B' and re != 'C'):
    print("Solamente se aceptan como respuesta 'A', 'B' o 'C'. Inténtelo de nuevo.")
    print ("")
    r = respuesta()
    re = r.upper()

print ("")
if re == 'B':
    print("Oleeeeee esa era")
else:
    print ("Mecachis esa no era")