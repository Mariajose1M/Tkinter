#EJERCICIO 1 Formulario de Registro 
import tkinter as tk

def guardar():
    """Obtiene los valores de los campos y los muestra en lbl_resultado."""
    nombre = entry_nombre.get()
    edad   = entry_edad.get()
    correo = entry_correo.get()

    if nombre and edad and correo:
        # Formateamos el texto que aparecerá en la etiqueta
        texto = f"Nombre: {nombre} | Edad: {edad} | Correo: {correo}"
        lbl_resultado.config(text=texto, fg="green")
    else:
        lbl_resultado.config(
            text="⚠️ Completa todos los campos.", fg="red"
        )

# ---------- Creación de la ventana ----------
root = tk.Tk()
root.title("Formulario de Registro")
root.resizable(False, False)   # Evita que se pueda redimensionar

# ---------- Campos del formulario ----------
tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = tk.Entry(root, width=30)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Edad:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_edad = tk.Entry(root, width=30)
entry_edad.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Correo electrónico:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_correo = tk.Entry(root, width=30)
entry_correo.grid(row=2, column=1, padx=10, pady=5)

# ---------- Botón Guardar ----------
btn_guardar = tk.Button(root, text="Guardar", command=guardar)
btn_guardar.grid(row=3, column=0, columnspan=2, pady=(10, 5))

#---------- Etiqueta para mostrar el resultado ----------
lbl_resultado = tk.Label(root, text="", font=("Helvetica", 9))
lbl_resultado.grid(row=4, column=0, columnspan=2, pady=(5, 10))

#---------- Bucle principal ----------
root.mainloop()

#**************************************************************************************************************

#EJERCICIO 2
import tkinter as tk

def convertir():
    try:
        temp = float(entry.get())
        if var.get() == 1:  # Celsius a Fahrenheit
            resultado = (temp * 9/5) + 32
            label_resultado.config(text=f"{resultado:.2f} °F")
        else:  # Fahrenheit a Celsius
            resultado = (temp - 32) * 5/9
            label_resultado.config(text=f"{resultado:.2f} °C")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un número válido")

root = tk.Tk()
root.title("Conversor de Temperaturas")

entry = tk.Entry(root)
entry.pack()

var = tk.IntVar(value=1)
radio1 = tk.Radiobutton(root, text="Celsius a Fahrenheit", variable=var, value=1)
radio1.pack()
radio2 = tk.Radiobutton(root, text="Fahrenheit a Celsius", variable=var, value=2)
radio2.pack()

boton = tk.Button(root, text="Convertir", command=convertir)
boton.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop()

#*************************************************************************************************

#EJERCICIO 3
import tkinter as tk

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Caja de texto para escribir tarea
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=5)

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Listbox para mostrar tareas
lista_tareas = tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=5)

# Botón eliminar
boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

ventana.mainloop()

#**********************************************************************************************

#Ejercicio 4
import tkinter as tk

contador = 0

def contar():
    global contador
    contador += 1
    etiqueta.config(text=f"Clics: {contador}")

root = tk.Tk()
root.title("Contador de clics")

boton = tk.Button(root, text="Haz clic aquí", command=contar)
boton.pack()

etiqueta = tk.Label(root, text="Clics: 0")
etiqueta.pack()

root.mainloop()