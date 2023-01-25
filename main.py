# Calculator
import tkinter as tk

# Formula for Midnight
def calculate():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())

    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    diskriminate = b**2 - 4*a*c

    if(x1 == x2):
        result_label.config(text=f"x = {x1}\nDoppellössung")
    elif (diskriminate < 0):
        result_label.config(text=f"Keine lösung")
    elif (x1 != x2):
        result_label.config(text=f"x1 = {x1}\nx2 = {x2}")

root = tk.Tk()
root.title("Mitternachtsformel Berechner made by Dines Nimalthas")
root.config(bg='#A67449')

a_label = tk.Label(root, text="a:")
a_label.grid(row=0, column=0)

a_entry = tk.Entry(root)
a_entry.grid(row=0, column=1)

b_label = tk.Label(root, text="b:")
b_label.grid(row=1, column=0)

b_entry = tk.Entry(root)
b_entry.grid(row=1, column=1)

c_label = tk.Label(root, text="c:")
c_label.grid(row=2, column=0)

c_entry = tk.Entry(root)
c_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Berechnen", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
