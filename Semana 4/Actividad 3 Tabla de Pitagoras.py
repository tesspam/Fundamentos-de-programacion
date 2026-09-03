#Actividad 3 Tabla de Pitágoras en Matriz y Operaciones Espaciales

def generar_tabla(tamaño):
    tabla = []

    for fila in range(1, tamaño + 1):
        renglon = []

        for columna in range(1, tamaño + 1):
            producto = 0

            for i in range(columna):
                producto = producto + fila

            renglon.append(producto)

        tabla.append(renglon)

    return tabla


def imprimir_tabla(tabla):
    for fila in tabla:
        for elemento in fila:
            print(elemento, end="\t")
        print()


def consultar_producto(tabla, renglon, columna):
    resultado = tabla[renglon - 1][columna - 1]
    return resultado


tamaño = 10

tabla = generar_tabla(tamaño)

print("TABLA DE PITÁGORAS")
imprimir_tabla(tabla)

renglon = int(input("Ingresa el renglón (factor): "))
columna = int(input("Ingresa la columna (factor): "))

resultado = consultar_producto(tabla, renglon, columna)

print("El producto de", renglon, "x", columna, "es:", resultado)
