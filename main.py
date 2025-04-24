import tkinter as tk
from tkinter import messagebox

datos_ciudades = {
    "Madrid": {
        "horas": {
            "8:00": "Temperatura: 20°C\nHumedad: 60%",
            "14:00": "Temperatura: 30°C\nHumedad: 40%",
            "20:00": "Temperatura: 25°C\nHumedad: 50%",
        }
    },
    "París": {
        "horas": {
            "8:00": "Temperatura: 15°C\nHumedad: 70%",
            "20:00": "Temperatura: 18°C\nHumedad: 65%",
        }
    },
    "Londres": {
        "horas": {
            "8:00": "Temperatura: 15°C\nHumedad: 70%",
        }
    },
    "Berlín": {
        "horas": {
            "8:00": "Temperatura: 18°C\nHumedad: 60%",
            "14:00": "Temperatura: 25°C\nHumedad: 50%",
            "20:00": "Temperatura: 20°C\nHumedad: 55%",
        }
    },
    "Roma": {
        "horas": {
            "8:00": "Temperatura: 22°C\nHumedad: 50%",
            "20:00": "Temperatura: 28°C\nHumedad: 45%",
        }
    },
    "Ámsterdam": {
        "horas": {
            "8:00": "Temperatura: 15°C\nHumedad: 65%",
            "14:00": "Temperatura: 20°C\nHumedad: 55%",
            "20:00": "Temperatura: 17°C\nHumedad: 60%",
        }
    },
    "Lisboa": {
        "horas": {
            "8:00": "Temperatura: 18°C\nHumedad: 55%",
            "20:00": "Temperatura: 22°C\nHumedad: 50%",
        }
    },
    "Viena": {
        "horas": {
            "8:00": "Temperatura: 19°C\nHumedad: 58%",
        }
    },
}

def mostrar_horas(ciudad):
    horas = datos_ciudades[ciudad]["horas"].keys()
    ventana_horas = tk.Toplevel(root)
    ventana_horas.title(f"Seleccionar hora - {ciudad}")
    
    label = tk.Label(ventana_horas, text=f"Seleccione una hora para {ciudad}:", font=("Arial", 12))
    label.pack(pady=10)
    
    for hora in horas:
        boton_hora = tk.Button(ventana_horas, text=hora, font=("Arial", 12), 
                               command=lambda h=hora: mostrar_datos(ciudad, h))
        boton_hora.pack(pady=5)

def mostrar_datos(ciudad, hora):
    datos = f"Datos meteorológicos para {ciudad} a las {hora}:\n{datos_ciudades[ciudad]['horas'][hora]}"
    messagebox.showinfo("Datos Meteorológicos", datos)

root = tk.Tk()
root.title("Menú de Tiempo Meteorológico")

label = tk.Label(root, text="Seleccione una ciudad para ver los datos meteorológicos:", font=("Arial", 14))
label.pack(pady=10)

for ciudad in datos_ciudades.keys():
    boton = tk.Button(root, text=ciudad, font=("Arial", 12), command=lambda c=ciudad: mostrar_horas(c))
    boton.pack(pady=5)

root.mainloop()