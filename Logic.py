import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import re
import os
from function import convert_to_decimal,valida_scelta_campo

# Importa il dizionario tag_descriptions dal modulo tag.py
from tag import tag_descriptions

# Colori personalizzati
COLOR_PRIMARY   = "#0F1626"  # Blu 
COLOR_SECONDARY = "#E6202F"  # Rosso 

# Variabili globali
ID101 = CA101 = ""
VA101 = CA201 = DA201 = CA305 = DA401 = DB401 = CA1002 = CA307 = CA403 = CA404 = 0
DA503 = DB503 = CA702 = CA706 = DA507 = DB507 = DB201 = TA201 = TA205 = DA301 = DB301 = DB505 = DA505 = 0
time = data = ""

# Set per tenere traccia dei tag inseriti nel Treeview
inserted_tags = set()

#funzione per azzerare le variabili globali
def azzera():
    global ID101, CA101, VA101, CA201, DA201, CA305, DA401, DB401, CA1002, CA307, CA403, CA404, time, data
    global DA503,DB503,CA702,CA706,DA507,DB507,DB201, TA201, TA205 , DA301 , DB301, DB505, DA505
    ID101 = CA101 = ""
    VA101 = CA201 = DA201 = CA305 = DA401 = DB401 = CA1002 = CA307 = CA403 = CA404 = 0
    DA503 = DB503 = CA702 = CA706 = DA507 = DB507 = DB201 = TA201 = TA205 = DA301 = DB301 = DB505 = DA505 = 0
    time = data = ""

# Funzione per la registrazione dei messaggi
def log(message):
    print(message)

# Funzione per creare e restituire gli elementi dell'interfaccia grafica
def crea_interfaccia(root):

    # Creazione della barra dei menu
    menu_bar = tk.Menu(root, bg=COLOR_PRIMARY, fg="white")
    root.config(menu=menu_bar)

    # Menu File
    file_menu = tk.Menu(menu_bar, tearoff=0, bg=COLOR_PRIMARY, fg="white")
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Apri", command=apri_file)
    file_menu.add_separator()
    file_menu.add_command(label="Esci", command=root.quit)

    # Menu Help
    help_menu = tk.Menu(menu_bar, tearoff=0, bg=COLOR_PRIMARY, fg="white")
    menu_bar.add_cascade(label="?", menu=help_menu)
    help_menu.add_command(label="Informazioni sullo sviluppatore", command=mostra_info_sviluppatore)

    # Frame per contenere il Treeview e la scrollbar
    frame = tk.Frame(root, bg=COLOR_PRIMARY)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Treeview per i tag audit
    style = ttk.Style()
    style.theme_use("default")

    style.configure("Treeview",
                    background=COLOR_PRIMARY,
                    foreground="white",
                    fieldbackground=COLOR_PRIMARY)
    style.configure("Treeview.Heading", background=COLOR_PRIMARY, foreground="white")

    style.map("Treeview", background=[('selected', COLOR_SECONDARY)])

    tag_tree = ttk.Treeview(frame, columns=("Tag", "Value", "Description"), show="headings", height=20, style="Treeview")
    tag_tree.heading("Tag", text="Tag")
    tag_tree.heading("Value", text="Value")
    tag_tree.heading("Description", text="Description")  # Intestazione per la nuova colonna

    # Scrollbar verticale per il Treeview
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tag_tree.yview)
    tag_tree.configure(yscrollcommand=scrollbar.set)

    # Creazione di tk.Text per le informazioni dettagliate
    info_text = tk.Text(frame, width=80, height=70, bg=COLOR_PRIMARY, fg="white", wrap=tk.WORD)
    info_text.config(state=tk.DISABLED)  # Imposta il widget in stato di sola lettura

    # Pack Treeview, Scrollbar e tk.Text
    tag_tree.pack(side=tk.LEFT, fill=tk.Y)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    info_text.pack(side=tk.LEFT, padx=10, fill=tk.Y)  # Sposta info_text a sinistra e aggiunge padding

    return tag_tree, frame, info_text

#funzione che legge il file audit selezionato
def leggi_file(dir_path, file_name):
    try:
        if os.path.exists(os.path.join(dir_path, file_name)):

            # Pulizia del Treeview prima di aggiungere nuovi dati
            pulisci_treeview()
            
            with open(os.path.join(dir_path, file_name), 'r') as reader:
                line_number = 1
                for line in reader:
                    line = line.strip()
                    if not line:
                        line_number += 1
                        continue
                    
                    parts = re.split(r"\*", line)
                    tag = parts[0]
                    
                    for i in range(1, len(parts)):
                        formatted_index = f"{i:02}"
                        selettore_tag(tag, formatted_index, parts[i])
                    
                    line_number += 1

            show_info_vending_machine_tag()
        else:
            log(f"Il file specificato non esiste: {os.path.join(dir_path, file_name)}")
    except Exception as e:
        log(f"Errore durante la lettura del file: {e}")

def pulisci_treeview():
    global tag_tree, inserted_tags
    for item in tag_tree.get_children():
        tag_tree.delete(item)
    inserted_tags.clear()

def show_info_vending_machine_tag():
    global ID101, CA101, VA101, CA201, DA201, CA305, DA401, DB401, CA1002, CA307, CA403, CA404, time, data
    global DA503,DB503,CA702,CA706,DA507,DB507,DB201, TA201, TA205 , DA301 , DB301, DB505, DA505
    
    try:
        VA101  = float(VA101)
        CA201  = float(CA201)
        DA201  = float(DA201)
        DB201  = float(DB201)
        CA305  = float(CA305)
        DA401  = float(DA401)
        DB401  = float(DB401)
        CA1002 = float(CA1002)
        CA307  = float(CA307)
        CA403  = float(CA403)
        CA404  = float(CA404)
        DA503  = float(DA503)
        DB503 = float(DB503)
        CA702  = float(CA702)
        CA706  = float(CA706)
        DA507  = float(DA507)
        DB507  = float(DB507)
        TA201  = float(TA201)
        TA205  = float(TA205)
        DA301  = float(DA301)
        DA301  = float(DB301)
        DB505  = float(DB505)
        DA505  = float(DA505)

        
        # EA302 e EA303 potrebbero già essere stringhe formattate correttamente, non necessitano di conversione
        time = time
        data = data
        
        if CA101 == "":
            id_gettoniera = ID101
        else:
            id_gettoniera = CA101

        cumulative_values = [
            ("DATI VENDING MACHINE",""),
            ("ID101: DATI DELLA MACCHINA", id_gettoniera),
            ("EA302: DATA DI QUESTA LETTURA", data),
            ("EA303: ORA DI QUESTA LETTURA", time),
            ("___________________________________________________________________",""),
            ("VALORI CUMULATI DELLA MACCHINA - NUOVA FORMULA",""),
            ("Venduto", f"{convert_to_decimal(VA101)}€"),
            ("VendutoContante", f"{convert_to_decimal(CA201)}€"),
            ("VendutoNoContante", f"{convert_to_decimal(DA201)}€"),
            ("Incassato", f"{convert_to_decimal(CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(DA401 + DB401)}€"),
            ("IncassatoVendita", f"{convert_to_decimal(CA305 - (DA401 + DB401) - CA1002)}€"),
            ("TotaleResoTubiResto", f"{convert_to_decimal(CA403)}€"),
            ("TotaleCaricatoTubiResto", f"{convert_to_decimal(CA307)}€"),
            ("TotaleResoManualeTubiResto", f"{convert_to_decimal(CA404)}€"),
            ("TotaleCaricatoManualeTubiResto", f"{convert_to_decimal(CA1002)}€"),
            ("___________________________________________________________________",""),
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA MEI | CPI",""),
            ("Venduto", f"{convert_to_decimal( (VA101-DA503-DB503-CA702) + (CA706+DA507+DB507) )}€"),
            ("VendutoContante", f"{convert_to_decimal( (CA201-CA702) + CA706 )}€"),
            ("VendutoNoContante", f"{convert_to_decimal( (DA201+DB201) - (DA503+TA201+TA205+DA507+DB507) )}€"),
            ("Incassato   ", f"{convert_to_decimal(CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(valida_scelta_campo(DA201,DA301,'>',0) + valida_scelta_campo(DB201,DB301,'>',0) + DA401 + DB401 - (DA301 - DB301 - DB505 - DA505))}€"),
            ("IncassatoVendita   ", f"{convert_to_decimal(CA305 - CA1002 - DA401 - DB401)}€"),
            ("TotaleResoTubiResto", f"{convert_to_decimal(CA403)}€"),
            ("TotaleCaricatoTubiResto", f"{convert_to_decimal(CA307)}€"),
            ("TotaleResoManualeTubiResto", f"{convert_to_decimal(CA404)}€"),
            ("TotaleCaricatoManualeTubiResto", f"{convert_to_decimal(CA1002)}€"),
        ]

        # Pulizia del widget tk.Text
        info_text.config(state=tk.NORMAL)
        info_text.delete("1.0", tk.END)

        for tag, value in cumulative_values:
            info_text.insert(tk.END, f"{tag}\n{value}\n")
        
        # Disabilita il widget per la sola lettura
        info_text.config(state=tk.DISABLED)
        
        # Azzeramento delle variabili
        azzera()
    
    except ValueError as e:
        log(f"Errore di conversione: {e}")

def lettura_tag(full_tag, initial_tag, part, i_max, j_max):
    global ID101, CA101, VA101, CA201, DA201, CA305, DA401, DB401, CA1002, CA307, CA403, CA404, time, data
    global DA503,DB503,CA702,CA706,DA507,DB507,DB201, TA201, TA205 , DA301 , DB301, DB505, DA505
    
    if full_tag == "EA302" and "EA302" not in inserted_tags:
        if len(part) >= 6:
            data = f"{part[4:6]}/{part[2:4]}/{part[0:2]}"
            description = tag_descriptions.get(full_tag, "Nessuna descrizione disponibile")
            tag_tree.insert("", tk.END, values=("EA302", data, description), tags=('custom_tag',))
            inserted_tags.add("EA302")
            
    if full_tag == "EA303" and "EA303" not in inserted_tags:
        if len(part) >= 4:
            time = f"{part[0:2]}:{part[2:4]}"
            description = tag_descriptions.get(full_tag, "Nessuna descrizione disponibile")
            tag_tree.insert("", tk.END, values=("EA303", time, description), tags=('custom_tag',))
            inserted_tags.add("EA303")

    if full_tag.startswith(initial_tag):
        for i in range(1, i_max + 1):
            if j_max > 0:
                for j in range(1, j_max + 1):
                    if full_tag not in inserted_tags:
                        description = tag_descriptions.get(full_tag, "Nessuna descrizione disponibile")
                        tag_tree.insert("", tk.END, values=(full_tag, part, description), tags=('custom_tag',))
                        inserted_tags.add(full_tag)
                    if full_tag == "ID101":
                        ID101 = part
                    elif full_tag == "VA101":
                        VA101 = float(part)
                    elif full_tag == "CA201":
                        CA201 = float(part)
                    elif full_tag == "CA101":
                        CA101 = part
                    elif full_tag == "DA503":
                        DA503 = float(part)
                    elif full_tag == "DB503":
                        DB503 = float(part)
                    elif full_tag == "CA702":
                        CA702 = float(part)
                    elif full_tag == "CA706":
                        CA706 = float(part)
                    elif full_tag == "DA507":
                        DA507 = float(part)
                    elif full_tag == "DB507":
                        DB507 = float(part)
                    elif full_tag == "DA201":
                        DA201 = float(part)
                    elif full_tag == "DB201":
                        DB201 = float(part)
                    elif full_tag == "CA305":
                        CA305 = float(part)
                    elif full_tag == "DA401":
                        DA401 = float(part)
                    elif full_tag == "DB401":
                        DB401 = float(part)
                    elif full_tag == "CA1002":
                        CA1002 = float(part)
                    elif full_tag == "CA307":
                        CA307 = float(part)
                    elif full_tag == "CA403":
                        CA403 = float(part)
                    elif full_tag == "CA404":
                        CA404 = float(part)
                    elif full_tag == "TA201":
                        TA201 = float(part)
                    elif full_tag == "TA205":
                        TA205 = float(part)
                    elif full_tag == "DA301":
                        DA301 = float(part)
                    elif full_tag == "DB301":
                        DB301 = float(part)
                    elif full_tag == "DB505":
                        DB505 = float(part)
                    elif full_tag == "DA505":
                        DA505 = float(part)
            else:
                if full_tag not in inserted_tags:
                    description = tag_descriptions.get(full_tag, "Nessuna descrizione disponibile")
                    tag_tree.insert("", tk.END, values=(full_tag, part, description), tags=('custom_tag',))
                    inserted_tags.add(full_tag)

def selettore_tag(tag, formatted_index, part):
    full_tag = tag + formatted_index
    lettura_tag(full_tag, "ID", part, 9, 11) , lettura_tag(full_tag, "ID1", part, 8, 10)
    lettura_tag(full_tag, "CA", part, 10, 8) , lettura_tag(full_tag, "MA", part, 9, 11)
    lettura_tag(full_tag, "PA", part, 8, 10) , lettura_tag(full_tag, "TA", part, 10, 8)
    lettura_tag(full_tag, "VA", part, 3, 9)  , lettura_tag(full_tag, "DXS", part, 6, 0)
    lettura_tag(full_tag, "ST", part, 2, 0)  , lettura_tag(full_tag, "LA", part, 5, 0)
    lettura_tag(full_tag, "AM", part, 5, 0)  , lettura_tag(full_tag, "SE", part, 2, 0)
    lettura_tag(full_tag, "DXE", part, 2, 0) , lettura_tag(full_tag, "G85", part, 1, 0)

#------------------------------------------------------------------------------------------------------------------------------
def apri_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        dir_path, file_name = os.path.split(file_path)
        leggi_file(dir_path, file_name)

def mostra_info_sviluppatore():
    info = """
    Developer   : Corrado Trigilia
    WorkPosition: Software Developer at Sisoft s.r.l.
    Località    : Catania, Sicily, Italy
    """
    messagebox.showinfo("Developer Information", info)

# Creazione della finestra principale
root = tk.Tk()
root.title("SIEVADTSOFT")
root.geometry("1200x700")
root.resizable(False, False)
root.configure(bg=COLOR_PRIMARY)

# Creazione dell'interfaccia grafica
tag_tree, frame, info_text = crea_interfaccia(root)

# Avvio della finestra
root.mainloop()
