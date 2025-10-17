#**************************************************LISTA DE TAREAS***************************************#
import tkinter as tk

def agr_t():
    tar = ent_t.get()
    if tar != "":
        lst_t.insert(tk.END, tar)
        ent_t.delete(0, tk.END)

def elm_t():
    sel = lst_t.curselection()
    if sel:
        lst_t.delete(sel)

vetn = tk.Tk()
vetn.title("Lista de Tareas")

ent_t = tk.Entry(vetn, width=40)
ent_t.pack(pady=5)

btn_agr = tk.Button(vetn, text="Agregar elemento", command=agr_t)
btn_agr.pack(pady=5)

lst_t = tk.Listbox(vetn, width=50, height=20)
lst_t.pack(pady=5)

btn_elm = tk.Button(vetn, text="Eliminar elemento", command=elm_t)
btn_elm.pack(pady=5)

vetn.mainloop()