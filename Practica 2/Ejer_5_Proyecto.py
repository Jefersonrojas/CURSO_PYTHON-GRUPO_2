from enum import Enum
from datetime import datetime

import uuid
'''
INIT    Data
'''
class EstadoLibro(Enum):
    ALQUILADO = 1
    LIBRE = 2


class libroModel:
    def __init__(self, id, titulo, categoria, precio, estado):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.precio = precio
        self.estado = estado
    
    def __repr__(self):
        return f"""
    id={self.id},
    titulo='{self.titulo}',
    categoria={self.categoria},
    precio={self.precio},
    estado={self.estado})"""
    
    
class AlquilerModel:
    def __init__(self, cliente, total, fecha, idlibro):
        self.id = uuid.uuid4().hex
        self.cliente = cliente
        self.total = total
        self.fecha = fecha
        self.idlibro = idlibro
        self.devuelto = False

alquileres = []
libros = []

libros.append(libroModel('1','Harry Potter piedra filosofal','Misterio',110, EstadoLibro.LIBRE.name))
libros.append(libroModel('2','Harry Potter y el live del profe','Misterio',110, EstadoLibro.LIBRE.name))
libros.append(libroModel('3','Harry Potter y el baneo del live','Misterio',110, EstadoLibro.LIBRE.name))
libros.append(libroModel('4','Harry Potter y sorteo de libros digitales','Misterio',110, EstadoLibro.LIBRE.name))

'''
END    Data
'''

exit = False

def buscar_libro_por_titulo(libros, titulo):
    for libro in libros:
        if libro.titulo.lower() == titulo.lower():
            return libro
    return None

def buscar_libro_por_id(libros, id):
    for libro in libros:
        if libro.id.lower() == id.lower():
            return libro
    return None

def buscar_alquiler_por_id(id):
    for alquiler in alquileres:
        if alquiler.id.lower() == id.lower():
            return alquiler


def Agregar_libro(libros):
    print("\n--- Agregar Nuevo Libro ---")
    try:
        id = int(input("Ingrese el ID del libro: "))
        titulo = input("Ingrese el título del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        precio = float(input("Ingrese el precio del libro: "))
        estado = input("Ingrese el estado del libro (LIBRE/OCUPADO): ").upper()
        # Crear una nueva instancia del libro y agregarla a la lista
        libroEncontrado = buscar_libro_por_titulo(libros, titulo)
        if libroEncontrado:
            print("Libro con el mismo titulo ya existe")
            return 
        nuevo_libro = libroModel(id, titulo, categoria, precio, estado)
        libros.append(nuevo_libro)
        print("¡Libro agregado con éxito!")
    except ValueError as e:
        print(f"Error: Entrada inválida. {e}")
                    
def Mostrar_libro(libros):
    print("\n--- Lista de Libros ---")
    print(f"{'ID':<5} {'Título':<40} {'Categoría':<15} {'Precio':<10} {'Estado':<10}")
    print("-" * 75)
    for libro in libros:
        print(f"{libro.id:<5} {libro.titulo:<40} {libro.categoria:<15} {libro.precio:<10.2f} {libro.estado:<10}")
    return None

def mostrarAlquileres():
    print("\n--- Lista de Alquileres ---")
    print(f"{'ID':<30} {'Fecha':<40} {'Cliente':<15} {'Total':<10}")
    print("-" * 75)
    for alquiler in alquileres:
        print(f"{alquiler.id:<30} {alquiler.fecha:<40} {alquiler.cliente:<15} {alquiler.total:<10.2f}")
        print(f"{'ID':<5} {'Título':<40} {'Categoría':<15} {'Precio':<10} {'Estado':<10}")
        print("-" * 75)
        libro = buscar_libro_por_id(libros, alquiler.idlibro)
        print(f"{libro.id:<5} {libro.titulo:<40} {libro.categoria:<15} {libro.precio:<10.2f} {libro.estado:<10}")
    print("-" * 75)
    print("\n\r")
    
    
    return None


def alquilarLibro():
    inputID = input("Ingrese el código del libro a alquilar: ")
            
    libro = buscar_libro_por_id(libros, inputID)
            
    cliente = input("Ingrese el nombre del cliente: ")
    total = libro.precio
    fecha = datetime.now().strftime("%d/%m/%Y")
    
    alquiler = AlquilerModel(cliente, total, fecha, libro.id)
    alquileres.append(alquiler)
    
    print("") 
    print(f"Codigo de Boleta: {alquiler.id}") 
    print(f"fecha:{alquiler.fecha:<20}\n\rCliente:{alquiler.cliente}")
    print(f"{'ID':<5} {'Título':<40} {'Categoría':<15} {'Precio':<10}")
    print(f"{libro.id:<5} {libro.titulo:<40} {libro.categoria:<15} {libro.precio:<10.2f}")
    print(f"Total:{alquiler.total:<20}")
    actualizar_estado_por_id(libros, inputID, EstadoLibro.ALQUILADO.name)
            
    print(f"Libro alquilado, Se guardo correctamente")

def devolucionLibro():
    print("Devolución de libro")
    inputID = input("Ingrese el código de boleta a alquilar: ")
    alquiler = buscar_alquiler_por_id(inputID)
    if alquiler:
        alquiler.devuelto = True
    
    libro = buscar_libro_por_id(libros, alquiler.idlibro)
    actualizar_estado_por_id(libros, libro.id, EstadoLibro.LIBRE.name)
    print(f"Libro devuelto, Se guardo correctamente")

def actualizar_estado_por_titulo(libros, titulo, nuevo_precio):
    producto = buscar_libro_por_titulo(libros, titulo)
    if producto:
        producto.precio = nuevo_precio
        return True
    return False

def actualizar_estado_por_id(libros, id, estado):
    libro = buscar_libro_por_id(libros, id)
    if libro:
        libro.estado = estado
        
        return True
    return False




def volverAlMenu():
    cliclo = True
    while cliclo:
        print("\n\r")
        inResponse = input("Desea volver al menu principal [S] si, [N] no :")
        if(inResponse.lower() == "s"):
            cliclo = False
            return True
        elif(inResponse.lower() == "n"):
            cliclo = False
            return False
        else:
            ciclo = True
            




print("Bienvenido al sistema de Biblioteca \n\r")
while True:
    title = """
    Elija la opcion a realizar: 
    1: Buscar 
    2: Alquilar 
    3: Liberar 
    4: Mostrar Libros
    5: Agregar Libros 
    6: Mostrar Alquileres"""

    print(title)

    option = int(input("Ingrese el primer número: "))

    match(option):
        case 1:
            busqueda = input("Ingrese el titulo o id del libro: ")
            resultado = buscar_libro_por_titulo(libros, busqueda) or buscar_libro_por_id(libros,busqueda)
            # resultado = [libro for libro in libros if libro["titulo"].lower() == busqueda.lower()]            
            print(resultado)
            
            if(volverAlMenu() == False):
                exit = True

        case 2:
            alquilarLibro()
            if(volverAlMenu() == False):
                exit = True
        case 3:
            # inputID = input("Ingrese el código del libro: ")
            # actualizar_estado_por_id(libros, inputID, EstadoLibro.LIBRE.name)
            # print(f"Libro liberado, Se guardo correctamente")
            devolucionLibro()
            if(volverAlMenu() == False):
                exit = True
        case 4:
            Mostrar_libro(libros)           
            if(volverAlMenu() == False):
                exit = True
        case 5:
            Agregar_libro(libros)           
            if(volverAlMenu() == False):
                exit = True
        case 6:
            mostrarAlquileres()
        case 0:
            exit = True
            
            
            
            
    if(exit):
        break









