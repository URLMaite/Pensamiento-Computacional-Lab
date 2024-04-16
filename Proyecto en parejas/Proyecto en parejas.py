def calcular_distancia(partida, destino):
    if partida == "51" and destino == "61":
        return 39
    elif partida == "51" and destino == "71":
        return 18
    elif partida == "71" and destino == "82":
        return 23
    elif partida == "61" and destino == "51":
        return 8
    elif partida == "82" and destino == "51":
        return 42
    else:
        return None

def calcular_costo_viaje(distancia):
    if distancia is None:
        return 0
    
    precio_base = 1.50 
    precio_adicional = 0.25  
    
    if distancia <= 8:
        costo_total = distancia * precio_base
    else:
        costo_total = 8 * precio_base + (distancia - 8) * precio_adicional
    
    return costo_total

# Estaciones disponibles
E1 = "Estacion Javier (código 51)"
E2 = "Estacion Trebol (código 61)"
E3 = "Estacion Don Bosco (código 71)"
E4 = "Estacion Plaza Municipal (código 82)"

# Rutas Disponibles
R1 = "Estacion Javier a Estacion Trebol"
R2 = "Estacion Javier a Estacion Don Bosco"
R3 = "Estacion Don Bosco a Estacion Plaza Municipal"
R4 = "Estacion Trebol a Estacion Javier"
R5 = "Estacion Plaza Municipal a Estacion Javier"

# Diccionario para mantener un registro de las compras de todos los usuarios
registro_compras = {}

while True:
    print("1. Comprar boleto")
    print("2. Ver reportes")
    print("3. Salir del programa")
    
    opcion = input("Seleccione una opción, ya sea 1, 2 o 3: ")
    while opcion not in ["1", "2", "3"]:
        opcion = input("Por favor, responda con '1', '2' o '3': ")

    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        print("Compra tu boleto")
        print("Estaciones disponibles")
        print(E1, E2, E3, E4)
        print("Rutas disponibles")
        print(R1, R2, R3, R4, R5)

        print("Hola", nombre, "escoja las estaciones de la ruta que tomará hoy")
        partida = input("Ingrese número de estación de partida: ")
        while partida not in ["51", "61", "71", "82"]:
            partida = input("Por favor, responda con '51', '61', '71' o '82': ")

        destino = input("Ingrese número de estación de destino: ")
        while destino not in ["51", "61", "71", "82"]:
            destino = input("Por favor, responda con '51', '61', '71' o '82': ")

        ruta = f"Estacion {partida} a Estacion {destino}"
        
        if nombre in registro_compras:
            registro_compras[nombre].append(ruta)
        else:
            registro_compras[nombre] = [ruta]

        embarazada = input("¿Está embarazada? (sí/no): ").lower()
        
        if embarazada == "sí" or embarazada == "si":
            print("Su boleto es gratis, disfrute su viaje")
            costo_total_viaje = 0
        else:
            edad = int(input("Ingrese su edad: "))
            distancia_del_viaje = calcular_distancia(partida, destino)
            if distancia_del_viaje is not None:
                costo_total_viaje = calcular_costo_viaje(distancia_del_viaje)
                if 15 <= edad <= 25:
                    costo_total_viaje *= 0.75
                    print("Usted recibirá un 25% de descuento en el precio total del boleto.")
            else:
                costo_total_viaje = 0

        if costo_total_viaje > 0:
            print("El costo total del viaje es: Q", round(costo_total_viaje, 2))
            print("Para procesar su pago recuerde que solo aceptamos tarjetas de crédito o débito")
            print("Inserte su tarjeta")
            print("Transacción exitosa")
        
        print("Gracias por su compra, que tenga un buen viaje!")
    
    elif opcion == "2":
        print("Reportes:")
        print("Cantidad de boletos vendidos por ruta:")
        for ruta in [R1, R2, R3, R4, R5]:
            partida = ruta.split(" ")[1]
            destino_nombre = ruta.split(" ")[-2] + " " + ruta.split(" ")[-1]
            ruta_completa = f"Estacion {partida} a {destino_nombre}"
            
            cantidad_boletos = sum(ruta_completa in rutas for rutas in registro_compras.values())
            partida_codigo = partida.split(" ")[-1].strip("(código").strip(")")
            destino_codigo = destino_nombre.split(" ")[-1].strip("(código").strip(")")
            distancia = calcular_distancia(partida_codigo, destino_codigo)
            dinero_recaudado = cantidad_boletos * calcular_costo_viaje(distancia)
            print(f"{ruta}: {cantidad_boletos} boletos, Dinero recaudado: Q{dinero_recaudado:.2f}")

        total_dinero = sum(sum(calcular_costo_viaje(calcular_distancia(
                        ruta.split(" ")[1].split(" ")[-1].strip("(código").strip(")"),
                        ruta.split(" ")[-2] + " " + ruta.split(" ")[-1].split(" ")[-1].strip("(código").strip(")")))
                        for ruta in usuario)
                        for usuario in registro_compras.values())
        print("Total de dinero percibido por la venta de boletos: Q", round(total_dinero, 2))

    elif opcion == "3":
        print("Saliendo del programa.")
        break