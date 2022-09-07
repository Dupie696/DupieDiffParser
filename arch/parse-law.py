import re


text = open("law.txt", "r").read()
 

import re

"""CORTE SUPREMA DE JUSTICIA
EXAMEN DE NOTARIADO 2021
Cuestionario Jornada 1: 
Sábado 4 de diciembre de 9:20 a.m. a 11:00 a.m.
Página 1 de 32"""

x = """CORTE SUPREMA DE JUSTICIA
EXAMEN DE NOTARIADO 2021
Cuestionario Jornada \d: 
Sábado 4 de diciembre de 9:20 a.m. a 11:00 a.m.
Página \d+ de \d+
(Nota: El color verde indica que la opción es la correcta, el color rojo indica que la opción es incorrecta.
PREGUNTAS
RESPUESTA 
CORRECTA)
""".replace("\n","\\n")



x = """CORTE SUPREMA DE JUSTICIA
EXAMEN DE NOTARIADO 2021
Cuestionario Jornada \d: 
Sábado 4 de diciembre de 9:20 a.m. a 11:00 a.m.
Página \d+ de \d+
(Nota: El color verde indica que la opción es la correcta, el color rojo indica que la opción es incorrecta.
PREGUNTAS
RESPUESTA 
CORRECTA)?""".replace("\n","\\n")
res_str = re.sub(x, "", text)

if res_str[0:1] == "\n":
    res_str = res_str[1:]
    print ("yeah, it's bklank1")
# String after replacement
print(res_str[:1000])
#print(res_str)
myindex=0
for z in res_str.split("\n")[:10]:
    myindex +=1
    # print (z)
    # print ()
    # print (z[-2:])

    print ("%s:%s -- %s" % (myindex,z[-2:],z)) 

myindex = 0
questionStart = 0
answer_count = 0
answerEnd = []

while answer_count < 4:

    z = res_str.split("\n")[:10][myindex]

    if z[-2:] == "Si" or z[-2:] == "No":
        print (myindex+1)
        answer_count +=1

    myindex+=1
  


text2 = open("law3.txt", "r").read()

a= (res_str.split("\n")[:10][1])
b= (res_str.split("\n")[:10][2])
c= (res_str.split("\n")[:10][3])

print (a)
print (b)
print (c)
print(text2.find("%s%s" % (a,b[:-4])))
print(text2.find("%s%s" % (b,c[:-4])))