import tkinter as tk

def calculate():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())

    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

    result_label.config(text=f"x1 = {x1}\nx2 = {x2}")

root = tk.Tk()
root.title("Mitternachtsformel Berechner made by Dines Nimalthas")

root.grid_columnconfigure(index=0, weight=1)
root.grid_rowconfigure(index=0, weight=1)

a_label = tk.Label(root, text="a:")
a_label.grid(row=0, column=0, sticky='nwse')

a_entry = tk.Entry(root)
a_entry.grid(row=0, column=1, sticky='nwse')

b_label = tk.Label(root, text="b:")
b_label.grid(row=1, column=0, sticky='nwse')

b_entry = tk.Entry(root)
b_entry.grid(row=1, column=1, sticky='nwse')

c_label = tk.Label(root, text="c:")
c_label.grid(row=2, column=0, sticky='nwse')

c_entry = tk.Entry(root)
c_entry.grid(row=2, column=1, sticky='nwse')

calculate_button = tk.Button(root, text="Berechnen", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, sticky='nwse')

result_label = tk.Label(root)
result_label.grid(row=4, column=0, columnspan=2, sticky='nwse')

root.mainloop()
