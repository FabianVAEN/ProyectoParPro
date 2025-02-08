# Definir los conciertos y sus categorías de entradas
conciertos = {
    1: {
        "nombre": "Secretos Tour",
        "artista": "Esteman",
        "fecha": "18 de Feb",
        "hora": "21:00",
        "boletos": [100],
        "entradas": ["VIP", 80, "Platinum", 120, "Tribuna", 50]
    },
    2: {
        "nombre": "Fuego en la Montaña",
        "artista": "NOTOKEN",
        "fecha": "28 de Feb",
        "hora": "18:00",
        "boletos": [100],
        "entradas": ["VIP", 120, "Platinum", 150, "Tribuna", 80]
    },
    3: {
        "nombre": "Sinfonía de Dolores",
        "artista": "Mon Laferte",
        "fecha": "3 de Marz",
        "hora": "19:00",
        "boletos": [100],
        "entradas": ["VIP", 120, "Platinum", 140, "Tribuna", 80]
    },
    4: {
        "nombre": "La Fiesta Sigue",
        "artista": "Los fabulosos cadillacs",
        "fecha": "5 de Feb",
        "hora": "18:00",
        "boletos": [100],
        "entradas": ["VIP", 130, "Platinum", 160, "Tribuna", 70]
    },
    5: {
        "nombre": "Dónde Juegan las Niñas?",
        "artista": "Molotov",
        "fecha": "5 de Mar",
        "hora": "20:00",
        "boletos": [100],
        "entradas": ["VIP", 110, "Platinum", 135, "Tribuna", 75]
    }
}

persona = ["Adulto", "Niño", "Tercera edad"] ### Tipo de persona

print("Bienvenido a ICON, tu aplicación para conciertos")
print("Elige tu concierto:")
for clave, valor in conciertos.items():
    print(f"{clave}. {valor["nombre"]} \n\t•Artista: {valor["artista"]} \n\t•Fecha: {valor["fecha"]} \n\t•Hora: {valor["hora"]} \n\t•Boletos disponibles: {valor["boletos"]}")

# Selección de concierto
while True:  
    try:
        seleccion = int(input("Ingresa el concierto al que deseas ir (1-5): "))
        if seleccion > 5 or seleccion < 1:
            print("Selección no válida. Inténtalo de nuevo.")
            continue  
        break  
    except ValueError:
        print("El valor que ingresaste no es válido. Inténtalo de nuevo.")
    except Exception as e:
        print(f"Error identificado como {e}. Inténtalo de nuevo.")

# Obtener el concierto seleccionado
concierto_seleccionado = conciertos[seleccion]
print(f"\nHas seleccionado: {concierto_seleccionado['nombre']}")
print(f"Entradas disponibles {concierto_seleccionado["boletos"]} :")
print("-"*60)

# Numero de entradas
while True:
    try:
        num_entradas = int(input("Ingrese el número de entradas que desea comprar: "))
        if num_entradas < 1:
            print("Error: ingrese un número mayor a cero.")
            continue
        break
    except ValueError:
        print("El valor que ingresaste no es válido.")
    except Exception as e:
        print(f"Error detectado: {e}")

# Verificar si hay suficientes boletos disponibles
if num_entradas > concierto_seleccionado['boletos'][0]:
    print("Error: No hay suficientes boletos disponibles.")
    exit()
else:
    print(concierto_seleccionado['boletos'][0] )
    concierto_seleccionado['boletos'][0] -= num_entradas
    print(f"Ha apartado {num_entradas} entradas. Boletos restantes: {concierto_seleccionado['boletos'][0]}")


### Tipo de persona segun la edad 
personaedad = []
for i in range(num_entradas):
    while True:
        try:
            seleccion_edad = int(input(f"Ingrese (1 - 3) para la entrada {i + 1}: 1. Adulto, 2. Niño, 3. Tercera edad: "))
            if seleccion_edad < 1 or seleccion_edad > 3:
                print("Error: seleccione una opción válida (1, 2 o 3).")
                continue
            break
        except ValueError:
            print("El valor que ingresaste no es válido.")
        except Exception as e:
            print(f"Error detectado: {e}")
    personaedad.append(persona[seleccion_edad - 1])  ### Aqui se resta un menos uno ya que estamos basandonos en la lista persona [] que recordemos comienza con el elemento 0.

print("Las entradas que ha seleccionado son para:", personaedad)

# Selección de categorías de entradas
totalentradas = []

def seleccioncategorias(concierto, num_entradas):
    concierto = concierto_seleccionado
    for i in range(num_entradas):
        while True:
            try:
                print("\nCategorías disponibles:")
                print(f"1. {concierto['entradas'][0]}: ${concierto['entradas'][1]}")
                print(f"2. {concierto['entradas'][2]}: ${concierto['entradas'][3]}")
                print(f"3. {concierto['entradas'][4]}: ${concierto['entradas'][5]}")
                seleccioncategorias = int(input(f"Ingresa la categoría de la entrada {i + 1} (1, 2 o 3): "))
                if seleccioncategorias < 1 or seleccioncategorias > 3:
                    print("Error: seleccione una opción válida (1, 2 o 3).")
                    continue
                break
            except ValueError:
                print("El valor que ingresaste no es válido.")

        if seleccioncategorias == 1:
            categoria = concierto['entradas'][0]  # VIP
            precio = concierto['entradas'][1]     # Precio VIP
        elif seleccioncategorias == 2:
            categoria = concierto['entradas'][2]  # Platinum
            precio = concierto['entradas'][3]     # Precio Platinum
        elif seleccioncategorias == 3:
            categoria = concierto['entradas'][4]  # Tribuna
            precio = concierto['entradas'][5]     # Precio Tribuna

        totalentradas.append((categoria, precio))
        print(f"Entrada {categoria} (${precio}) añadida correctamente.")


seleccioncategorias(concierto_seleccionado, num_entradas)

### Primer total
for i, entrada in enumerate(totalentradas): 
    print(f"Entrada {i + 1}: Categoría: {entrada[0]}, Precio: ${entrada[1]}, Tipo de persona: {personaedad[i]}") ### Recordar que itera sobre una tupla con un indice previo y en personaedad i es le elemento 

total_costo = sum(entrada[1] for entrada in totalentradas) ### Total entradas guarda el costo en tuplas clave, valor, por lo que podemos iterar sobre ellas.

total_entradas_siniva = total_costo

print(f"\nEl costo total de todas las entradas es: ${total_costo}")
iva = total_costo * 0.16
print((f"EL IVA de las entradas es: ${iva}"))

totaldesc = sum(entrada[1] * 0.05 for i, entrada in enumerate(totalentradas) if personaedad[i] == "Tercera edad" or personaedad[i] == "Niño") 


if totaldesc > 0:
    print(f"Felicidades tienes un descuento por tercera edad en tus boletos de: ${totaldesc} \nEl descuento se aplicará al momento de pagar") ### Impresión del primer decuento

print("-"*60)

adicionales = {
    1: ("Meet & Greet", 50),
    2: ("Camiseta", 20),
    3: ("Disco", 25),
    4: ("Poster", 10)
}

# Lista para almacenar los ítems seleccionados
items_seleccionados = []

# Mostrar los ítems disponibles
print("\nAntes de finalizar su compra, ¿desea agregar algún ítem adicional?")
print("Ítems disponibles:")
for clave, (item, precio) in adicionales.items():
    print(f"{clave}. {item}: ${precio}")

# Permitir al usuario seleccionar ítems
while True:
    try:
        seleccion = input("\nIngrese el número del ítem que desea agregar (o 'fin' para terminar): ")
        if seleccion.lower() == "fin":
            break

        seleccion = int(seleccion) #Convertimos la selección a un numero
        
        # Verificar si el número de ítem es válido
        if seleccion in adicionales:
            item, precio = adicionales[seleccion]
            items_seleccionados.append((item, precio))
            print(f"Ítem '{item}' agregado correctamente.")
        else:
            print("Error: Número de ítem no válido. Intente nuevamente.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Calcular el costo total de los ítems adicionales
total_adicionales = sum(item[1] for item in items_seleccionados)

# Mostrar el resumen de los ítems adicionales
if items_seleccionados:
    print("\nResumen de ítems adicionales:")
    for item in items_seleccionados:
        print(f"- {item[0]}: ${item[1]}")
    print(f"Total de ítems adicionales: ${total_adicionales}")
else:
    print("\nNo se agregaron ítems adicionales.")

print("-"*60)
iva2= total_adicionales * 0.16 ### IVA de los adicionales 
iva3= iva +iva2 ### IVA final con boletos + adicionales

totaldesc2 = 0

print("Métodos de pago disponible: \n\t1. Efectivo \n\t2. Tarjeta de credito")
metodode_pago = int(input("Ingrese su método de pago: "))

if metodode_pago == 1:
    print("Gracias por seleccionar efectivo.")
elif metodode_pago == 2:
    totaldesc2 = (total_costo + total_adicionales)*0.10
    print("EL método de pago seleccionado aplica un descuento adicional del 10%")

print(f"Su descuento es de: ${totaldesc2}")

totalscon_iva_sindesc= total_costo + total_adicionales + iva3
decuentos_finales = totaldesc + totaldesc2
total_final = total_costo + total_adicionales + iva3 - decuentos_finales

print("-"*60)
print("Su resumen de compra es: ")
print(f"El costo total de las entradas: ${total_entradas_siniva}")
print(f"El costo toal de los adicionales es: ${total_adicionales}")
print(f"EL descuento final es de : ${decuentos_finales}")
print(f"El IVA de sus compras es: ${iva3}")
print(f"El subttotal de sus compras + IVA y sin descuento es de: ${totalscon_iva_sindesc} ")
print(f"El total a pagar por su compra es de: ${total_final}")
