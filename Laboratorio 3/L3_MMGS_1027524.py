#import math
import math

# Tipo de triángulo
def tipo_triangulo(a, b, c):
    if a == b == c:
        return "equilátero"
    elif a == b or a == c or b == c:
        return "isósceles"
    else:
        return "escaleno"

def funcion_triangulo():
    while True:
        lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
        lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
        lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

        tipo = tipo_triangulo(lado1, lado2, lado3)
        print("El triángulo es", tipo,)

        break

funcion_triangulo()

# Circulo
def perimetro_circulo(radio):
    return 2 * math.pi * radio

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

radio = float(input("Ingrese el radio del círculo: "))

perimetro = perimetro_circulo(radio)
print("El perímetro de la circunferencia es:", perimetro)

area = area_circulo(radio)
print("El área de la circunferencia es:", area)

volumen = volumen_esfera(radio)
print("El volumen de la esfera es:", volumen)

# Meses del año
def mes():
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    
    while True:
        numero = int(input("Ingrese un número del 1 al 12: "))
        if numero in meses:
            print("El mes número", numero, "es", meses[numero])
            break
        else:
            print("El número ingresado no es válido. Intenta otra vez")

mes()
