### Permitir que el usuario ingrese la dimensión y los datos que desea llenar:
elementos = int(input("Escriba el número de elementos que desea ingresar: "))
arreglo = [0]* elementos
print(arreglo)

for i in range(len(arreglo)):
    arreglo[i] = int(input("Ingrese el valor que desee: "))
print(arreglo)
Eleccion = input("Escriba Mayor si desea ordenar de mayor a menor  o Menor si desea de menor a mayor: ")
Eleccion = Eleccion.lower()
print(arreglo)
if Eleccion == "menor":
    for i in range(len(arreglo)): 
        posicionmenor = i
        for j in range(i+1, len(arreglo)):
            if(arreglo[j]< arreglo[posicionmenor]):
                posicionmenor = j
        aux = arreglo[posicionmenor] 
        arreglo[posicionmenor] = arreglo[i]
        arreglo[i] = aux
    print(arreglo)
elif Eleccion == "mayor":
    for i in range(len(arreglo)): 
        posicionmayor = i
        for j in range(i+1, len(arreglo)):
            if(arreglo[j]> arreglo[posicionmayor]):
                posicionmayor = j
        aux = arreglo[posicionmayor] 
        arreglo[posicionmayor] = arreglo[i]
        arreglo[i] = aux
    print(arreglo)


### DIMENSIONES DINAMICAS FILAS - COLUMNAS, SEBE SOLICITAR TANTO PARA MATRIZ A COMO MATRIZ B
## MULTIPLICAR MATRIZ A * MATRIZ B
## IMPRIMIR LA MATRIZ RESULTANTE (DIMENSIONES)

print("Ingreso de datos matriz A")
filasA = int(input("Por favor ingrese el número de filas que desea: "))
columnasA = int(input("Por favor ingrese el número de columnas que desea: "))
print("Ingreso de datos matriz B")
filasB = int(input("Por favor ingrese el npumero de filas que desea: "))
columnasB = int(input("Por favor ingrese el número de columnas que desea: "))

matrizA = [[0 for _ in range(columnasA)]for _ in range(filasA)]
matrizB = [[0]*columnasB for _ in range(filasB)]

# Valores de A
for i in range(len(matrizA)):
    for j in range(len(matrizA[i])):
        valoresA = int(input(f"Ingrese los valores de {i},{j}: "))
        matrizA[i][j] = valoresA
print(f"La matriz A es: {matrizA}")

# Valores de B
for i in range(len(matrizB)):
    for j in range(len(matrizB[i])):
        valoresB = int(input(f"Ingrese los valores de {i},{j}: "))
        matrizB[i][j] = valoresB
print(f"La matriz B es: {matrizB}")

### # Multiplicación 
if columnasA != filasB:
    print("No se puede realizar una multiplicación si las filas y columnas son diferentes")
else:
    matrizC = [[0 for _ in range(columnasB)] for _ in range(filasA)]
    # Bucle para calcular la multiplicación
    for i in range(filasA):   ### Rango para las filas A
        for j in range(columnasB):  ### Rango externo para las columnas B
            for k in range(columnasA):  ### Operación 
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
    print(f"La matriz resultante C es: {matrizC}")


### Calculadora de matrices 
# 1. crear matriz A
# 2. crear matriz B
# 3. imprimir matriz A
# 4. imprimir matriz B
# 5. Imprimir Transpuesta A
# 6. Imprimir Transpuesta B
# 5. sumar matriz A+B
# 6. multiplicar matriz A*B
# 7. salir
print("=======Bienvenido a su calculadora de matrices=======")
print("Operaciones disponibles \n\t1. Crear Matriz A \n\t2. Crear Matriz B \n\t3. Imprimir Matriz A \n\t4. imprimir Matriz B \n\t5. Imrpimir Transpuesta A \n\t6. Imrpimir Transpuesta B \n\t7. Sumanr Matrices \n\t8. Multiplicar Matrices \n\t9. Salir")


def CrearMatriz():
    fila = int(input("Por favor ingrese el número de filas que desea: "))
    columna = int(input("Por favor ingrese el número de columnas que desea: "))
    matriz = [[0 for _ in range(columna)]for _ in range(fila)]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valores = int(input(f"Ingrese los valores de {i},{j}: "))
            matriz[i][j] = valores
    return matriz

def Creartraspuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz)
    matriz_transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]
    for i in range(len(matriz_transpuesta)):
        for j in range(len(matriz_transpuesta[0])):
            matriz_transpuesta[j][i] = matriz[i][j]
    return matriz_transpuesta

def Sumarmatriz(matrizA, matrizB):
    if len(matrizB) != len(matrizA):
        print("No se puede realizar una suma de diferentes dimensiones")
    else:
        Sumas = [[0]* (len(matrizB)) for _ in range (len(matrizA))]
        for i in range((len(matrizA))):
            for j in range(len(matrizA[0])):
                Sumas[i][j] = matrizA[i][j] + matrizB[i][j]
        return Sumas
    
def multiplicarmatriz(matrizA, matrizB):
    if len(matrizA[0]) != len(matrizB):
        print("No se puede realizar la multiplicación. Las columnas de A deben coincidir con las filas de B.")

    # Crear la matriz resultante con dimensiones correctas
    filasA = len(matrizA)
    columnasB = len(matrizB[0])
    columnasA = len(matrizA[0])  
    Multiplicacion = [[0 for _ in range(columnasB)] for _ in range(filasA)]

    # Realizar la multiplicación
    for i in range(filasA):  # Filas de A
        for j in range(columnasB):  # Columnas de B
            for k in range(columnasA):  # Columnas de A (o filas de B)
                Multiplicacion[i][j] += matrizA[i][k] * matrizB[k][j]
    return Multiplicacion


matrizA = None
transpuestaA = None
matrizB = None
transpuestaB = None
MatrizC = None
matrizD = None

opcion = 0
while opcion < 9:
    opcion= int(input("Ingrese la opción que desea realizar: "))
    match opcion:
        case 1:
            matrizA = CrearMatriz()
            print("Matriz A creada")
        case 2:
            matrizB = CrearMatriz()
            print("Matriz B creada")
        case 3:
            print(matrizA)
        case 4:
            print(matrizB)
        case 5:
            transpuestaA = Creartraspuesta(matrizA)
            print(transpuestaA)
        case 6:
            transpuestaB = Creartraspuesta(matrizB)
            print(transpuestaB)
        case 7:
            MatrizC = Sumarmatriz(matrizA, matrizB)
            print(MatrizC)
        case 8:
            matrizD = multiplicarmatriz(matrizA, matrizB)
            print(matrizD)
        case 9:
            print("Saliendo.... \nGracias por usar su calculadora :D  ")
            opcion = 15
        case _:
            print("No ha seleccionado una de las opciones permitidas")




Categorias =["Salud","Alimentación","Transporte","Recreación","Ahorro"] ### Definimos las categorias
gastos = [] ### Creamos una lista vacia para los gastos 

def IngresarPresupuesto():
    presupuesto = [] ### Presupuesto vamos a tratarla como recurrente en este ejemplo, solo se definira una vez y se comparará a todos los meses.
    for categoria in Categorias:
        valor = float(input(f"Ingrese su presupuesto para {categoria}: "))
        presupuestoCategoria = [categoria,valor]
        presupuesto.append(presupuestoCategoria)
    return presupuesto

def IngresarGastos(mes):
    for categoria in Categorias:
        valor = float(input(f"Ingrese sus gastos de {categoria}: "))
        gasto = [mes, categoria, valor]
        gastos.append(gasto)
    print("Sus gastos son: ")
    return gasto
    

def AnalizarGastosMes(mes,presupuesto):  
    for gasto in gastos:
        for categoria in presupuesto:
            if categoria[0] == gasto[1]:        
                if(gasto[0] == mes):
                    print(f"Presuepuesto para  {categoria[0]}  ${categoria[1]}")
                    print(f"Usted Gasto en  {gasto[1]}  ${gasto[2]}")


def AnalizarGastosAnuales(presupuesto):
    gastos_anuales = {}  # Diccionario para almacenar gastos por categoría
    for categoria in Categorias:
        gastos_anuales[categoria] = 0  # Inicializamos los gastos en 0 para cada categoría

    for gasto in gastos:
        categoria = gasto[1]
        valor = gasto[2]
        gastos_anuales[categoria] += valor  # Sumamos el gasto al total de la categoría

    print("\nAnálisis de Gastos Anuales:")
    for categoria, total_gastado in gastos_anuales.items():
        presupuesto_categoria = 0
        for p in presupuesto:
            if p[0] == categoria:
                presupuesto_categoria = p[1]
                break  # Salimos del bucle una vez encontrada la categoría en el presupuesto
        presupuesto_anual = presupuesto_categoria * 12  # Calculamos el presupuesto anual
        print(f"Categoría: {categoria}")
        print(f"Presupuesto Anual: ${presupuesto_anual}")
        print(f"Total Gastado: ${total_gastado}")


print("Bienvenido a su calculadora de presupuestos")
print("Presupuesto general por mes")
presupuesto = IngresarPresupuesto()
print(f"Su presupuesto por mes es de: {presupuesto}")

def obtener_nombre_mes(mes):
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return nombres_meses[mes - 1] if 1 <= mes <= 12 else "Mes no válido"

while True:
    opcion = int(input("Ingrese el mes del que desea detallar gastos (1-12) o 0 para análisis anual: "))
    if opcion == 0:
        AnalizarGastosAnuales(presupuesto)
        break  
    elif 1 <= opcion <= 12:
        mes = opcion
        print(f"Ha seleccionado {obtener_nombre_mes(mes)}")  # Función para obtener el nombre del mes
        IngresarGastos(mes)
        AnalizarGastosMes(mes, presupuesto)
    else:
        print("Ha seleccionado una opción no válida.")

