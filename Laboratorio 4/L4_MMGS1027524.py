#Lista de precios, mostrar menor y mayor 
lista= [50,75,46,22,80,65,8]
def mayor(lista):
    mayor = lista[0]
    for lista in lista:
        if lista> mayor: 
            mayor= lista
    return mayor

def menor(lista):
    menor = lista[0]
    for lista in lista:
        if lista< menor: 
            menor= lista           
    return menor

mayor_lista=mayor(lista)
menor_lista=menor(lista)

print("El mayor precio es:", mayor_lista)
print("El menor precio es:", menor_lista)

#Lista abecedario y elimina multiplos de 3
def abecedario():
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    resultado = [letra for i, letra in enumerate(lista) if (i + 1) % 3 != 0]  
    return resultado
print(abecedario())


#Lista de palabras
lista_palabras=["lapiz", "tijera", "crayon", "lapicero", "cuaderno", "libro", "computadora", "mochila"]
palabra_buscada=input("Introduce que palabra que deseas buscar:")
conteo= lista_palabras.count(palabra_buscada)
print("La palabra buscada",palabra_buscada, "aparece", conteo, "veces en la lista.")

#Pares e impares 
import random
vector = [random.randint(1, 10) for _ in range(100)]

pares = [num for num in vector if num % 2 == 0]
impares = [num for num in vector if num % 2 != 0]

print("Numeros pares:", pares)
print("Numeros impares:", impares)
