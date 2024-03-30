from tkinter import *
from tkinter import messagebox

# Función para solicitar el número de VLANs a generar
def ask_for_vlans():
    vlans_count = entry_vlans.get()
    if not vlans_count.isdigit() or int(vlans_count) <= 0:
        messagebox.showerror("Error", "Ingrese un número entero positivo.")
        return
    vlans_count = int(vlans_count)

    # Verifica si ya se han generado VLANs antes
    if entry_vlan_names:
        current_vlan_count = len(entry_vlan_names)
        # Si el número de VLANs generado es mayor que el nuevo número ingresado, no hagas nada
        if current_vlan_count >= vlans_count:
            messagebox.showinfo("Información", f"Ya se han generado {current_vlan_count} VLANs. No se necesitan más.")
            return
        else:
            # Si el nuevo número ingresado es mayor que el número actual, 
            # solo genera las VLANs adicionales
            vlans_count -= current_vlan_count

    # Limpiar los cuadros de entrada anteriores antes de crear nuevos
    clear_vlans()

    # Crea los campos de entrada para los nombres de las VLANs
    for i in range(vlans_count):
        label = Label(frame_vlan_names, text=f"Ingrese el nombre de la VLAN {i + 2}:")
        label.grid(row=i+1, column=0, padx=5, pady=5, sticky="w")
        label_vlan_names.append(label)

        entry = Entry(frame_vlan_names)
        entry.grid(row=i+1, column=1, padx=5, pady=5, sticky="ew")
        entry_vlan_names.append(entry)

    # Configurar el tamaño de la ventana de desplazamiento
    frame_vlan_names.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Deshabilitar el scroll si no es necesario
    if len(entry_vlan_names) <= 5:  # Ajusta el número según sea necesario
        scrollbar.grid_forget()
        canvas.config(yscrollcommand=None)
    else:
        scrollbar.grid(row=1, column=2, sticky="ns")
        canvas.config(yscrollcommand=scrollbar.set)

    # Actualizar estado de los botones
    button_ask.config(state=DISABLED)
    button_generate.config(state=NORMAL)
    button_clear.config(state=NORMAL)

# Función para generar los comandos VLAN
def generate_vlans():
    vlans_data = []
    vlan_names = set()  # Utilizamos un conjunto para almacenar los nombres y garantizar que no se repitan
    for i, entry in enumerate(entry_vlan_names):
        vlan_name = entry.get().strip()
        if not vlan_name:
            messagebox.showerror("Error", f"Ingrese el nombre de la VLAN {i + 2}.")
            return
        if vlan_name in vlan_names:  # Verificar si el nombre ya existe
            messagebox.showerror("Error", f"El nombre de la VLAN '{vlan_name}' ya ha sido utilizado.")
            return
        vlan_names.add(vlan_name)  # Agregar el nombre al conjunto
        vlans_data.append(f"vlan {i + 2}\nname {vlan_name}\nexit\n")  # Se inicia desde la VLAN 2

    # Mostrar los comandos VLAN generados
    result_text.delete(1.0, END)
    result_text.insert(END, "".join(vlans_data))

    # Actualizar estado de los botones
    button_save.config(state=NORMAL)
    button_copy.config(state=NORMAL)

# Función para guardar los comandos VLAN en un archivo
def save_vlans():
    vlans_data = result_text.get(1.0, END)
    with open("vlans.txt", "w") as file:
        file.write(vlans_data)

    messagebox.showinfo("Comandos Guardados", "Los comandos de VLAN han sido guardados en vlans.txt")

# Función para copiar los comandos VLAN al portapapeles
def copy_vlans():
    vlans_data = result_text.get(1.0, END)
    root.clipboard_clear()
    root.clipboard_append(vlans_data)
    root.update()
    messagebox.showinfo("VLANs Copiadas", "Los comandos de VLAN han sido copiados al portapapeles")

# Función para limpiar los campos y restablecer la interfaz
def clear_vlans():
    entry_vlans.delete(0, END)
    for entry in entry_vlan_names:
        entry.destroy()
    entry_vlan_names.clear()
    
    for label in label_vlan_names:
        label.destroy()
    label_vlan_names.clear()
    
    result_text.delete(1.0, END)
    button_ask.config(state=NORMAL)
    button_generate.config(state=DISABLED)
    button_clear.config(state=DISABLED)
    button_save.config(state=DISABLED)
    button_copy.config(state=DISABLED)

# Función para manejar el desplazamiento del mouse
def on_mousewheel(event):
    # Verifica si hay contenido fuera de la vista en la dirección del desplazamiento
    if canvas.bbox("all")[3] > canvas.winfo_height():
        canvas.yview_scroll(-1*(event.delta//120), "units")

# Crear la ventana principal
root = Tk()
root.title("VLAN Generator")

# Elementos de la interfaz de usuario
label_vlans = Label(root, text="Número de VLANs a generar:")
label_vlans.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_vlans = Entry(root)
entry_vlans.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

button_ask = Button(root, text="Siguiente", command=ask_for_vlans)
button_ask.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

canvas = Canvas(root)
canvas.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.grid(row=1, column=2, sticky="ns")

frame_vlan_names = Frame(canvas)
canvas.create_window((0, 0), window=frame_vlan_names, anchor="nw")

canvas.config(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))

entry_vlan_names = []
label_vlan_names = []

button_generate = Button(root, text="Generar VLANs", command=generate_vlans, state=DISABLED)
button_generate.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

button_save = Button(root, text="Guardar Comandos", command=save_vlans, state=DISABLED)
button_save.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

button_copy = Button(root, text="Copiar VLANs", command=copy_vlans, state=DISABLED)
button_copy.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

button_clear = Button(root, text="Borrar", command=clear_vlans, state=DISABLED)
button_clear.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

result_text = Text(root, height=10, width=40)
result_text.grid(row=1, column=3, rowspan=2, padx=5, pady=5, sticky="nsew")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# Vincular el evento de la rueda del mouse al desplazamiento en el canvas
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Loop principal
root.mainloop()
