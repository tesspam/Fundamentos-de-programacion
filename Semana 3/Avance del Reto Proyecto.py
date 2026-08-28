#Registro de inscripcciones a talleres deportivos 

taller = 0
taller_flag = 0
taller_voleibol = 0
taller_futbol = 0

print("Registro de inscripcuones a talleres deportivos")

nombre=input("Ingrese tu nombre:")
tipo=input("¿Eres de prepa o universidad?:")
matricula=int(input("Ingresa tu matricula:"))

print("Seleccione el taller disponibe:")
print("1. Voleibol")
print("2. Futbol")
print("3. Flag Football")

taller=int(input("Ingrese el número del taller que desea inscribirse:"))



if taller==1:
    taller_flag=taller_flag+1
    print("Inscripción realizada en el taller de flag")
    print("Inscritos:", taller_flag)

elif taller==2:
    taller_voleibol=taller_voleibol+1
    print("Inscripción realizada en Voleibol")
    print("Inscritos:", taller_voleibol)

elif taller==3:
    taller_futbol=taller_futbol+1
    print("Inscripción realizada en futbol")
    print("Inscritos:", taller_futbol)

else:
    print ("Taller no disponible seleccione un taller disponible")

