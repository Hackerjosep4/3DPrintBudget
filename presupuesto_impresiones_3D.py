# Imports

import tkinter as tk
from os.path import exists as archivoExiste



# Funciones

def leerConfig():

    if not archivoExiste("Config.txt"):
        cerrarPorError("Falta el archivo \"Config.txt\"")

    # Abrir el archivo Config.txt en modo lectura
    with open('Config.txt', 'r', encoding='utf-8') as file:
        # Leer todas las líneas del archivo
        lines = file.readlines()

        if len(lines) != 5:
            cerrarPorError("Contenido erroneo en\nel archivo \"Config.txt\"")
    # Retornamos una lista con las configuraciones

    try:
        config1 = float(lines[0].split(':')[1].strip())
        config2 = float(lines[1].split(':')[1].strip())
        config3 = float(lines[2].split(':')[1].strip())
        config4 = float(lines[3].split(':')[1].strip())
        config5 = str(lines[4].split(':')[1].strip())
    except:
        cerrarPorError("Hay una o varias\nconfiguraciones erroneas")

    return [config1, config2, config3, config4, config5]

def pedirValores1():
    global gramosGastadosDeFilamento
    global tiempoDeImpresion
    global ventanaActual
    global ventana1
    global input1v1
    global input2v1
    global input3v1
    global input4v1

    try:
        gramosGastadosDeFilamento = float(input1v1.get().strip())
        # Calculamos el tiempo de impresion en horas
        tiempoDeImpresion = 0.0
        tiempoDeImpresion += float(input2v1.get().strip())*24
        tiempoDeImpresion += float(input3v1.get().strip())
        tiempoDeImpresion += (float(input4v1.get().strip())+1)/60
    except:
        cerrarPorError("Argumento erroneo")
    ventana1.destroy()
    ventanaActual = 2


def pedirValores2():
    global gastosAdicionales
    global ventanaActual
    global ventana2
    global input1v2
    global text1v2

    if input1v2.get() == "":
        ventana2.destroy()
        ventanaActual = 3
        return

    try:
        gastoAdicional = float(input1v2.get().strip().replace(",","."))
    except:
        cerrarPorError("Argumento erroneo")
    text1v2["text"] += "\n- " + ("{:.2f}".format(gastoAdicional))
    gastosAdicionales.append(gastoAdicional)

def calculos():
    global totalGastosAdicionales
    global gastosAdicionales
    global precioFinal
    global gastoLuz
    global GASTO_IMPRESORA
    global PRECIO_LUZ
    global PRECIO_FILAMENTO
    global tiempoDeImpresion
    global gastoPorTiempo
    global gastoNormalFilamento
    global PESO_BOBINA
    global gramosGastadosDeFilamento
    global gastosTotales
    global beneficosTotales
    global ventanaActual
    global ventana3

    # Sumamos precio de los gastos adicionales
    totalGastosAdicionales = float(sum(gastosAdicionales))*1.5
    precioFinal += totalGastosAdicionales
    # Sumamos precio de la luz
    gastoLuz = (GASTO_IMPRESORA/1000)*PRECIO_LUZ*tiempoDeImpresion
    precioFinal += gastoLuz
    # SUmamos gastos por tiempo
    gastoPorTiempo = tiempoDeImpresion*0.04
    precioFinal += gastoPorTiempo
    # Sumamos precio del filamento
    gastoNormalFilamento = (PRECIO_FILAMENTO*gramosGastadosDeFilamento)/PESO_BOBINA
    if gastoNormalFilamento < 10:
        precioFinal += gastoNormalFilamento*2
    elif gastoNormalFilamento > 20:
        precioFinal += gastoNormalFilamento*1.5
    else:
        precioFinal += gastoNormalFilamento+10

    # Redondear precio final
    precioFinal = round(precioFinal, 2)
    # Calcular beneficios y gastos
    gastosTotales = totalGastosAdicionales+gastoLuz+gastoNormalFilamento
    beneficosTotales = precioFinal-gastosTotales

    ventana3.after(2000, ventana3.destroy)
    ventanaActual = 4

def pedirNombrePresupuesto():
    global input1v4
    global button1v4
    global button2v4
    global button3v4
    global button4v4

    button1v4.pack_forget()
    button2v4.pack_forget()
    input1v4.pack()
    button3v4.pack()
    button4v4.pack()

def guardarPresupuesto():
    global SIMBOLO_MONEDA
    global gramosGastadosDeFilamento
    global tiempoDeImpresion
    global gastoLuz
    global gastoNormalFilamento
    global totalGastosAdicionales
    global gastoPorTiempo
    global gastosTotales
    global beneficosTotales
    global precioFinal
    global input1v4


    nArchivo = input1v4.get().strip()
    nAuxArchivo = nArchivo
    nAux = 0

    if nAuxArchivo == "":
        nAuxArchivo = "Unnamed"

    
    while archivoExiste("Presupuestos\\"+nAuxArchivo+".txt"):
        nAux += 1
        nAuxArchivo = f"{nArchivo} ({nAux})"

    with open("Presupuestos\\"+nAuxArchivo.strip()+".txt", 'w', encoding='utf-8') as archivo:
        # Redirigir la salida estándar al archivo
        print(f"Resultado final:", file=archivo)
        print(file=archivo)
        print(f"\tFilamento usado: {gramosGastadosDeFilamento} g", file=archivo)
        print(f"\tTiempo de impresion: {tiempoDeImpresion} H", file=archivo)
        print(file=archivo)
        print(f"\tGasto energetico: {gastoLuz} {SIMBOLO_MONEDA}", file=archivo)
        print(f"\tGasto material: {gastoNormalFilamento} {SIMBOLO_MONEDA}", file=archivo)
        print(f"\tGastos adicionales: {totalGastosAdicionales} {SIMBOLO_MONEDA}", file=archivo)
        print(f"\tGasto de tiempo: {gastoPorTiempo} {SIMBOLO_MONEDA}", file=archivo)
        print(file=archivo)
        print(f"\tGasto total: {gastosTotales} {SIMBOLO_MONEDA}", file=archivo)
        print(f"\tBeneficio total: {beneficosTotales} {SIMBOLO_MONEDA}", file=archivo)
        print(file=archivo)
        print(f"\tPrecio final: {precioFinal} {SIMBOLO_MONEDA}", file=archivo)

    cancelarPresupuesto()

def cancelarPresupuesto():
    global input1v4
    global button1v4
    global button2v4
    global button3v4
    global button4v4

    input1v4.pack_forget()
    button3v4.pack_forget()
    button4v4.pack_forget()
    button1v4.pack()
    button2v4.pack()

def cerrar():
    global ventanaActual
    global ventana4

    ventana4.destroy()
    ventanaActual = 5

def cerrarPorError(textError = "Unknow"):
    ventanaError = tk.Tk()
    text1vE = tk.Label(ventanaError, text= "Error:")
    text2vE = tk.Label(ventanaError, text= textError)
    text1vE.pack()
    text2vE.pack()
    ventanaError.after(5000, ventanaError.destroy)
    ventanaError.mainloop()
    exit()




# Variables y constantes

PRECIO_FILAMENTO, PESO_BOBINA, PRECIO_LUZ, GASTO_IMPRESORA, SIMBOLO_MONEDA = leerConfig()
ventanaActual = 0
precioFinal = 0.0

ventanaActual = 1
ventana1 = tk.Tk()
ventana1.geometry("220x220")

text1v1 = tk.Label(ventana1, text= "Gramos gastados durante la impresion:")
input1v1 = tk.Entry(ventana1)
text2v1 = tk.Label(ventana1, text= "Tiempos de impresion:")
text3v1 = tk.Label(ventana1, text= "Dias:")
input2v1 = tk.Entry(ventana1)
text4v1 = tk.Label(ventana1, text= "Horas:")
input3v1 = tk.Entry(ventana1)
text5v1 = tk.Label(ventana1, text= "Minutos:")
input4v1 = tk.Entry(ventana1)
button1v1 = tk.Button(ventana1, text= "Continuar", command= pedirValores1)

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

ventana1.mainloop()

while ventanaActual != 2:
    pass

# Gastos adicionales
gastosAdicionales = []

ventana2 = tk.Tk()
ventana2.geometry("200x250")

text1v2 = tk.Label(ventana2, text= "Introduzca los gastos adicionales:\n(Dejar en blanco para continuar)")
input1v2 = tk.Entry(ventana2)
button1v2 = tk.Button(ventana2, text= "Continuar", command= pedirValores2)

text1v2.pack()
input1v2.pack()
button1v2.pack()

ventana2.mainloop()

while ventanaActual != 3:
    pass


ventana3 = tk.Tk()
ventana3.geometry("100x50")

text1v3 = tk.Label(ventana3, text= "Cargando")

text1v3.pack()

ventana3.after(0, calculos)

ventana3.mainloop()


while ventanaActual != 4:
    pass


ventana4 = tk.Tk()
ventana4.geometry("300x500")

#Finalizar

text1v4 = tk.Label(ventana4, text= f'''Resultado final:
---------------------------
Filamento usado:
{gramosGastadosDeFilamento} g
Tiempo de impresion:
{tiempoDeImpresion} H
---------------------------
Gasto energetico:
{gastoLuz} {SIMBOLO_MONEDA}
Gasto material:
{gastoNormalFilamento} {SIMBOLO_MONEDA}
Gastos adicionales:
{totalGastosAdicionales} {SIMBOLO_MONEDA}
Gasto de tiempo:
{gastoPorTiempo} {SIMBOLO_MONEDA}
---------------------------
Gasto total:
{gastosTotales} {SIMBOLO_MONEDA}
Beneficio total:
{beneficosTotales} {SIMBOLO_MONEDA}
---------------------------
Precio final:
{precioFinal} {SIMBOLO_MONEDA}
''')
button1v4 = tk.Button(ventana4, text= "Guardar presupuesto", command= pedirNombrePresupuesto)
input1v4 = tk.Entry(ventana4)
button2v4 = tk.Button(ventana4, text= "Cerrar", command= cerrar)
button3v4 = tk.Button(ventana4, text= "Confirmar nombre\ny guardar presupuesto", command= guardarPresupuesto)
button4v4 = tk.Button(ventana4, text= "Cancelar", command= cancelarPresupuesto)

text1v4.pack()
button1v4.pack()
button2v4.pack()


ventana4.mainloop()


while ventanaActual != 5:
    pass



print("Adios")
exit()