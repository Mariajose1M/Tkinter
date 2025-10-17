#*********************************************CONTADOR DE CLICS***************************************#
import tkinter as tk

cnt = 0

def contar():
    global cnt
    cnt += 1
    lbl.config(text=f"Cantidad de clics: {cnt}", fg="purple")

vetn = tk.Tk()
vetn.title("Contador de clics")

btn = tk.Button(vetn, text="Haga clic para contar", command=contar)
btn.pack()

lbl = tk.Label(vetn, text="Cantidad de clics: 0")
lbl.pack()

vetn.mainloop()