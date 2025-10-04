def sumar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.set(n1 + n2)
    except ValueError:
        resultado.set("Error")
#--------------------Ventana principal-------------------------------#
ventana= tk.Tk()
ventana.title ("Calculadora basica")
ventana.geometry("250x180")
#--------------------Variables---------------------------------------#
resultado=tk.stringvar()
#----------------------Widgets---------------------------------------#
tk.Label(ventana, text="Numero 1:"). pack(pady=5)
entrada1=tk.entry(ventana)
entrada1.pack()

tk.Label (ventana, text="numero2:").pack (pady=5)
entrada2=tk.entry(ventana)
entrada2.pack()

tk.button (ventana, text="sumar", command=suma).pack(pady=5)
tk.label (ventana,text="resultado:").pack(tk.Label(ventana,textvariable=resultado,fg="pink",font=("Arial",12)).pack()
    ventana.mainloop()
