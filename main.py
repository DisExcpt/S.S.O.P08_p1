import random
import threading
import tkinter as tk
import time
from parking import *


def entrada_auto():
    while True:
        estacionamiento.agregar_auto()
        actualizar_interfaz()
        time.sleep(frecuencia_entrada)

def salida_auto():
    while True:
        estacionamiento.retirar_auto()
        actualizar_interfaz()
        time.sleep(frecuencia_salida)

def actualizar_interfaz():
    for i, estado in enumerate(estacionamiento.estado):
        if estado == "libre":
            canvas.itemconfig(rectangulos[i], fill="green")
        else:
            canvas.itemconfig(rectangulos[i], fill="red")

def actualizar_frecuencias():
    global frecuencia_entrada, frecuencia_salida
    frecuencia_entrada = float(frecuencia_entrada_var.get())
    frecuencia_salida = float(frecuencia_salida_var.get())

# Inicializar el estacionamiento
capacidad_estacionamiento = 12
estacionamiento = Estacionamiento(capacidad_estacionamiento)
frecuencias = [0.5,1,2]

# Crear la ventana principal de la interfaz
ventana = tk.Tk()
ventana.title("Estacionamiento")

# Crear el lienzo (canvas) para mostrar el estacionamiento
canvas = tk.Canvas(ventana, width=400, height=300)
canvas.pack()

# Crear rectángulos para representar los espacios del estacionamiento
tamano_espacio = 50  # Tamaño de cada espacio del estacionamiento
rectangulos = []
# con este podemos alterar la posicion de las casillas en la pantalla , con un valor de
# 50 el estacionamiento queda realtivamente centrado en x para las medidas de este ejemplo
pos = 50 

x, y = pos, pos  # Posición inicial

for i in range(capacidad_estacionamiento):
    rectangulo = canvas.create_rectangle(x, y, x + tamano_espacio, y + tamano_espacio, outline="black", fill="green")
    rectangulos.append(rectangulo)
    # dos filas de 6 columnas para simular que es un parking normal
    if (i + 1) % 6 == 0:
        x = pos
        y += tamano_espacio
    else:
        x += tamano_espacio

# frecuencias iniciales para el estacionamiento
frecuencia_entrada = random.choice(frecuencias)  # segundos
frecuencia_salida = random.choice(frecuencias)  # segundos


# Controles para ajustar las frecuencias
frecuencia_entrada_var = tk.StringVar(value=str(frecuencia_entrada))  # Valor inicial de la frecuencia de entrada
frecuencia_salida_var = tk.StringVar(value=str(frecuencia_salida))  # Valor inicial de la frecuencia de salida

etiqueta_frecuencia_entrada = tk.Label(ventana, text="Frecuencia de Entrada:")
entrada_frecuencia_entrada = tk.Entry(ventana, textvariable=frecuencia_entrada_var)
etiqueta_frecuencia_salida = tk.Label(ventana, text="Frecuencia de Salida:")
entrada_frecuencia_salida = tk.Entry(ventana, textvariable=frecuencia_salida_var)
boton_actualizar_frecuencias = tk.Button(ventana, text="Actualizar Frecuencias",cursor="hand2", command=actualizar_frecuencias)

etiqueta_frecuencia_entrada.pack()
entrada_frecuencia_entrada.pack()
etiqueta_frecuencia_salida.pack()
entrada_frecuencia_salida.pack()
boton_actualizar_frecuencias.pack()

# Iniciar hilos para la entrada y salida de autos
thread_entrada = threading.Thread(target=entrada_auto)
thread_salida = threading.Thread(target=salida_auto)

# Iniciar los hilos
thread_entrada.start()
thread_salida.start()

# Iniciar la actualización de la interfaz
actualizar_interfaz_thread = threading.Thread(target=actualizar_interfaz)
actualizar_interfaz_thread.start()

# Ejecutar la interfaz
ventana.mainloop()

# Esperar a que los hilos terminen
thread_entrada.join()
thread_salida.join()
actualizar_interfaz_thread.join()
