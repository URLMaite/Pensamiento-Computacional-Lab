#Ejercicio1 Nombre y saludo
print("Ejercicio 1")
nombre = input("Escriba su nombre")
print("Hola, ",nombre)

#Ejercicio2 Nombre y edad
print("Ejercicio 2")
nombre=input("Escriba su nombre")
edad=input("Escriba su edad")
print("Hola ",nombre," Tienes ",edad,"años" )

#Ejercicio 3 Celsius a Fahrenheit
print("Ejercicio 3")
celsius=int(input("Ingresa la temperatura en grados celsius"))
formula=((celsius*9)/5)+32
print("La temperatura en Fahrenheit es de",formula)

#Ejercicio 4 Operaciones basicas
print("Ejercicio 4")
numero1=int(input("Ingrese un numero"))
numero2=int(input("Ingrese otro numero"))
suma=(numero1+numero2)
resta=(numero1-numero2)
multiplicacion=(numero1*numero2)
division=(numero1/numero2)
print("La suma de los numeros es ",suma)
print("La resta de los numeros es ",resta)
print("La multiplicacion de los numeros es ",multiplicacion)
print("La division de los numeros es ",division)

#Ejercicio 5 area de un triangulo 
print("Ejercicio 5")
altura=int(input("Ingrese la altura de su traingulo"))
base=int(input("Ingrese la base de su triangulo"))
print("El area del triangulo es de")
area=int(input((base*altura)/2))