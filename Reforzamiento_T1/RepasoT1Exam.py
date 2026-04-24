class Zapato:
    def __init__(self, modelo = "", talla = 0, precio = 0):
        self.modelo = modelo 
        self.talla = talla 
        self.precio = precio

    def __str__(self):
        return f"-> {self.modelo} - {self.talla} (S/{self.precio})"
    

#busqueda lineal con letras
def buscaZapato(lst, zapa) -> bool:
    for z in lst:
        if z.modelo == zapa.modelo and z.talla == zapa.talla and z.precio == zapa.precio:
            return True
    return False


def ordSeleccion(lst):
    n = len(lst)
    for mano in range(n-1):
        posMayor = mano
        for ver in range(mano + 1, n):
            if lst[ver].talla > lst[posMayor].talla:
                posMayor = ver
        lst[mano], lst[posMayor] = lst[posMayor], lst[mano]


def ordInsercion(lst):
    n = len(lst)
    for pasada in range(1,n):
        posnuenum = pasada
        while posnuenum >= 1 and lst[posnuenum] < lst[posnuenum - 1]:
            lst[posnuenum], lst[posnuenum - 1] = lst[posnuenum - 1], lst[posnuenum]
            posnuenum -= 1


def busqueda_bin(lista, objetivo): 
    lower = 0 
    higher = len(lista) - 1 
    while lower + 1 < higher: 
        middle = (lower + higher) // 2 
        if lista[middle] == objetivo: 
            return True 
        elif lista[middle] < objetivo: 
            lower = middle
        elif lista[middle] > objetivo: 
            higher = middle 
    return False
numeros = [4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 58, 65, 80, 98] 
buscar = int(input("Ingrese numero a buscar:\n")) 
if busqueda_bin(numeros, buscar): 
    print(f"Número encontrado") 
else: 
    print("Número no encontrado")


#busqueda lineal con numero 
num = int(input("Ingrese numero a buscar:\n"))
lista = [1,2,3,4,5]
for x in lista:
    if x == num:
        print("Encontrado")

#menu de opciones 
lista = []        
while True:
    print("----Menú de opciones----")
    print("-> 1. Agregar")
    print("-> 2. Listar")
    print("-> 3. Borrar Talla")
    print("-> 4. Buscar Talla")
    print("-> 9 Salir")
    opc = input("Seleccione una opción: ")
    if opc == "1":
        #crear nuevo
        modelo = input("Ingrese modelo:")
        talla = int(input("Ingrese talla:"))
        precio = float(input("Ingrese precio:"))
        nuevo = Zapato(modelo, talla, precio)
        #validar que no existe
        if not buscaZapato(lista, nuevo):
            print(nuevo)
            lista.append(Zapato(modelo, talla, precio))
            print(len(lista))

    elif opc == "2":
        #Listar todos sin ordenarlos 
        for a in lista:
            print(a)

    elif opc == "3":
        #ordenar seleccion
        ordSeleccion(lista)
        elitalla = int(input("Ingrese talla a eliminar: "))
        #elimina lineal
        for idx, q in enumerate(lista):
            if q.talla == elitalla:
                del lista[idx]
    
    elif opc == "4":
        #orden por insercion
        ordInsercion(lista)