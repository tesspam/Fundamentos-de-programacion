"""
PROYECTO FINAL - Sistema de inscripcion a talleres deportivos
Objetivo: Contar cuantos alumnos de prepa y de universidad se
inscriben a cada taller (Voleibol, Futbol, Flag Football) y
guardar toda la informacion en archivos de texto (.txt).
 
"""
 
import time         # para la pantalla de carga y medir inactividad
import os           # para revisar que archivos .txt existen
import datetime     # para validar que la fecha ingresada sea real
import pdb          # modulo de depuracion 
 
 
# CONSTANTES: valores fijos que usamos varias veces
 
MINUTOS_LIMITE = 10          # minutos de inactividad permitidos
SEGUNDOS_POR_MINUTO = 60
 
# Diccionario: numero de opcion -> nombre del archivo de ese taller
TALLERES = {
    "1": "voleibol.txt",
    "2": "futbol.txt",
    "3": "flag_football.txt",
}
 
# Los 4 archivos .txt que deben existir desde el inicio 
ARCHIVOS_BASE = ["voleibol.txt", "futbol.txt", "flag_football.txt", "horarios.txt"]
 
# MENU COMO MATRIZ: es una lista de listas (filas y columnas) 
MENU = [
    ["1. Leer archivo",        "2. Crear archivo"],
    ["3. Escribir en archivo", "4. Inscribir alumno"],
    ["5. Ver conteo",          "6. Cambiar de usuario"],
    ["7. Salir",               ""],
]
 

# INICIO DEL PROGRAMA 
 
def pedir_usuario():
    """Pide el nombre del usuario y no deja continuar si esta vacio."""
    nombre = ""
    while nombre == "":
        nombre = input("Ingresa tu nombre o nickname: ").strip()
    return nombre
 
 
def dar_bienvenida(nombre):
    """Muestra un mensaje de bienvenida usando el operador '+' de strings."""
    print("=" * 40)
    print("Bienvenido(a) " + nombre + " al sistema de talleres deportivos")
    print("=" * 40)
 
 
def pantalla_de_carga():
    """Simula que el sistema esta cargando, maximo 5 segundos."""
    for segundo in range(1, 5):                 # 4 pasos = 4 segundos
        print("Cargando" + "." * segundo)
        time.sleep(1)
    print("Listo!\n")
 
 
# FECHA EN TUPLA 

 
def pedir_fecha():
    """Pide la fecha y la guarda en una TUPLA: Fecha = dia, mes, anio."""
    while True:
        try:
            texto = input("Fecha de hoy (dd/mm/aaaa): ")
            dia, mes, anio = texto.split("/")
            dia, mes, anio = int(dia), int(mes), int(anio)
            datetime.date(anio, mes, dia)   # esto truena si la fecha no existe
            Fecha = dia, mes, anio          # <- aqui se crea la tupla pedida
            return Fecha
        except ValueError:
            print("Fecha invalida. Usa el formato dd/mm/aaaa, ej. 12/06/2023\n")
 
 
def fecha_texto(fecha):
    """Convierte la tupla (dia, mes, anio) en un texto facil de leer."""
    return f"{fecha[0]:02d}/{fecha[1]:02d}/{fecha[2]}"
 
 
# ARCHIVOS: lectura, escritura y excepciones 

 
def crear_archivos_base(fecha, usuario):
    """Crea los 4 archivos .txt iniciales, solo si todavia no existen."""
    try:
        for nombre in ARCHIVOS_BASE:
            if not os.path.exists(nombre):
                with open(nombre, "w", encoding="utf-8") as archivo:
                    archivo.write(f"Archivo creado el {fecha_texto(fecha)} por {usuario}\n")
    except PermissionError:
        print("No tengo permisos para crear los archivos.")
 
 
def listar_archivos_txt():
    """Regresa una lista con los nombres de todos los .txt que existen."""
    archivos = []
    for nombre in os.listdir("."):
        if nombre.endswith(".txt"):
            archivos.append(nombre)
    return archivos
 
 
def leer_archivo():
    """Muestra los .txt disponibles y despliega el contenido del elegido."""
    try:
        archivos = listar_archivos_txt()
        print("\nArchivos disponibles:")
        for i in range(len(archivos)):
            print(str(i + 1) + ". " + archivos[i])
 
        nombre = input("Escribe el nombre del archivo que quieres abrir: ").strip()
        with open(nombre, "r", encoding="utf-8") as archivo:
            print("\n--- Contenido ---")
            print(archivo.read())
    except FileNotFoundError:
        print("Ese archivo no existe. Revisa que el nombre este bien escrito.")
    except PermissionError:
        print("No tienes permiso para abrir ese archivo.")
 
 
def crear_archivo(fecha, usuario):
    """Crea un archivo .txt nuevo (no sobrescribe uno que ya existe)."""
    try:
        nombre = input("Nombre del nuevo archivo (ej. notas.txt): ").strip()
        if not nombre.endswith(".txt"):
            nombre = nombre + ".txt"
        with open(nombre, "x", encoding="utf-8") as archivo:   # "x" = crear, falla si ya existe
            archivo.write(f"Archivo creado el {fecha_texto(fecha)} por {usuario}\n")
        print("Archivo creado con exito.")
    except FileExistsError:
        print("Ya existe un archivo con ese nombre.")
    except PermissionError:
        print("No tienes permiso para crear archivos aqui.")
 
 
def escribir_archivo(fecha, usuario):
    """Agrega una linea nueva (con fecha) al final de un archivo existente."""
    try:
        nombre = input("Nombre del archivo donde quieres escribir: ").strip()
        texto = input("Escribe lo que quieres guardar: ")
        with open(nombre, "a", encoding="utf-8") as archivo:   # "a" = anexar al final
            archivo.write(f"[{fecha_texto(fecha)}] {usuario}: {texto}\n")
        print("Guardado con exito.")
    except FileNotFoundError:
        print("Ese archivo no existe. Crealo primero con la opcion 2.")
    except PermissionError:
        print("No tienes permiso para escribir en ese archivo.")
 
 
def inscribir_alumno(fecha):
    """Registra la matricula y el nivel del alumno en el taller elegido."""
    try:
        matricula = input("Matricula del alumno: ").strip()
        nivel = input("Nivel (1 = Prepa, 2 = Universidad): ").strip()
 
        if nivel == "1":
            nivel_texto = "Prepa"
        elif nivel == "2":
            nivel_texto = "Universidad"
        else:
            print("Opcion de nivel invalida.")
            return
 
        print("Talleres -> 1. Voleibol   2. Futbol   3. Flag Football")
        taller = input("Numero de taller: ").strip()
        if taller not in TALLERES:
            print("Ese taller no existe.")
            return
 
        nombre_archivo = TALLERES[taller]
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{fecha_texto(fecha)} | {matricula} | {nivel_texto}\n")
        print("Alumno inscrito correctamente.")
    except PermissionError:
        print("No tienes permiso para escribir en el archivo del taller.")
 
 
def ver_conteo():
    """Cuenta cuantos alumnos de Prepa y Universidad hay en cada taller."""
    print("\nTALLER               PREPA   UNIVERSIDAD")
    for taller in TALLERES:
        prepa = 0
        universidad = 0
        try:
            with open(TALLERES[taller], "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea.endswith("Prepa"):
                        prepa = prepa + 1
                    elif linea.endswith("Universidad"):
                        universidad = universidad + 1
            print(f"{TALLERES[taller]:<20} {prepa:<7} {universidad}")
        except FileNotFoundError:
            print(TALLERES[taller] + " (archivo no encontrado)")
 
 

# CONTROL DE INACTIVIDAD 

 
def usuario_esta_inactivo(momento_inicial):
    """Con un ciclo for revisa, minuto por minuto, si ya se cumplieron
    los 10 minutos sin que el usuario haya elegido una opcion."""
    segundos_pasados = time.time() - momento_inicial
    for minuto in range(1, MINUTOS_LIMITE + 1):
        if minuto == MINUTOS_LIMITE and segundos_pasados >= minuto * SEGUNDOS_POR_MINUTO:
            return True
    return False
 
 
def preguntar_si_continua():
    """Suspende el menu y exige responder exactamente 'si' o 'no'."""
    print("\n*** Han pasado 10 minutos sin usar el menu ***")
    while True:
        respuesta = input("Deseas continuar? (si/no): ").strip().lower()
        if respuesta == "si":
            return True
        if respuesta == "no":
            return False
        print("Responde solamente 'si' o 'no'.")
 
 
# MENU PRINCIPAL 

 
def mostrar_menu():
    """Recorre la matriz MENU y la imprime en 2 columnas alineadas."""
    print("\n===== MENU PRINCIPAL =====")
    for fila in MENU:
        print(fila[0].ljust(26) + fila[1])
 
 
def menu_principal(usuario, fecha):
    """Ciclo principal del programa: se repite hasta 'Salir' o
    'Cambiar de usuario'."""
    momento_inicial = time.time()
 
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()
 
        # Revisamos si el usuario tardo demasiado en elegir 
        if usuario_esta_inactivo(momento_inicial):
            if preguntar_si_continua():
                momento_inicial = time.time()
                continue
            else:
                return "inicio"
 
        momento_inicial = time.time()   # se reinicia el contador de tiempo
 
        # pdb.set_trace()   # <- quita el "#" de esta linea para depurar paso a paso
 
        if opcion == "1":
            leer_archivo()
        elif opcion == "2":
            crear_archivo(fecha, usuario)
        elif opcion == "3":
            escribir_archivo(fecha, usuario)
        elif opcion == "4":
            inscribir_alumno(fecha)
        elif opcion == "5":
            ver_conteo()
        elif opcion == "6":
            print("Cambiando de usuario...\n")
            return "inicio"
        elif opcion == "7":
            print("Gracias por usar el sistema. Hasta luego!")
            return "salir"
        else:
            print("Opcion no valida, intenta de nuevo.")
 
# PROGRAMA PRINCIPAL
 
def main():
    while True:
        usuario = pedir_usuario()
        dar_bienvenida(usuario)
        pantalla_de_carga()
        fecha = pedir_fecha()
        crear_archivos_base(fecha, usuario)
        resultado = menu_principal(usuario, fecha)
        if resultado == "salir":
            break
 
 
if __name__ == "__main__":
    main()
    