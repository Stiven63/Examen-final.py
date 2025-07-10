productos = {
    '8475HD': ['HP', 15.6, '8GB', 'dd', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 15.6, '8GB', 'ssd', '512GB', 'Intel Core i5', 'Intel UHD'],
    'JjfFHD': ['Dell', 14.0, '16GB', 'ssd', '1TB', 'Intel Core i7', 'Nvidia MX250'],
    'UWU131HD': ['Dell', 13.3, '8GB', 'dd', '512GB', 'Intel Core i3', 'Intel UHD'],
    '123FHD': ['Lenovo', 15.6, '4GB', 'ssd', '256GB', 'Intel Core i3', 'Intel UHD'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 41],
    'JjfFHD': [424990, 11],
    'UWU131HD': [349990, 11],
    '123FHD': [290890, 32],
}

def stock_marca(marca):
    total = 0
    marca = marca.lower()
    for modelo, info in productos.items():
        if info[0].lower() == marca:
            total += stock.get(modelo, [0,0])[1]
    print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")
    if resultados:
        print("Los notebooks entre los precios consultados son:")
        print(sorted(resultados))
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False
####MENU PRINCIPAL####

def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")

        opcion = input("Ingrese opción: ")

        if opcion == '1':
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opcion == '2':
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(p_min, p_max)

        elif opcion == '3':
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese precio nuevo: "))
                except ValueError:
                    print("Debe ingresar un precio válido.")
                    continue

                exito = actualizar_precio(modelo, nuevo_precio)
                if exito:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")

                repetir = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                if repetir != 'si':
                    break

        elif opcion == '4':
            print("Programa finalizado")
            break

        else:
            print("Debe seleccionar una opción válida!!")

menu()
