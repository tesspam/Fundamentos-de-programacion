precio_bebe=0.0
precio_niño=30.0
precio_adulto_mayor=45.0


#Descuentos 
descuento_adulto_mayor=0.12
descuento_profesor=0.10
descuento_estudiante=0.10
descuento_ninguno=0
total=0.0
descuento=0.0



total_visitantes=int(input("¿Cuántos boletos requieres?: "))
for i in range(total_visitantes):
    print(f"\n--------------visitante {i+1 }---------------")
    edad=int(input("¿Cuál es la edad del visitante?: "))
    if edad <3:
        total_inicial=precio_bebe
    elif edad >=3 and edad <=17:
        total_inicial=precio_niño
    else:
        total_inicial=precio_adulto_mayor

    
if edad <3:
    descuento=descuento_ninguno
else:
    visitantes=input("¿El visitante es profesor, estudiante o adulto mayor? (profesor/estudiante/adulto mayor): ")
    if visitantes=="profesor":
        descuento=descuento_profesor
    elif visitantes=="estudiante":
        descuento=descuento_estudiante
    elif visitantes=="adulto mayor":
        descuento=descuento_adulto_mayor
    else:
        descuento=descuento_ninguno


    total_descuento= total_inicial*descuento
    total_final= total_inicial - total_descuento
    total+= total_final

    print(f"Precio inicial: ${total_inicial:.2f}")
    print(f"Descuento aplicado: ${total_descuento:.2f}({int(descuento*100)}%)")
print(f"Precio final a pagarpor los visitantes ${total:.2f}")
