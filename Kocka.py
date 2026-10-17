import tkinter as tk
from tkinter import ttk

def dobas():
    print("dobtam")
    pass
root = tk.Tk()
root.geometry("600x400")
root.title("Kockázás")
root.resizable(False, False)


cím_cimke =ttk.Label(text="Kockajáték", font=("Arial", 14, "bold") )
cím_cimke.pack(pady=20)

dobas_szam = tk.StringVar(value="10")
dobas_szam_be =ttk.Entry(textvariable=dobas_szam,width=10)
dobas_szam_be.pack(pady=20)

dobas_gomb =ttk.Button(text="Dobás",command=dobas)
dobas_gomb.pack(pady=20)


kilepes_gomb = ttk.Button(text="Kilépés", width=10, command=root.destroy)
kilepes_gomb.pack(pady=20)

dobas_eredmenye =ttk.Label(root, text="Eredmény:", font=("Arial", 14, ) )
dobas_eredmenye.pack(pady=20)

root.mainloop()