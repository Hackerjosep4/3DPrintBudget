# INDICE
#
# 1: Imports                        Linea: 
# 2: Funciones                      Linea: 
# 3: Iniciar ventana principal      Linea: 
# 4: Variables                      Linea: 
# 5: Codigo                         Linea: 
# 6: Maninloop ventana principal    Linea: 
# 7: Finalizar programa             Linea:
# 
# 
# 
# 
# 
# Ventana0 : Inicializar
# Ventana1 : Pedir valores
# Ventana2 : Gastos extras
# Ventana3 : Hacer calculos
# Ventana4 : Enseñar recivo
# Ventana5 : Guardar recivo
# Ventana6 : Cerrar
# 
# 
# 
# 
# 
# 
# 










# 1: Imports

# Libreria para la parte grafica
import tkinter as tk
# Funcion para comprovar si un archivo existe
from os.path import exists as archivoExiste










# 2: Funciones

# Para cerrar el codigo en caso de error
def cerrarPorError(textError = "Unknow"):
    # Crear una ventana secundaria para el mensage
    ventanaError = tk.Toplevel()
    # Añadir los textos
    text1vE = tk.Label(ventanaError, text= "Error:")
    text2vE = tk.Label(ventanaError, text= textError)
    text1vE.pack()
    text2vE.pack()
    # Hacer que finalize el codigo despues de 5 segundos
    ventanaError.after(5000, exit)
    # Llamar al mainloop
    ventanaError.mainloop()
    # Para que se cierre el codigo en caso que salga del mainloop
    exit()

# Cerrar el programa
def cerrar():
    # Llamar a la ventana principal
    global ventanaPrincipal
    # Cerrar ventana principal
    ventanaPrincipal.destroy()
    # Cerrar codigo
    exit()

# Para vaciar la ventana principal y añadir elementos desde cero
def vaciarVentanaPrincipal():
    # Llamar a las variables globales
    global ventanaPrincipal
    # Destruir cada elemento de la ventana principal
    for elemento in ventanaPrincipal.winfo_children():
        elemento.destroy()
    ventanaPrincipal.geometry("100x100")
    ventanaPrincipal.title("")

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

def loadVentana1():
    global gramosUsados
    global tiempoDeDuracionD
    global tiempoDeDuracionH
    global tiempoDeDuracionM
    global ventanaPrincipal

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Introducir datos")
    ventanaPrincipal.geometry("275x220")

    text1v1 = tk.Label(ventanaPrincipal, text= "Gramos gastados durante la impresion:")
    input1v1 = tk.Entry(ventanaPrincipal)
    text2v1 = tk.Label(ventanaPrincipal, text= "Tiempos de impresion:")
    text3v1 = tk.Label(ventanaPrincipal, text= "Dias:")
    input2v1 = tk.Entry(ventanaPrincipal)
    text4v1 = tk.Label(ventanaPrincipal, text= "Horas:")
    input3v1 = tk.Entry(ventanaPrincipal)
    text5v1 = tk.Label(ventanaPrincipal, text= "Minutos:")
    input4v1 = tk.Entry(ventanaPrincipal)
    button1v1 = tk.Button(ventanaPrincipal, text= "Continuar", command= lambda: funButton1v1(input1v1.get(), input2v1.get(), input3v1.get(), input4v1.get()))

    input1v1.insert(0, str(gramosUsados))
    input2v1.insert(0, str(tiempoDeDuracionD))
    input3v1.insert(0, str(tiempoDeDuracionH))
    input4v1.insert(0, str(tiempoDeDuracionM))

    text1v1.pack()
    input1v1.pack()
    text2v1.pack()
    text3v1.pack()
    input2v1.pack()
    text4v1.pack()
    input3v1.pack()
    text5v1.pack()
    input4v1.pack()
    button1v1.pack()

def loadVentana2():
    global ventanaPrincipal
    global listaGastosAdicionales

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Introducir datos")
    ventanaPrincipal.geometry("275x250")

    text1v2 = tk.Label(ventanaPrincipal, text= "Introduzca los gastos adicionales:\n(Dejar en blanco para continuar)")
    text2v2 = tk.Label(ventanaPrincipal, text= "")
    input1v2 = tk.Entry(ventanaPrincipal)
    button1v2 = tk.Button(ventanaPrincipal, text= "Continuar", command= lambda: funButton1v2(input1v2.get()))
    button2v2 = tk.Button(ventanaPrincipal, text= "Atras", command= loadVentana1)

    for i in listaGastosAdicionales:
        text2v2["text"] += f"\n- {i}"

    text1v2.pack()
    text2v2.pack()
    input1v2.pack()
    button1v2.pack()
    button2v2.pack()

def loadVentana3():
    global ventanaPrincipal

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Calculos")
    ventanaPrincipal.geometry("250x100")

    text1v3 = tk.Label(ventanaPrincipal, text= "Cargando...")

    text1v3.pack()

    calculos()

    ventanaPrincipal.after(2000, loadVentana4)

def loadVentana4():
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

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Presupuesto")
    ventanaPrincipal.geometry("350x400")

    text1v4 = tk.Label(ventanaPrincipal, text= f'''Resultado final:
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
    button1v4 = tk.Button(ventanaPrincipal, text= "Guardar presupuesto", command= loadVentana5)
    button2v4 = tk.Button(ventanaPrincipal, text= "Salir", command= loadVentana6)
    button3v4 = tk.Button(ventanaPrincipal, text= "Atras", command= loadVentana2)
    
    text1v4.pack()
    button1v4.pack()
    button2v4.pack()
    button3v4.pack()

def loadVentana5():
    global ventanaPrincipal

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Guardar")
    ventanaPrincipal.geometry("225x150")

    text1v5 = tk.Label(ventanaPrincipal, text= "Introducir nombre\ndel Presupuesto:")
    input1v5 = tk.Entry(ventanaPrincipal)
    button1v5 = tk.Button(ventanaPrincipal, text= "Confirmar nombre\ny guardar presupuesto", command= lambda: funButton1v5(input1v5.get().strip()))
    button2v5 = tk.Button(ventanaPrincipal, text= "Cancelar", command= loadVentana4)

    text1v5.pack()
    input1v5.pack()
    button1v5.pack()
    button2v5.pack()

def loadVentana6():
    global ventanaPrincipal

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Final")
    ventanaPrincipal.geometry("200x125")

    text1v6 = tk.Label(ventanaPrincipal, text= "")
    button1v6 = tk.Button(ventanaPrincipal, text= "Volver a empezar", command= funButton1v6)
    button2v6 = tk.Button(ventanaPrincipal, text= "Atras", command= loadVentana4)
    button3v6 = tk.Button(ventanaPrincipal, text= "Cerrar", command= cerrar)

    text1v6.pack()
    button1v6.pack()
    button2v6.pack()
    button3v6.pack()

def funButton1v1(gramos, dias, horas, minutos):
    global gramosUsados
    global tiempoDeDuracion
    global tiempoDeDuracionD
    global tiempoDeDuracionH
    global tiempoDeDuracionM

    gramosUsados = float(str(gramos).strip().replace(",","."))
    tiempoDeDuracionD = float(str(dias).strip().replace(",","."))
    tiempoDeDuracionH = float(str(horas).strip().replace(",","."))
    tiempoDeDuracionM = float(str(minutos).strip().replace(",","."))
    tiempoDeDuracion = tiempoDeDuracionD*24 + tiempoDeDuracionH + tiempoDeDuracionM/60

    loadVentana2()

def funButton1v2(gastoAdicional):
    gastoAdicional = str(gastoAdicional).strip().replace(",",".")

    if gastoAdicional == "":
        loadVentana3()
    else:
        gastoAdicional = float(gastoAdicional)
        listaGastosAdicionales.append(gastoAdicional)
        loadVentana2()

def funButton1v5(nombreArchivo):
    guardarPresupuesto(nombreArchivo)

    loadVentana4()

def funButton1v6():
    reiniciarVariables()

    loadVentana1()










# 3: Iniciar ventana principal

ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("250x100")
ventanaPrincipal.title("Iniciando...")
text1v0 = tk.Label(ventanaPrincipal, text= "Iniciando...")
text1v0.pack(expand= True)










# 4: Variables

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










# 5: Codigo

loadVentana1()










# 6: Mainloop ventana principal

ventanaPrincipal.mainloop()










# 7: Finalizar programa

exit()