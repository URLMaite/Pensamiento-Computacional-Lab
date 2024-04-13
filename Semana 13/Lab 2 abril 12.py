# Función para contar números pares e impares dentro de un rango
def contar_pares_impares(numero):
    pares = 0
    impares = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

# 1. Solicitar al usuario un número entero positivo y contar la cantidad de pares e impares
numero = int(input("Ingrese un número entero positivo: "))
if numero <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    cantidad_pares, cantidad_impares = contar_pares_impares(numero)
    print("Cantidad de números pares:", cantidad_pares)
    print("Cantidad de números impares:", cantidad_impares)

# 2. Sumar todos los números pares dentro de un rango dado por el usuario
inicio = int(input("Ingrese un número inicial: "))
fin = int(input("Ingrese un número final: "))

suma_pares = 0
for num in range(inicio, fin + 1):
    if num % 2 == 0:
        suma_pares += num

print("La suma de todos los números pares en el rango es:", suma_pares)

# 3. Mostrar la tabla de multiplicar de un número dado por el usuario
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 4. Imprimir los números del 1 al 50 con las reglas de FizzBuzz
print("FizzBuzz:")
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 5. Imprimir todos los divisores de un número ingresado por el usuario
numero = int(input("Ingrese un número: "))

print(f"Los divisores de {numero} son: ")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
