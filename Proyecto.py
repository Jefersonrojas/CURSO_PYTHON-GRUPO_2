import json
import os
from datetime import datetime

class AsistenteFinanzasPersonales:
    def __init__(self):
        self.archivo_datos = "datos_financieros.json"
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        """Cargar datos financieros desde un archivo JSON o inicializar un nuevo conjunto de datos."""
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'r') as archivo:
                return json.load(archivo)
        else:
            return {"ingresos": [], "gastos": [], "ahorros": 0}

    def guardar_datos(self):
        """Guardar datos financieros en un archivo JSON."""
        with open(self.archivo_datos, 'w') as archivo:
            json.dump(self.datos, archivo, indent=4)

    def agregar_ingreso(self, monto, fuente):
        """Agregar un registro de ingreso."""
        registro = {
            "monto": monto,
            "fuente": fuente,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.datos["ingresos"].append(registro)
        self.datos["ahorros"] += monto
        self.guardar_datos()
        print(f"Ingreso de {monto} desde {fuente} agregado exitosamente!")

    def agregar_gasto(self, monto, categoria):
        """Agregar un registro de gasto."""
        registro = {
            "monto": monto,
            "categoria": categoria,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.datos["gastos"].append(registro)
        self.datos["ahorros"] -= monto
        self.guardar_datos()
        print(f"Gasto de {monto} en {categoria} agregado exitosamente!")

    def ver_resumen(self):
        """Ver un resumen de ingresos, gastos y ahorros."""
        print("\nResumen Financiero:")
        print("====================")
        print(f"Total de Ingresos: {sum(item['monto'] for item in self.datos['ingresos'])}")
        print(f"Total de Gastos: {sum(item['monto'] for item in self.datos['gastos'])}")
        print(f"Ahorros: {self.datos['ahorros']}")

    def ver_detalles(self):
        """Ver detalles de las transacciones."""
        print("\nDetalles de Ingresos:")
        print("=====================")
        for registro in self.datos["ingresos"]:
            print(f"Fecha: {registro['fecha']}, Monto: {registro['monto']}, Fuente: {registro['fuente']}")

        print("\nDetalles de Gastos:")
        print("===================")
        for registro in self.datos["gastos"]:
            print(f"Fecha: {registro['fecha']}, Monto: {registro['monto']}, Categoría: {registro['categoria']}")

    def ejecutar(self):
        """Ejecutar el bucle principal del asistente financiero."""
        while True:
            print("\nAsistente de Finanzas Personales")
            print("================================")
            print("1. Agregar Ingreso")
            print("2. Agregar Gasto")
            print("3. Ver Resumen")
            print("4. Ver Detalles")
            print("5. Salir")

            opcion = input("Elige una opción: ")

            if opcion == '1':
                monto = float(input("Ingresa el monto del ingreso: "))
                fuente = input("Ingresa la fuente del ingreso: ")
                self.agregar_ingreso(monto, fuente)
            elif opcion == '2':
                monto = float(input("Ingresa el monto del gasto: "))
                categoria = input("Ingresa la categoría del gasto: ")
                self.agregar_gasto(monto, categoria)
            elif opcion == '3':
                self.ver_resumen()
            elif opcion == '4':
                self.ver_detalles()
            elif opcion == '5':
                print("¡Adiós!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    asistente = AsistenteFinanzasPersonales()
    asistente.ejecutar()
