from enum import Enum

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
    

libros = []

libros.append(libroModel('1','Harry Potter piedra filosofal','Misterio',110, EstadoLibro.LIBRE.name))
libros.append(libroModel('2','Harry Potter y el live del profe','Misterio',110, EstadoLibro.LIBRE.name))
libros.append(libroModel('3','Harry Potter y el baneo del live','Misterio',110, EstadoLibro.LIBRE.name))
libros.append(libroModel('4','Harry Potter y sorteo de libros digitales','Misterio',110, EstadoLibro.LIBRE.name))

'''
END    Data
'''

exit = False

def Agregar_libro(libros):
    print("\n--- Agregar Nuevo Libro ---")
    try:
        id = int(input("Ingrese el ID del libro: "))
        titulo = input("Ingrese el título del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        precio = float(input("Ingrese el precio del libro: "))
        estado = input("Ingrese el estado del libro (LIBRE/OCUPADO): ").upper()
        # Crear una nueva instancia del libro y agregarla a la lista
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
        print(libro)
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
    5: Agregar Libros """

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
            inputID = input("Ingrese el código del libro: ")
            actualizar_estado_por_id(libros, inputID, EstadoLibro.ALQUILADO.name)
                    
            print(f"Libro alquilado, Se guardo correctamente")
            if(volverAlMenu() == False):
                exit = True
        case 3:
            inputID = input("Ingrese el código del libro: ")
            actualizar_estado_por_id(libros, inputID, EstadoLibro.LIBRE.name)
            print(f"Libro liberado, Se guardo correctamente")
            
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
        case 0:
            exit = True
            
            
            
            
    if(exit):
        break









