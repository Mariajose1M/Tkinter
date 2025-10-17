#*********************************************CONVERSOR DE TEMPERATURAS****************************#
import tkinter as tk

def conv():
    try:
        tmp = float(ent.get())
        if op.get() == 1: 
            res = (tmp * 9/5) + 32
            lbl_res.config(text=f"{res:.1f} °F")
        else:  
            res = (tmp - 32) * 5/9
            lbl_res.config(text=f"{res:.1f} °C")
    except ValueError:
        lbl_res.config(text="*EL NUMERO INGRESADO NO ES VALIDO, VUELVA A INTENTARLO*")

vetn = tk.Tk()
vetn.title("Conversor de Temperaturas")

ent = tk.Entry(vetn)
ent.pack()

op = tk.IntVar(value=1)
r1 = tk.Radiobutton(vetn, text="Celsius a Fahrenheit", variable=op, value=1)
r1.pack()
r2 = tk.Radiobutton(vetn, text="Fahrenheit a Celsius", variable=op, value=2)
r2.pack()

btn = tk.Button(vetn, text="Convertir grados", command=conv)
btn.pack()

lbl_res = tk.Label(vetn, text="")
lbl_res.pack()

vetn.mainloop()