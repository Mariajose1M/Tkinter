import tkinter as tk

def sumar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.set(n1 + n2)
    except ValueError:
        resultado.set("Error")

#--------------------Ventana principal-------------------------------#
ventana = tk.Tk()
ventana.title("Calculadora basica")
ventana.geometry("250x180")

#--------------------Variables---------------------------------------#
resultado = tk.StringVar()

#----------------------Widgets---------------------------------------#
tk.Label(ventana, text="Numero 1:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Numero 2:").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Sumar", command=sumar).pack(pady=5)
tk.Label(ventana, text="Resultado:").pack()
tk.Label(ventana, textvariable=resultado, fg="pink", font=("Arial", 12)).pack()

ventana.mainloop()