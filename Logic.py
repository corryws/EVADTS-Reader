import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import re
import os
from variable_tag import GlobalState
from function import convert_to_decimal,valida_scelta_campo,mostra_info_sviluppatore,convertTagToData,convertTagToTime

# Importa il dizionario tag_descriptions dal modulo tag.py
from tag import tag_descriptions

# Colori personalizzati
COLOR_PRIMARY   = "#0F1626"  # Blu 
COLOR_SECONDARY = "#E6202F"  # Rosso 

# Set per tenere traccia dei tag inseriti nel Treeview
inserted_tags = set()

# Funzione per creare e restituire gli elementi dell'interfaccia grafica
def crea_interfaccia(root, state):
    # Creazione della barra dei menu
    menu_bar = tk.Menu(root, bg=COLOR_PRIMARY, fg="white")
    root.config(menu=menu_bar)

    # Menu File
    file_menu = tk.Menu(menu_bar, tearoff=0, bg=COLOR_PRIMARY, fg="white")
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Apri", command=lambda: apri_file(state))
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
    scrollbar_tree = ttk.Scrollbar(frame, orient="vertical", command=tag_tree.yview)
    tag_tree.configure(yscrollcommand=scrollbar_tree.set)

    # Creazione di tk.Text per le informazioni dettagliate
    info_text = tk.Text(frame, width=80, height=70, bg=COLOR_PRIMARY, fg="white", wrap=tk.WORD)
    info_text.config(state=tk.DISABLED)  # Imposta il widget in stato di sola lettura

    # Scrollbar verticale per il tk.Text
    scrollbar_text = ttk.Scrollbar(frame, orient="vertical", command=info_text.yview)
    info_text.configure(yscrollcommand=scrollbar_text.set)

    # Pack Treeview, Scrollbar e tk.Text
    tag_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar_tree.pack(side=tk.LEFT, fill=tk.Y)
    info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
    scrollbar_text.pack(side=tk.LEFT, fill=tk.Y)

    return tag_tree, frame, info_text

#funzione che legge il file audit selezionato
def leggi_file(dir_path, file_name,state):
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
                        selettore_tag(tag, formatted_index, parts[i],state)
                    
                    line_number += 1

            show_info_vending_machine_tag(state)
        else:
            print(f"Il file specificato non esiste: {os.path.join(dir_path, file_name)}")
    except Exception as e:
        print(f"Errore durante la lettura del file: {e}")

def pulisci_treeview():
    global tag_tree, inserted_tags
    for item in tag_tree.get_children():
        tag_tree.delete(item)
    inserted_tags.clear()

def RicavaMarcaModelloGettoniera(state):

    MarcaModello = ""

    # RICAVO MODELLO CPI
    if state.CA102 != "":
        if state.CA102 in ["CF8000EXEC", "CF8000MDB", "CF690", "CF6000EXEC", "EC6000MDB", "CF7900EXEC", "CF7900MDB"]:
            MarcaModello = "MEI|" + state.CA102

    # RICAVO MODELLO COGES
    if MarcaModello == "":
        if state.ID102 != "":
            if state.ID102 in ["93", "97", "77", "64", "76", "38", "30", "AETERNA", "85"]:
                MarcaModello = "COGES|" + state.ID102
        elif state.CA101.startswith("COG"):
            if state.CA403 == "":
                MarcaModello = "COGES|IDEA4COL"

    # RICAVO MODELLO PAYTEC
    if MarcaModello == "":
        if state.ID102 != "":
            if state.ID102.startswith("FAG"):
                MarcaModello = "PAYTEC|PAYTECV0"

    # RICAVO MODELLO SUZOHAPP
    if MarcaModello == "":
        if state.CA102 != "" and state.CA102.startswith("C2"):
            MarcaModello = "SUZ0HAPP|CURRENZA"
    
    if state.ID102 != "":
        if  state.ID102.startswith("WKL"):
            MarcaModello = "SUZ0HAPP|WORLDKEY"
        elif state.ID102.startswith("EKN"):
            MarcaModello = "SUZ0HAPP|EURO KEY NEXT"

    if state.ID705 != "":
        if  state.ID705.startswith("WKL"):
            MarcaModello = "SUZ0HAPP|WORLDKEY"
        elif state.ID705.startswith("EKN"):
            MarcaModello = "SUZ0HAPP|EURO KEY NEXT"

    # RICAVO MODELLO ELKEY
    if MarcaModello == "":
        if state.DA102 != "" and state.DA102.startswith("1"):
            MarcaModello = "ELKEY|BUBBLE"
        if state.DA102 != "" and state.DA102 == "ELK Bubble":
            MarcaModello = "ELKEY|BUBBLE"

    return MarcaModello

def show_info_vending_machine_tag(state):
    try:
        state.VA101  = float(state.VA101)
        state.CA201  = float(state.CA201)
        state.DA201  = float(state.DA201)
        state.DB201  = float(state.DB201)
        state.CA305  = float(state.CA305)
        state.DA401  = float(state.DA401)
        state.DB401  = float(state.DB401)
        state.CA1002 = float(state.CA1002)
        state.CA307  = float(state.CA307)
        state.CA403  = float(state.CA403)
        state.CA404  = float(state.CA404)
        state.DA503  = float(state.DA503)
        state.DB503  = float(state.DB503)
        state.CA702  = float(state.CA702)
        state.CA706  = float(state.CA706)
        state.DA507  = float(state.DA507)
        state.DB507  = float(state.DB507)
        state.TA201  = float(state.TA201)
        state.TA205  = float(state.TA205)
        state.DA301  = float(state.DA301)
        state.DB301  = float(state.DB301)
        state.DB505  = float(state.DB505)
        state.DA505  = float(state.DA505)
        state.CA102  = state.CA102
        state.EA301 = state.EA301
        state.EA302 = state.EA302
        state.EA303 = state.EA303
        state.EA305 = state.EA305
        state.EA306 = state.EA306
        state.ID102 = state.ID102
        state.ID705 = state.ID705
        state.DA102 = state.DA102

        if state.CA101 == "":
            id_gettoniera = state.ID101
        else:
            id_gettoniera = state.CA101

        cumulative_info_values = [
            ("DATI VENDING MACHINE",""),
            ("DATI DELLA GETTONIERA", id_gettoniera),
            ("MODELLO GETTONIERA", RicavaMarcaModelloGettoniera(state)),
            ("ProgressivoPrelievo", state.EA301),
            ("DATA DI QUESTA LETTURA", state.EA302),
            ("ORA DI QUESTA LETTURA", state.EA303),
            ("DataOraPrelievoPrecedente: ", state.EA305 + " " + state.EA306),
            ("___________________________________________________________________",""),
        ]

        cumulative_newformula_values = [
            ("VALORI CUMULATI DELLA MACCHINA - NUOVA FORMULA",""),
            ("Venduto", f"{convert_to_decimal(state.VA101)}€"),
            ("VendutoContante", f"{convert_to_decimal(state.CA201)}€"),
            ("VendutoNoContante", f"{convert_to_decimal(state.DA201)}€"),
            ("Incassato", f"{convert_to_decimal(state.CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(state.DA401 + state.DB401)}€"),
            ("IncassatoVendita", f"{convert_to_decimal(state.CA305 - (state.DA401 + state.DB401) - state.CA1002)}€"),
            ("___________________________________________________________________",""),
        ]

        cumulative_meiformula_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA MEI | CPI",""),
            ("Venduto", f"{convert_to_decimal( (state.VA101-state.DA503-state.DB503-state.CA702) + (state.CA706+state.DA507+state.DB507) )}€"),
            ("VendutoContante", f"{convert_to_decimal( (state.CA201-state.CA702) + state.CA706 )}€"),
            ("VendutoNoContante", f"{convert_to_decimal( (state.DA201+state.DB201) - (state.DA503+state.TA201+state.TA205+state.DA507+state.DB507) )}€"),
            ("Incassato   ", f"{convert_to_decimal(state.CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(valida_scelta_campo(state.DA201,state.DA301,'>',0) + valida_scelta_campo(state.DB201,state.DB301,'>',0) + state.DA401 + state.DB401 - (state.DA301 - state.DB301 - state.DB505 - state.DA505))}€"),
            ("IncassatoVendita   ", f"{convert_to_decimal(state.CA305 - state.CA1002 - state.DA401 - state.DB401)}€"),
            ("___________________________________________________________________",""),
        ]
        
        cumulative_mhdformula_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA MHD | MICROHARD",""),
            ("Venduto", f"{convert_to_decimal(state.VA101)}€"),
            ("VendutoContante", f"{convert_to_decimal( (state.CA201-state.CA702) + state.CA706 )}€"),
            ("VendutoNoContante", f"{convert_to_decimal( (state.DA201+state.DB201) - (state.DA503+state.TA201+state.TA205+state.DA507+state.DB507) )}€"),
            ("Incassato   ", f"{convert_to_decimal(state.CA305 + state.DA301 + state.DB301)}€"),
            ("IncassatoRicarica   ", f"{convert_to_decimal(state.DA401 + state.DB401)}€"),
            ("IncassatoVendita   ", f"{convert_to_decimal(state.CA305 - state.CA1002 - state.DA401 - state.DB401)}€"),
            ("___________________________________________________________________",""),
        ]
        
        cumulative_genericException_values = [
            ("VALORI CUMULATI DELLA MACCHINA IDENTICI PER TUTTE LE ECCEZIONI",""),
            ("TotaleResoTubiResto    ", f"{convert_to_decimal(state.DA503+state.DB503)}€"),
            ("TotalePrelevatoTubiResto   ", f"{convert_to_decimal(state.CA702)}€"),
            ("TotaleCaricatoTubiResto   ", f"{convert_to_decimal(state.CA706+state.DA507+state.DB507)}€"),
            ("TotaleIncassatoMeccanico   ", f"{convert_to_decimal(state.DA301+state.DB301)}€"),
            ("TotaleIncassatoBillValidator   ", f"{convert_to_decimal(state.DA505+state.DB505)}€")
        ]

        cumulative_values = cumulative_info_values + cumulative_newformula_values + cumulative_meiformula_values

        """ aggiungere qui le somme in base al modello della gettoniera uscito """


        cumulative_values = cumulative_values + cumulative_genericException_values

        # Pulizia del widget tk.Text
        info_text.config(state=tk.NORMAL)
        info_text.delete("1.0", tk.END)

        for tag, value in cumulative_values:
            info_text.insert(tk.END, f"{tag}\n{value}\n")
        
        # Disabilita il widget per la sola lettura
        info_text.config(state=tk.DISABLED)
        
        # Azzeramento delle variabili
        state.azzera()
    
    except ValueError as e:
        print(f"Errore di conversione: {e}")

def lettura_tag(full_tag, initial_tag, part, i_max, j_max,state):

    for i in range(1, i_max + 1):
        if j_max > 0:
            for j in range(1, j_max + 1):
                if full_tag not in inserted_tags:
                    description = tag_descriptions.get(full_tag, "Nessuna descrizione disponibile")
                    tag_tree.insert("", tk.END, values=(full_tag, part, description), tags=('custom_tag',))
                    inserted_tags.add(full_tag)
                    if full_tag == "ID101":
                        state.ID101 = part
                    if full_tag == "ID102":
                        state.ID102 = part
                    if full_tag == "ID705":
                        state.ID705 = part
                    elif full_tag == "VA101":
                        state.VA101 = float(part)
                    if full_tag == "ID101":
                        state.ID101 = part
                    elif full_tag == "EA301":
                        state.EA301 = part
                    elif full_tag == "EA302":
                        if len(part) >= 6:
                            state.EA302 = convertTagToData(part)
                    elif full_tag == "EA303":
                        if len(part) >= 4:
                            state.EA303 = convertTagToTime(part)
                    elif full_tag == "EA305":
                        if len(part) >= 6:
                            state.EA305 = convertTagToData(part)
                    elif full_tag == "EA306":
                        if len(part) >= 4:
                            state.EA306 = convertTagToTime(part)
                    elif full_tag == "CA101":
                        state.CA101 = part
                    elif full_tag == "CA102":
                        state.CA102 = part
                    elif full_tag == "DA503":
                        state.DA503 = float(part)
                    elif full_tag == "DB503":
                        state.DB503 = float(part)
                    elif full_tag == "CA702":
                        state.CA702 = float(part)
                    elif full_tag == "CA706":
                        state.CA706 = float(part)
                    elif full_tag == "DA507":
                        state.DA507 = float(part)
                    elif full_tag == "DB507":
                        state.DB507 = float(part)
                    elif full_tag == "DA201":
                        state.DA201 = float(part)
                    elif full_tag == "DB201":
                        state.DB201 = float(part)
                    elif full_tag == "CA305":
                        state.CA305 = float(part)
                    elif full_tag == "DA102":
                        state.DA102 = float(part)
                    elif full_tag == "DA401":
                        state.DA401 = float(part)
                    elif full_tag == "DB401":
                        state.DB401 = float(part)
                    elif full_tag == "CA1002":
                        state.CA1002 = float(part)
                    elif full_tag == "CA307":
                        state.CA307 = float(part)
                    elif full_tag == "CA403":
                        state.CA403 = float(part)
                    elif full_tag == "CA404":
                        state.CA404 = float(part)
                    elif full_tag == "TA201":
                        state.TA201 = float(part)
                    elif full_tag == "TA205":
                        state.TA205 = float(part)
                    elif full_tag == "DA301":
                        state.DA301 = float(part)
                    elif full_tag == "DB301":
                        state.DB301 = float(part)
                    elif full_tag == "DB505":
                        state.DB505 = float(part)
                    elif full_tag == "DA505":
                        state.DA505 = float(part)
                else:
                    if full_tag not in inserted_tags:
                        description = tag_descriptions.get(full_tag, "Nessuna descrizione disponibile")
                        tag_tree.insert("", tk.END, values=(full_tag, part, description), tags=('custom_tag',))
                        inserted_tags.add(full_tag)

def selettore_tag(tag, formatted_index, part, state):
    full_tag = tag + formatted_index
    lettura_tag(full_tag, "ID", part, 9, 11,state) , lettura_tag(full_tag, "ID1", part, 8, 10,state)
    lettura_tag(full_tag, "EA", part, 9, 10,state)
    lettura_tag(full_tag, "CA", part, 10, 8,state) , lettura_tag(full_tag, "MA", part, 9, 11,state)
    lettura_tag(full_tag, "PA", part, 8, 10,state) , lettura_tag(full_tag, "TA", part, 10, 8,state)
    lettura_tag(full_tag, "VA", part, 3, 9,state)  , lettura_tag(full_tag, "DXS", part, 6, 0,state)
    lettura_tag(full_tag, "ST", part, 2, 0,state)  , lettura_tag(full_tag, "LA", part, 5, 0,state)
    lettura_tag(full_tag, "AM", part, 5, 0,state)  , lettura_tag(full_tag, "SE", part, 2, 0,state)
    lettura_tag(full_tag, "DXE", part, 2, 0,state) , lettura_tag(full_tag, "G85", part, 1, 0,state)

#------------------------------------------------------------------------------------------------------------------------------
def apri_file(state):
    file_path = filedialog.askopenfilename()
    if file_path:
        dir_path, file_name = os.path.split(file_path)
        leggi_file(dir_path, file_name,state)

# Creazione della finestra principale
root = tk.Tk()
root.title("SIEVADTSOFT")
root.geometry("1200x700")
root.resizable(False, False)
root.configure(bg=COLOR_PRIMARY)
global_state = GlobalState()

# Creazione dell'interfaccia grafica
tag_tree, frame, info_text = crea_interfaccia(root,global_state)

# Avvio della finestra
root.mainloop()
