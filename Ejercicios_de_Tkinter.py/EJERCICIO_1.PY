# *********************************FORMULARIO DE REGISTRO*******************************# 
import tkinter as tk

def guardar_dt():
    nom = ent_nom.get()
    ed  = ent_ed.get()
    cor = ent_cor.get()
    
    if nom and ed and cor:
        texto = f"Nombre: {nom} | Edad: {ed} | Correo: {cor}"
        lbl_msg.config(text=texto, fg="cyan")
    else:
        lbl_msg.config(
            text=" *POR FAVOR COMPLETE TODOS LOS DATOS*", fg="orange"
        )

vetn = tk.Tk()
vetn.title("Formulario de Registro")
vetn.resizable(False, False)   

tk.Label(vetn, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
ent_nom = tk.Entry(vetn, width=30)
ent_nom.grid(row=0, column=1, padx=10, pady=5)

tk.Label(vetn, text="Edad:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
ent_ed = tk.Entry(vetn, width=30)
ent_ed.grid(row=1, column=1, padx=10, pady=5)

tk.Label(vetn, text="Correo electrónico:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
ent_cor = tk.Entry(vetn, width=30)
ent_cor.grid(row=2, column=1, padx=10, pady=5)

btn_g = tk.Button(vetn, text="Guardar", command=guardar_dt)
btn_g.grid(row=3, column=0, columnspan=2, pady=(10, 5))

lbl_msg = tk.Label(vetn, text="", font=("Verdana", 9))
lbl_msg.grid(row=4, column=0, columnspan=2, pady=(5, 10))

vetn.mainloop()