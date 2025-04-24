import tkinter as tk
from tkinter import messagebox

datos_ciudades = {
    "Madrid": "Temperatura: 25°C\nHumedad: 50%",
    "París": "Temperatura: 18°C\nHumedad: 65%",
    "Londres": "Temperatura: 15°C\nHumedad: 70%",
    "Berlín": "Temperatura: 20°C\nHumedad: 55%",
    "Roma": "Temperatura: 28°C\nHumedad: 45%",
    "Ámsterdam": "Temperatura: 17°C\nHumedad: 60%",
    "Lisboa": "Temperatura: 22°C\nHumedad: 50%",
    "Viena": "Temperatura: 19°C\nHumedad: 58%",
}

def mostrar_datos(ciudad):
    datos = f"Datos meteorológicos para {ciudad}:\n{datos_ciudades[ciudad]}"
    messagebox.showinfo("Datos Meteorológicos", datos)

root = tk.Tk()
root.title("Menú de Tiempo Meteorológico")

label = tk.Label(root, text="Seleccione una ciudad para ver los datos meteorológicos:", font=("Arial", 14))
label.pack(pady=10)

for ciudad in datos_ciudades.keys():
    boton = tk.Button(root, text=ciudad, font=("Arial", 12), command=lambda c=ciudad: mostrar_datos(c))
    boton.pack(pady=5)

root.mainloop()