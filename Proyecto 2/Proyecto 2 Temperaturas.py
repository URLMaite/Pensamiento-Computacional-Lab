#Importar dataframe y time
import datetime
import time

# Definir la clase Zona
class Zona:
    def __init__(self, nombre, temp_deseada):
        self.nombre = nombre
        self.temp_deseada = temp_deseada
        self.temp_actual = 21  # Temperatura inicial por defecto
        self.horarios = []

# Definir el sistema de control 
class SistemaControlTemperatura:
    def __init__(self):
        self.zonas = {}
        self.historial = []

    # Agregar zonas
    def agregar_zona(self):
        nombre = input("Ingrese el nombre de la zona: ")
        temp_deseada = float(input(f"Ingrese la temperatura deseada para {nombre}: "))
        self.zonas[nombre] = Zona(nombre, temp_deseada)
        print(f"Zona {nombre} con temperatura deseada de {temp_deseada}°C añadida.\n")

    # Ver zonas existentes 
    def ver_zonas(self):
        if not self.zonas:
            print("No hay zonas definidas.\n")
        else:
            for nombre, zona in self.zonas.items():
                print(f"Zona: {nombre}, Temperatura Deseada: {zona.temp_deseada}°C, Temperatura Actual: {zona.temp_actual}°C")
            print()

    # Ajustar temperatura 
    def ajustar_temperatura(self):
        nombre = input("Ingrese el nombre de la zona a ajustar: ")
        if nombre in self.zonas:
            temp_deseada = float(input(f"Ingrese la nueva temperatura deseada para {nombre}: "))
            self.zonas[nombre].temp_deseada = temp_deseada
            print(f"Temperatura deseada de la zona {nombre} ajustada a {temp_deseada}°C.\n")
        else:
            print(f"La zona {nombre} no existe.\n")

    # Programar horario 
    def programar_horario(self):
        nombre = input("Ingrese el nombre de la zona: ")
        if nombre in self.zonas:
            hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
            temp_deseada = float(input(f"Ingrese la temperatura deseada para {nombre} a las {hora_inicio}: "))
            self.zonas[nombre].horarios.append((hora_inicio, temp_deseada))
            print(f"Horario para la zona {nombre} programado a las {hora_inicio} con temperatura deseada de {temp_deseada}°C.\n")
        else:
            print(f"La zona {nombre} no existe.\n")

    # Monitorear temperaturas 
    def monitorear_temperaturas(self):
        while True:
            ahora = datetime.datetime.now().strftime("%H:%M")
            for zona in self.zonas.values():
                temp_actual = zona.temp_actual
                temp_deseada = zona.temp_deseada
                for horario, temp in zona.horarios:
                    if ahora == horario:
                        temp_deseada = temp
                if temp_actual < temp_deseada:
                    zona.temp_actual += 1  # Simulación de aumento de temperatura
                elif temp_actual > temp_deseada:
                    zona.temp_actual -= 1  # Simulación de disminución de temperatura
                self.historial.append((zona.nombre, ahora, zona.temp_actual))
                print(f"Zona: {zona.nombre}, Hora: {ahora}, Temp Actual: {zona.temp_actual}°C, Temp Deseada: {temp_deseada}°C")
            time.sleep(60)  # Espera un minuto y repite 

    # Mostrar historial 
    def mostrar_historial(self):
        if not self.historial:
            print("No hay historial disponible.\n")
        else:
            for registro in self.historial:
                print(f"Zona: {registro[0]}, Hora: {registro[1]}, Temperatura: {registro[2]}°C")
            print()

    # Menu del programa 
    def iniciar(self):
        while True:
            print("1. Configurar zona")
            print("2. Ver zonas")
            print("3. Ajustar temperatura de una zona")
            print("4. Programar horario")
            print("5. Monitorear temperaturas")
            print("6. Mostrar historial")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_zona()
            elif opcion == "2":
                self.ver_zonas()
            elif opcion == "3":
                self.ajustar_temperatura()
            elif opcion == "4":
                self.programar_horario()
            elif opcion == "5":
                print("Iniciando monitoreo de temperaturas (Ctrl+C para detener)...")
                try:
                    self.monitorear_temperaturas()
                except KeyboardInterrupt:
                    print("\nMonitoreo detenido.\n")
            elif opcion == "6":
                self.mostrar_historial()
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.\n")

# Se crea una instancia del sistema y se inicia 
if __name__ == "__main__":
    sistema = SistemaControlTemperatura()
    sistema.iniciar()
