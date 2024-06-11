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
# aggiunge un pulsante per selezionare un file e una Treeview per visualizzare
# l'output formattato, e avvia il loop principale dell'interfaccia grafica.
def create_main_window():
    window = tk.Tk()
    window.title("EVA-DTS READER")
    window.geometry("800x600")

    file_button = tk.Button(window, text="Seleziona File", command=process_file)
    file_button.pack(pady=5)

    global tree
    tree = ttk.Treeview(window)
    tree.pack(expand=True, fill='both', padx=10, pady=10)

    tree.heading('#0', text='EVADTS TAG')

    # Avvio del loop principale
    window.mainloop()