# print("Bienvenido a ICON tu aplicación para conciertos")
# print("Elige tu concierto: \n1. Secretos Tour \n\t•Artista: Esteman \n\t•Fecha: 18 de Feb \n\t•Hora: 21:00")
# print("\n2. Fuego en la Montaña \n\t•Artista: NOTOKEN \n\t•Fecha: 28 de Feb \n\t•Hora: 18:00")
# print("\n3. Sinfonía de Dolores \n\t•Artista: Mon Laferte \n\t•Fecha: 3 Marz \n\t•Hora: 19:00")
# print("\n4. La Fiesta Sigue \n\t•Artista: Los fabulosos cadillacs \n\t•Fecha: 5 de Feb \n\t•Hora: 18:00")
# print("\n5. Dónde Juegan las Niñas? \n\t•Artista: Molotov\n\t•Fecha: 5  de FMar \n\t•Hora: 20:00")

### Tipo de persona 
persona = ["Adulto","Niño", "Tercera edad"]
Con1 = ["VIP",80,"Platinum",120,"Tribuna",50]
Con2 = ["VIP",120,"Platinum",150,"Tribuna",80]
Con3 = ["VIP",120,"Platinum",140,"Tribuna",80]
Con4 = ["VIP",130,"Platinum",160,"Tribuna",70]
Con5 = ["VIP",110,"Platinum",135,"Tribuna",75]
### Tipo de localidad 

eleccion = None
try:
    seleccion = int(input("Ingresa el concierto al que deseas ir (1-5): "))
    match seleccion:
        case 1:
            eleccion = 1
            print("Has seleccionado: Secretos Tour ")
            print("Entradas disponibles: ")
            print(Con1)
        case 2:
            eleccion = 2
            print("Has seleccionado: Fuego en la Montaña")
            print("Entradas disponibles: ")
            print(Con2)
        case 3:
            eleccion = 3
            print("Has seleccionado: Sinfonía de Dolores")
            print("Entradas disponibles: ")
            print(Con3)
        case 4:
            eleccion = 4
            print("Has seleccionado: La Fiesta Sigue")
            print("Entradas disponibles: ")
            print(Con4)
        case 5:
            eleccion = 5
            print("Has seleccionado: Dónde juegan las Niñas?")
            print("Entradas disponibles: ")
            print(Con5)
except ValueError:
    print("El valor que ingrsaste no es valido")

try:
    num_entradas = int(input("Ingrese el número de entradas que desea comprar: "))
except ValueError:
    print("El valor que ingresaste no es válido.")

num_entradas_aux = num_entradas ### Auxiliar para seleccion de persona 
categorias_aux = num_entradas ### Auxiliar para selección de categoría

personaedad = []
while True:
    if num_entradas_aux < 1:
        print("Error ingrese un número mayor a uno")
    elif num_entradas_aux > 0:
        seleccion_edad = int(input("Ingrese (1 - 3) correspondiendo: 1. Adulto, 2. Niño, 3. Preferencial: "))
        if seleccion_edad < 1 or seleccion_edad > 3:
            print("Error: seleccione una opción válida (1, 2 o 3).")
            continue
        if seleccion_edad == 1:
            personaedad.append(persona[0])
        elif seleccion_edad == 2:
            personaedad.append(persona[1])
        elif seleccion_edad == 3:
            personaedad.append(persona[2])
    num_entradas_aux -= 1
    if num_entradas_aux == 0:
        break
print("Las entradas que ha seleccionado son para:", personaedad)

totalentradas = []

def seleccioncategorias():
    if seleccion ==1:
        print("Categorías disponibles:")
        print(f"1. VIP: ${Con1[1]}")
        print(f"2. Platinum: ${Con1[3]}")
        print(f"3. Tribuna: ${Con1[5]}")
    categorias_aux = num_entradas
    while categorias_aux > 0:
        seleccioncategorias = int(input("Ingresa la categoría de tus entradas: 1. VIP 2. Preferencia 3. Tribuna: "))
        if seleccioncategorias < 1 or seleccioncategorias > 3:
            print("Ingrese una categoría válida")
        if eleccion == 1:
            concierto = Con1
        if seleccioncategorias == 1:
            categoria = concierto[0]  # VIP
            precio = concierto[1]     # Precio VIP
        elif seleccioncategorias == 2:
            categoria = concierto[2]  # Platino
            precio = concierto[3]     # Precio Platino
        elif seleccioncategorias == 3:
            categoria = concierto[4]  # Tribuna
            precio = concierto[5]     # Precio Tribuna
        categorias_aux -= 1
        totalentradas.append((categoria, precio)) # Almacenar la categoría y el precio en la lista totalentradas
        print(f"Entrada {categoria} (${precio}) añadida correctamente.")


# Llamar a la función para seleccionar categorías
seleccioncategorias()

# Mostrar las entradas seleccionadas
print("\nEntradas seleccionadas:")
for entrada in totalentradas:
    print(f"Categoría: {entrada[0]}, Precio: ${entrada[1]}")

boletos = seleccioncategorias()
print(seleccioncategorias)


