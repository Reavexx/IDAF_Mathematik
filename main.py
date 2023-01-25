# Calculator
import tkinter as tk
from tkinter import messagebox

# Formula for Midnight
def calculate():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())

    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    diskriminate = b**2 - 4*a*c

    if(x1 == x2):
        result_label.config(text=f"x = {x1}\nDoppellösung")
        messagebox.showinfo("Lösung?", "Doppellösung")
    elif (diskriminate < 0):
        result_label.config(text=f"Keine lösung")
        messagebox.showinfo("Lösung?", "Keine Lösung")
    elif (x1 != x2):
        result_label.config(text=f"x1 = {x1}\nx2 = {x2}")

root = tk.Tk()
root.title("Mitternachtsformel Berechner")



Title_label = tk.Label(root, text="Mitternachtsformel Berechner")
Title_label.pack(side="top")

a_label = tk.Label(root, text="a:")
a_label.pack(side="left", padx= 15, pady=15)

a_entry = tk.Entry(root)
a_entry.pack(side="left", padx= 15, pady=15)

b_label = tk.Label(root, text="b:")
b_label.pack(side="left", padx= 15, pady=15)

b_entry = tk.Entry(root)
b_entry.pack(side="left", padx= 15, pady=15)

c_label = tk.Label(root, text="c:")
c_label.pack(side="left", padx= 15, pady=15)

c_entry = tk.Entry(root)
c_entry.pack(side="left", padx= 15, pady=15)

calculate_button = tk.Button(root, text="Berechnen", command=calculate)
calculate_button.pack(side="left", padx= 15, pady=15)

result_label = tk.Label(root)
result_label.pack(side="left")

root.mainloop()
