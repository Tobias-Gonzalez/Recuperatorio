# # ejercicio 1-A
if(pers1[1] > pers2[1]):
    print(pers1[0],'ES ALTO')
else:
    print(pers2[0],'ES AlTO')

# B
if (pers1[2] > pers2[2]):
    print (pers1[0], 'ES PESADO')
else:
    print(pers2[0], 'ES PESADO ')

# C
if (pers1[4] > pers2[4]):
    print (pers1[0], "PARTICIPO EN MAS PELICULAS")
elif(peso1[4] == pers2[4]):
    print ("PARTICIPARON LAS MISMAS VECES")
else:
    print(pers2[0], "PERTICIPO EN MAS PELICULAS ")

# D
if(personaje1 =="Yoda" or personaje1 == "Grevious"):
    print('personaje 1', personaje1['name'])
if(personaje2 == "Yoda" or personaje2 == "Grevious"):
    print('personaje 2', personaje2['name'])

def nombre(item):
    return item['name']



# # ejercicio 2
import json
import requests

def pornombre(item):
    return item["name"]

def get_data(ruta):
    req = requests.get(ruta)
    if req.status_code == 200:
        dic= json.loads(req.text)
        return dic

def get_data_sw_characters():
    sw_data = []
    result = get_data("https://swapi.dev/api/people/")
    while(result["next"] is not None):
        for doc in result["results"]:
            sw_data.append(doc)
        result = get_data(result["next"])
    return sw_data

sw_data = get_data_sw_characters()

sw_data.sort(key=pornombre)

print("Respuesta 2.A")
for character in sw_data:
    print(character["name"], character["height"], "cm", len(character["films"]), "peliculas")
print("")
print("")
print("Respuesta 2.B")
for character in sw_data:
    if character["name"].startswith("D" or "C") or character["name"].endswith("s"):




# ejercicio 3
from random import randint

lista100 = []
lista001 = lista100

for i in range (0,100):
    numero = randint(0,100)
    lista100.append(numero)
print("La lista generada es:")
print(lista100)

lista100.sort()

print("Ejercicio 3.A")
print("Rango de valores: ", lista100[0], lista100[99])
print("La diferencia entre el mayor y el menor es: ", lista100[0] - lista100[99])

print("Ejercicio 3.B")
print(sum(lista100) / 100)

print ("Ejercicio 3.C")
print("Lista en orden creciente: ", lista100)

lista001.sort(reverse=True)

print("Ejercicio 3.D")
print("Lista en orden decreciente: ", lista001)

print("Ejercicio 3.E")
for num in lista100:
    if(num % 3 > 0 and num % 2 > 0):
        print(num)