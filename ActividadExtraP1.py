# Mostrar el menu
def displayMenu():
    print(">>>>>>>>>>> GESTION DE INVENTARIO <<<<<<<<<<<<")
    print("     1. Agregar un producto.")
    print("     2. Eliminar un producto.")
    print("     3. Mostrar el inventario")
    print("     4. Salir del programa.")

# añadir un producto en el inventario
def addProduct(inventario):
    print(":::: AGREGAR UN PRODUCTO EN EL INVENTARIO ::::")
    nomProduct = input("> Ingrese el nombre del producto: ")
    print()
    cant = int(input("> Ingrese la cantidad: "))
    if (nomProduct in inventario):
        cant += inventario[nomProduct]
    inventario[nomProduct] = cant

# eliminar un producto en el inventario
def deleteProduct (inventario):
    print(":::: ELIMINAR UN PRODUCTO EN EL INVENTARIO :::")
    nomProduct = input("Ingrese el nombre del producto: ")
    if (nomProduct in inventario):
        inventario.pop(nomProduct)
        print("> Ha eliminado este producto exito!!!")
    else:
        print("El producto no existe en el inventario. Vuelve al menu.")

# mostrar el listado de producto en el inventario
def printInventory(inventario):
    print("::: MOSTRAR LOS PRODUCTOS EN EL INVENTARIO :::")
    for i in inventario:
        print(f"Nombre del producto: {i}")
        print(f"Cantidad: {inventario.get(i)}")
        print()
    else:
        print("El inventario esta vacio!")

#Main
inventario = {}
while True:
    displayMenu()
    opcion = input("> Ingrese un numero (1-4): ")
    if opcion.isdigit():
        opcionInt = int(opcion)
        if (opcionInt == 1):
            addProduct(inventario)
        elif (opcionInt == 2):
            deleteProduct(inventario)
        elif (opcionInt == 3):
            printInventory(inventario)
        elif (opcionInt == 4):
            break
    else:
        print("Opcion no valido. Intente de nuevo.")
        exit(1)