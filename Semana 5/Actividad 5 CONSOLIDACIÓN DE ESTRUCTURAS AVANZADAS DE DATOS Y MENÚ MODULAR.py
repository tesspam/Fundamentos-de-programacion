

def suma_numeros(numeros):
    suma = 0
    
    for numero in numeros:
        suma += numero
        
    return suma


def trabajar_tuplas():
    numeros = (5, 8, 10, 3, 7)
    
    
    print("\nTercer elemento:", numeros[2])
    
    
    nuevo1 = float(input("Ingresa el primer número adicional: "))
    nuevo2 = float(input("Ingresa el segundo número adicional: "))
    
    
    numeros = numeros + (nuevo1, nuevo2)
    
    print("Nueva tupla:", numeros)
    
    
    lista_numeros = list(numeros)
    lista_numeros.sort()
    
    print("Lista ordenada:", lista_numeros)
    
    
    total = suma_numeros(numeros)
    print("Suma total:", total)


def buscar_contacto(contactos, nombre):
    return contactos.get(nombre)


def trabajar_diccionarios():
    contactos = {
        "Ana": "555-0101",
        "Luis": "555-0102",
        "Mía": "555-0103"
    }
    

    nombre = input("Nombre del nuevo contacto: ")
    telefono = input("Teléfono del nuevo contacto: ")
    
    contactos[nombre] = telefono
    

    print("\nContactos registrados:")
    
    for nombre in contactos.keys():
        print(nombre)
    

    nombre_buscar = input("Nombre a buscar: ")
    
    telefono_encontrado = buscar_contacto(contactos, nombre_buscar)
    
    if telefono_encontrado:
        print("El teléfono de", nombre_buscar, "es:", telefono_encontrado)
    else:
        print("Contacto no encontrado.")



def trabajar_excepciones():
    
        numero1 = int(input("Primer número entero: "))
        numero2 = int(input("Segundo número entero: "))
        
    
        suma = numero1 + numero2
        print("La suma es:", suma)
        
    
        resultado = numero1 / numero2
        print("La división es:", resultado)
        

        print("Error: Debes ingresar números enteros.")
        

        print("Error: No es posible dividir entre cero. Ingresa un divisor distinto de 0.")



def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)


def trabajar_strings():
    
    mensaje = "Python es un lenguaje poderoso"
    

    print("\nLongitud del mensaje:", len(mensaje))
    
    
    print("En mayúsculas:", mensaje.upper())
    
    
    texto_reemplazado = mensaje.replace("Python", "programación")
    print("Texto reemplazado:", texto_reemplazado)
    
    
    total_palabras = contar_palabras(mensaje)
    print("Palabras totales:", total_palabras)


opcion = 0

while opcion != 5:
    

    print("MENÚ PRINCIPAL")
    print("1. Trabajar con tuplas")
    print("2. Trabajar con diccionarios")
    print("3. Trabajar con excepciones")
    print("4. Trabajar con strings")
    print("5. Finalizar")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        trabajar_tuplas()
        
    elif opcion == "2":
        trabajar_diccionarios()
        
    elif opcion == "3":
        trabajar_excepciones()
        
    elif opcion == "4":
        trabajar_strings()
        
    elif opcion == "5":
        print("Programa finalizado.")
        
    else:
        print("Opción no válida. Selecciona un número del 1 al 5.")



