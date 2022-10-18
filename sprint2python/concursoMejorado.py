#FUNCIONES
def respuesta():
    r = input("¿Cúal es tu respuesta?")
    re = r.upper()
    while (re != 'A' and re != 'B' and re != 'C'):
        print("Solamente se aceptan como respuesta 'A', 'B' o 'C'. Inténtelo de nuevo.")
        print ("")
        r = input("¿Cúal es tu respuesta?")
        re = r.upper()
    return re


#MAIN
puntuacion = 0

print ("")
print ("********** CONCURSO **********")
print ("")

print ("-------------------------------------------------------------------------------------------")
print ("PRIMERA PREGUNTA")
print ("¿Cuál es objetivamente (siendo yo el baremo) la mejor canción del nuevo álbum del Ferxxo?")
print ("-------------------------------------------------------------------------------------------")
print ("")

print ("Respuestas posibles: ")
print ("A) Lady mi amor.")
print ("B) Nieve.")
print ("C) Si te la encuentras por ahí.")
print ("")

r = respuesta()

print ("")
if r == 'B':
    print("Oleeeeee esa era +5 puntos para ti!")
    puntuacion += 5
else:
    print ("Mecachis esa no era")


print ("-------------------------------------------------------------------------------------------")
print ("SEGUNDA PREGUNTA")
print ("¿Cuál es la mejor parte de 'Cayó la noche REMIX'?")
print ("-------------------------------------------------------------------------------------------")
print ("")

print ("Respuestas posibles: ")
print ("A) La de Quevedo.")
print ("B) La de Bejo.")
print ("C) La de Cruz Cafuné.")
print ("")

r = respuesta()

print ("")
if r == 'A':
    print("Oleeeeee esa era +5 puntos para ti!")
    puntuacion += 5
else:
    print ("Mecachis esa no era")

print ("-------------------------------------------------------------------------------------------")
print ("TERCERA PREGUNTA")
print ("¿Cuál es la última canción que escucho Iago Morales el 18/10/2022 a las 14:11?")
print ("-------------------------------------------------------------------------------------------")
print ("")

print ("Respuestas posibles: ")
print ("A) Cerebros destruidos de Escorbuto.")
print ("B) Toxic de Britney Spears.")
print ("C) Legalización de SKA-P.")
print ("")

r = respuesta()

print ("")
if r == 'A':
    print("Oleeeeee esa era +5 puntos para ti!")
    puntuacion += 5
else:
    print ("Mecachis esa no era")

print ("")
print ("El resultado final es de " + str(puntuacion))
