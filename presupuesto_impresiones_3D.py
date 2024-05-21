# INDICE
#
# 1: Imports                        Linea: 
# 2: Funciones                      Linea: 
# 3: Variables                      Linea: 
# 4: Codigo                         Linea: 
# 5: Finalizar programa             Linea:
# 
# 
# 
# 
# 
# Apartado0 : Inicializar
# Apartado1 : Pedir valores
# Apartado2 : Gastos extras
# Apartado3 : Hacer calculos
# Apartado4 : Enseñar recivo
# Apartado5 : Guardar recivo
# Apartado6 : Cerrar
# 
# 
# 
# 
# 
# 
# 










# 1: Imports

# Funcion para comprovar si un archivo existe
from os.path import exists as archivoExiste
#
from time import sleep as delay










# 2: Funciones

# Para cerrar el codigo en caso de error
def cerrarPorError(textError = "Unknow"):
    print(f"Error: {textError}")
    delay(5)
    # Para que se cierre el codigo en caso que salga del mainloop
    exit()

# Cerrar el programa
def cerrar():
    print("\nPrograma finalizado")
    delay(5)
    # Cerrar codigo
    exit()

def reiniciarVariables():
    global gramosUsados
    global tiempoDeDuracion
    global tiempoDeDuracionD
    global tiempoDeDuracionH
    global tiempoDeDuracionM
    global listaGastosAdicionales
    global gastoMaterial
    global gastoMaterialBeneficio
    global gastoElectricidad
    global gastoElectricidadBeneficio
    global gastosAdicionales
    global gastosAdicionalesBeneficio
    global gastoDeTiempo
    global gastoDeTiempoBeneficio
    global gastoTotal
    global beneficioTotal
    global precioFinal

    gramosUsados = 0.0
    tiempoDeDuracion = 0.0
    tiempoDeDuracionD = 0.0
    tiempoDeDuracionH = 0.0
    tiempoDeDuracionM = 0.0
    listaGastosAdicionales = []
    gastoMaterial = 0.0
    gastoMaterialBeneficio = 0.0
    gastoElectricidad = 0.0
    gastoElectricidadBeneficio = 0.0
    gastosAdicionales = 0.0
    gastosAdicionalesBeneficio = 0.0
    gastoDeTiempo = 0.0
    gastoDeTiempoBeneficio = 0.0
    gastoTotal = 0.0
    beneficioTotal = 0.0
    precioFinal = 0.0

def leerConfig():
    # Comprovar que el archivo exista
    if not archivoExiste("Config.txt"):
        # Lanzar un error en caso de que no exista
        cerrarPorError("Falta el archivo \"Config.txt\"")

    # Abrir el archivo Config.txt en modo lectura
    with open('Config.txt', 'r', encoding='utf-8') as file:
        # Leer todas las líneas del archivo
        lines = file.readlines()

    # Comprovamos que hayan 5 ajustes
    if len(lines) != 5:
        # Lanzamos un error en caso de que no hayan 5
        cerrarPorError("Contenido erroneo en\nel archivo \"Config.txt\"")

    # Comprovamos que los ajustes sean correctos
    try:
        config1 = float(lines[0].split(':')[1].strip().replace(",","."))
        config2 = float(lines[1].split(':')[1].strip().replace(",","."))
        config3 = float(lines[2].split(':')[1].strip().replace(",","."))
        config4 = float(lines[3].split(':')[1].strip().replace(",","."))
        config5 = str(lines[4].split(':')[1].strip())
    except:
        # Lanzamos un error si no son correctos
        cerrarPorError("Hay una o varias\nconfiguraciones erroneas")

    # Retornamos una lista con las configuraciones
    return [config1, config2, config3, config4, config5]

def guardarPresupuesto(nArchivo = ""):
    # Llamamos a las variables globales
    global SIMBOLO_MONEDA
    global gramosUsados
    global tiempoDeDuracion
    global gastoMaterial
    global gastoElectricidad
    global gastosAdicionales
    global gastoDeTiempo
    global gastoMaterialBeneficio
    global gastoElectricidadBeneficio
    global gastosAdicionalesBeneficio
    global gastoDeTiempoBeneficio
    global gastoTotal
    global beneficioTotal
    global precioFinal

    # Asignamos un nombre al archivo
    nAuxArchivo = nArchivo.strip()
    nAux = 0

    if nAuxArchivo == "":
        nAuxArchivo = "Unnamed"

    
    while archivoExiste("Presupuestos\\"+nAuxArchivo+".txt"):
        nAux += 1
        nAuxArchivo = f"{nArchivo} ({nAux})"

    # Guardamos el archivo
    with open("Presupuestos\\"+nAuxArchivo.strip()+".txt", 'w', encoding='utf-8') as archivo:
        # Redirigir la salida estándar al archivo
        print(f'''Resultado final:
------------------------------------------------------------------
Filamento usado: {gramosUsados} g
Tiempo de impresion: {tiempoDeDuracion} H
------------------------------------------------------------------
Gasto material: {gastoMaterial} {SIMBOLO_MONEDA}
Gasto electricidad: {gastoElectricidad} {SIMBOLO_MONEDA}
Gastos adicionales: {gastosAdicionales} {SIMBOLO_MONEDA}
Gasto de tiempo: {gastoDeTiempo} {SIMBOLO_MONEDA}
------------------------------------------------------------------
Beneficio material: {gastoMaterialBeneficio} {SIMBOLO_MONEDA}
Beneficio electricidad: {gastoElectricidadBeneficio} {SIMBOLO_MONEDA}
Beneficios adicionales: {gastosAdicionalesBeneficio} {SIMBOLO_MONEDA}
Beneficio de tiempo: {gastoDeTiempoBeneficio} {SIMBOLO_MONEDA}
------------------------------------------------------------------
Gasto total: {gastoTotal} {SIMBOLO_MONEDA}
Beneficio total: {beneficioTotal} {SIMBOLO_MONEDA}
------------------------------------------------------------------
Precio final: {precioFinal} {SIMBOLO_MONEDA}''', file=archivo)

def calculos():
    global PRECIO_BOBINA
    global PESO_BOBINA
    global PRECIO_ELECTRICIDAD
    global CONSUMO_IMPRESORA
    global gramosUsados
    global tiempoDeDuracion
    global listaGastosAdicionales
    global gastoMaterial
    global gastoMaterialBeneficio
    global gastoElectricidad
    global gastoElectricidadBeneficio
    global gastosAdicionales
    global gastosAdicionalesBeneficio
    global gastoDeTiempo
    global gastoDeTiempoBeneficio
    global gastoTotal
    global beneficioTotal
    global precioFinal

    # Calculamos los precios relacionados con el material
    gastoMaterial = (gramosUsados*PRECIO_BOBINA)/PESO_BOBINA
    if gastoMaterial < 10:
        gastoMaterialBeneficio = gastoMaterial*2.0
    elif gastoMaterial > 20:
        gastoMaterialBeneficio = gastoMaterial*1.5
    else:
        gastoMaterialBeneficio = gastoMaterial+10.0
    
    # Calcular los precios relacionados con la electricidad
    gastoElectricidad = (CONSUMO_IMPRESORA/1000)*PRECIO_ELECTRICIDAD*tiempoDeDuracion
    gastoElectricidadBeneficio = gastoElectricidad*1.5

    # Calcular los precios relacionados con los gastos adicionales
    gastosAdicionales = sum(listaGastosAdicionales)
    gastosAdicionalesBeneficio = gastosAdicionales*1.5

    # Calcular los precios relacionados con el tiempo de esta impresion con el que no se puede imprimir otras cosas
    gastoDeTiempo = tiempoDeDuracion*0.08
    gastoDeTiempoBeneficio = gastoDeTiempo

    # Calcular el gasto total
    gastoTotal = gastoMaterial+gastoElectricidad+gastosAdicionales+gastoDeTiempo
    # Calcular precio final
    precioFinal = gastoMaterialBeneficio+gastoElectricidadBeneficio+gastosAdicionalesBeneficio+gastoDeTiempoBeneficio
    # Redondear precio final
    precioFinal = round(precioFinal, 2)
    # Calcular beneficio
    beneficioTotal = precioFinal-gastoTotal

def loadApartado1():
    global gramosUsados
    global tiempoDeDuracion
    global tiempoDeDuracionD
    global tiempoDeDuracionH
    global tiempoDeDuracionM

    print("\n\n\n")

    gramosUsados = float(str(input("Gramos gastados durante la impresion: ")).strip().replace(",","."))
    print("Tiempos de impresion:")
    tiempoDeDuracionD = float(input("Dias: ").strip().replace(",","."))
    tiempoDeDuracionH = float(input("Horas: ").strip().replace(",","."))
    tiempoDeDuracionM = float(input("Minutos: ").strip().replace(",","."))
    tiempoDeDuracion = tiempoDeDuracionD*24 + tiempoDeDuracionH + tiempoDeDuracionM/60
    print()

    loadApartado2()

def loadApartado2():
    global listaGastosAdicionales

    print("\n\n\n")
    
    print("Introduzca los gastos adicionales:\n(Dejar en blanco para continuar)")

    for i in listaGastosAdicionales:
        print(f"- {i}")

    gastoAdicional = input(": ").strip().replace(",",".")

    if gastoAdicional != "":
        listaGastosAdicionales.append(float(gastoAdicional))
        loadApartado2()
    
    entradaMenu = input("Menu:\n\tC - Continuar\n\tA - Atras\nRespuesta: ").strip().lower()
    while not (entradaMenu in ["c","a"]):
        print("\nRespuesta incorrecta\n")
        entradaMenu = input("Menu:\n\tC - Continuar\n\tA - Atras\nRespuesta: ").strip().lower()
    
    if entradaMenu == "a":
        loadApartado1()
    else:
        loadApartado3()

def loadApartado3():
    global ventanaPrincipal

    print("\n\n\n")

    print("Cargando...")

    calculos()

    delay(2)

    loadApartado4()

def loadApartado4():
    # Llamamos a las variables globales
    global SIMBOLO_MONEDA
    global gramosUsados
    global tiempoDeDuracion
    global gastoMaterial
    global gastoElectricidad
    global gastosAdicionales
    global gastoDeTiempo
    global gastoMaterialBeneficio
    global gastoElectricidadBeneficio
    global gastosAdicionalesBeneficio
    global gastoDeTiempoBeneficio
    global gastoTotal
    global beneficioTotal
    global precioFinal
    global ventanaPrincipal

    print("\n\n\n")

    print(f'''Resultado final:
------------------------------------------------------------------
Filamento usado: {gramosUsados} g
Tiempo de impresion: {tiempoDeDuracion} H
------------------------------------------------------------------
Gasto material: {gastoMaterial} {SIMBOLO_MONEDA}
Gasto electricidad: {gastoElectricidad} {SIMBOLO_MONEDA}
Gastos adicionales: {gastosAdicionales} {SIMBOLO_MONEDA}
Gasto de tiempo: {gastoDeTiempo} {SIMBOLO_MONEDA}
------------------------------------------------------------------
Beneficio material: {gastoMaterialBeneficio} {SIMBOLO_MONEDA}
Beneficio electricidad: {gastoElectricidadBeneficio} {SIMBOLO_MONEDA}
Beneficios adicionales: {gastosAdicionalesBeneficio} {SIMBOLO_MONEDA}
Beneficio de tiempo: {gastoDeTiempoBeneficio} {SIMBOLO_MONEDA}
------------------------------------------------------------------
Gasto total: {gastoTotal} {SIMBOLO_MONEDA}
Beneficio total: {beneficioTotal} {SIMBOLO_MONEDA}
------------------------------------------------------------------
Precio final: {precioFinal} {SIMBOLO_MONEDA}''')
    
    entradaMenu = input("Menu:\n\tG - Guardar presupuesto\n\tA - Atras\n\tS - Salir\nRespuesta: ").strip().lower()
    while not (entradaMenu in ["g","a","s"]):
        print("\nRespuesta incorrecta\n")
        entradaMenu = input("Menu:\n\tG - Guardar presupuesto\n\tA - Atras\n\tS - Salir\nRespuesta: ").strip().lower()
    
    if entradaMenu == "g":
        loadApartado2()
    elif entradaMenu == "a":
        loadApartado5()
    else:
        loadApartado6()

def loadApartado5():
    global ventanaPrincipal

    print("\n\n\n")

    nArchivo = input("Nombre del presupuesto: ").strip()

    if nArchivo != "":
        guardarPresupuesto(nArchivo)
    
    loadApartado4()

def loadApartado6():
    global ventanaPrincipal

    print("\n\n\n")

    entradaMenu = input("Menu:\n\tV - Volver a empezar\n\tA - Atras\n\tC - Cerrar\nRespuesta: ").strip().lower()
    while not (entradaMenu in ["v","a","c"]):
        print("\nRespuesta incorrecta\n")
        entradaMenu = input("Menu:\n\tV - Volver a empezar\n\tA - Atras\n\tC - Cerrar\nRespuesta: ").strip().lower()

    if entradaMenu == "v":
        reiniciarVariables()
        loadApartado1()
    elif entradaMenu == "a":
        loadApartado4()
    else:
        cerrar()










# 3: Variables

# Iniciar variables
PRECIO_BOBINA = 0.0
PESO_BOBINA = 0.0
PRECIO_ELECTRICIDAD = 0.0
CONSUMO_IMPRESORA = 0.0
SIMBOLO_MONEDA = ""
gramosUsados = 0.0
tiempoDeDuracion = 0.0
tiempoDeDuracionD = 0.0
tiempoDeDuracionH = 0.0
tiempoDeDuracionM = 0.0
listaGastosAdicionales = []
gastoMaterial = 0.0
gastoMaterialBeneficio = 0.0
gastoElectricidad = 0.0
gastoElectricidadBeneficio = 0.0
gastosAdicionales = 0.0
gastosAdicionalesBeneficio = 0.0
gastoDeTiempo = 0.0
gastoDeTiempoBeneficio = 0.0
gastoTotal = 0.0
beneficioTotal = 0.0
precioFinal = 0.0

# Dar valores iniciales
PRECIO_BOBINA, PESO_BOBINA, PRECIO_ELECTRICIDAD, CONSUMO_IMPRESORA, SIMBOLO_MONEDA = leerConfig()










# 4: Codigo

loadApartado1()










# 5: Finalizar programa

exit()