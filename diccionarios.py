# personaedad = ["a","a"]
# total = 100
# for descuento in personaedad:
#     print(descuento)
#     if descuento == "a":
#         print("felicidades tienes un descuento")
#         totaldesc = total*0.5
#     else:
#         print("Ningun descuento se ha aplicado ")
# print(totaldesc)

# print("Antes de finalizar su compra desea agregar algun item adicional: ")

# adicionales = {"Meet & Greet": 50,"Camiseta": 20,"Disco": 25,"Poster":10}

# print("Items disponibles:")
# for clave, valor in adicionales.items():
#     print(f"{clave}: ${valor}")

# print("Antes de finalizar su compra desea agregar algun item adicional: ")

# adicionales = ["Meet & Greet", 50,"Camiseta",20,"Disco", 25,"Poster",10]

# print("Items disponibles:")
# for item in adicionales:
#     print(item)

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

concierto = conciertos[1]
print(concierto)


### ejemplo de acceso a boletos y costos 
# print(f"1. {concierto_seleccionado['entradas'][0]}: ${concierto_seleccionado['entradas'][1]}")
# print(f"2. {concierto_seleccionado['entradas'][2]}: ${concierto_seleccionado['entradas'][3]}")
# print(f"3. {concierto_seleccionado['entradas'][4]}: ${concierto_seleccionado['entradas'][5]}")
