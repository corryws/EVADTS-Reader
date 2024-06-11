import tkinter as tk
from tag import tag_descriptions
from tkinter import ttk, filedialog

# Questa funzione prende una lista di stringhe separate da '*',
# organizza e formatta le sottostringhe basate sul loro identificatore iniziale,
# restituendo un dizionario con le stringhe formattate.
def format_strings(string_list):
    formatted_output = {}
    
    for initial_string in string_list:
        parts = initial_string.split('*')
        base_identifier = parts[0]
        
        if base_identifier not in formatted_output:
            formatted_output[base_identifier] = []
        
        for i, part in enumerate(parts[1:], start=1):
            formatted_output[base_identifier].append(f"{base_identifier} {i:02} {part.strip()}")
    
    return formatted_output

# Questa funzione apre un file di testo selezionato dall'utente, legge le stringhe dal file,
# le formatta usando la funzione `format_strings`, e aggiorna una Treeview con le stringhe formattate.
def process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    
    with open(file_path, 'r') as file:
        string_list = file.readlines()
        text_box.insert(tk.END, ''.join(string_list))
    
    # Formatta le stringhe
    formatted_strings = format_strings(string_list)
    
    # Pulisci la Treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Inserisci le stringhe formattate nella Treeview
    for key, values in formatted_strings.items():
        tag_description = tag_descriptions.get(key, '')
        parent = tree.insert("", tk.END, text=f"{key} - {tag_description}")
        for value in values:
            tree.insert(parent, tk.END, text=value)


# Questa funzione crea e configura la finestra principale dell'applicazione,
# aggiunge un menu per selezionare un file e una Treeview per visualizzare
# l'output formattato, e avvia il loop principale dell'interfaccia grafica.
def create_main_window():
    window = tk.Tk()
    window.title("EVA-DTS READER")
    window.geometry("800x600")

    # Creazione del menu
    menu_bar = tk.Menu(window)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Seleziona Audit.txt", command=process_file)
    menu_bar.add_cascade(label="File", menu=file_menu)
    window.config(menu=menu_bar)

    # Aggiungi un nuovo widget Text per contenere string_list
    global text_box
    text_box = tk.Text(window, height=33, width=60)
    text_box.configure(state='normal')
    text_box.place(x=0, y=20)  # Posiziona la casella di testo

    #Creazione del TreeView
    global tree
    tree = ttk.Treeview(window,height=25)
    tree.column('#0', width=200)
    tree.heading('#0', text='EVADTSTAG')
    tree.place(x=500,y=20)

    # Avvio del loop principale
    window.mainloop()