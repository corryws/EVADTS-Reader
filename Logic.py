import tkinter as tk
from tkinter import filedialog, ttk
import re
import os
from variable_tag import GlobalState
from function import mostra_info_sviluppatore, convertTagToData,convertTagToTime

# Importa il dizionario tag_descriptions dal modulo tag.py
from tag import tag_descriptions

# Colori personalizzati
COLOR_PRIMARY   = "#0F1626" 
COLOR_SECONDARY = "#E6202F"

# Set per tenere traccia dei tag inseriti nel Treeview
inserted_tags = set()

def show_info_vending_machine_tag(state):
    try:
        # Ensure numerical values are converted correctly
        state.CA1002 = float(state.CA1002)
        state.CA201  = float(state.CA201)
        state.CA305  = float(state.CA305)
        state.CA307  = float(state.CA307)
        state.CA403  = float(state.CA403)
        state.CA404  = float(state.CA404)
        state.CA702  = float(state.CA702)
        state.CA706  = float(state.CA706)
        state.CA802  = float(state.CA802)
        state.DA201  = float(state.DA201)
        state.DA301  = float(state.DA301)
        state.DA401  = float(state.DA401)
        state.DA503  = float(state.DA503)
        state.DA505  = float(state.DA505)
        state.DA507  = float(state.DA507)
        state.DA601  = float(state.DA601)
        state.DB201  = float(state.DB201)
        state.DB301  = float(state.DB301)
        state.DB401  = float(state.DB401)
        state.DB503  = float(state.DB503)
        state.DB505  = float(state.DB505)
        state.DB507  = float(state.DB507)
        state.DB601  = float(state.DB601)
        state.TA201  = float(state.TA201)
        state.TA205  = float(state.TA205)
        state.VA101  = float(state.VA101)
        state.VA301  = float(state.VA301)

        # Ensure string values are indeed strings
        state.DA102  = str(state.DA102)
        state.DXS03  = str(state.DXS03)
        state.EA301  = str(state.EA301)
        state.EA302  = str(state.EA302)
        state.EA303  = str(state.EA303)
        state.EA305  = str(state.EA305)
        state.EA306  = str(state.EA306)
        state.ID102  = str(state.ID102)
        state.ID705  = str(state.ID705)
        state.MA502  = str(state.MA502)
        state.CA101  = str(state.CA101)
        state.DXS01  = str(state.DXS01)

        if state.CA101 == "":
            id_gettoniera = state.ID101
        else:
            id_gettoniera = state.CA101
        
        #MarcaModello = state.RicavaMarcaModelloGettoniera_()
        MarcaModello = str(state.RicavaMarcaModelloGettoniera_())  # Assicurarsi che sia una stringa
        print(MarcaModello)

        cumulative_info_values = [
            ("DATI VENDING MACHINE",""),
            ("DATI DELLA GETTONIERA", id_gettoniera),
            ("MODELLO GETTONIERA", MarcaModello),
            ("ProgressivoPrelievo", state.EA301),
            ("DATA DI QUESTA LETTURA", state.EA302),
            ("ORA DI QUESTA LETTURA", state.EA303),
            ("DataOraPrelievoPrecedente: ", state.EA305 + " " + state.EA306),
            ("___________________________________________________________________",""),
        ]

        cumulative_values = cumulative_info_values + state.returnNewFormulaList() + state.returnMeiFormulaList()

        """ aggiungere qui le somme in base al modello della gettoniera uscito """
        #Controllo Marca Modello
        # Aggiunta di controlli per tutte le variazioni di MarcaModello

        if MarcaModello.startswith("COGES|"):
             if state.DXS03.startswith("V0"):
                cumulative_values = cumulative_values + state.returnCogformulav0List()
             elif state.DXS03.startswith("V1"):
                 cumulative_values = cumulative_values + state.returnCogformulav1List()
             elif state.DXS03.startswith("V2"):
                 cumulative_values = cumulative_values + state.returnCogformulav2List()
             elif state.DXS03.startswith("V3"):
                 cumulative_values = cumulative_values + state.returnCogformulav3List()
             elif state.DXS03.startswith("V4"):
                 cumulative_values = cumulative_values + state.returnCogformulav4List()

        elif id_gettoniera.startswith("FAG"):
            if MarcaModello.startswith("PAYTEC|PAYTECV0"):
                pass
            elif MarcaModello.startswith("PAYTEC|PAYTECV1"):
                pass
            elif MarcaModello.startswith("PAYTEC|PAYTECV2"):
                pass
            elif MarcaModello.startswith("PAYTEC|PAYTECV3"):
                pass
            elif MarcaModello.startswith("PAYTEC|PAYTECV4"):
                pass
            pass

        elif MarcaModello.startswith("SUZ0HAPP|"):
            # Fai qualcosa se MarcaModello è "SUZ0HAPP|CURRENZA"
            cumulative_values = cumulative_values + state.returnNriformulaList()
            pass

        elif MarcaModello == "ELKEY|BUBBLE":
            # Fai qualcosa se MarcaModello è "ELKEY|BUBBLE"
            cumulative_values = cumulative_values + state.returnElkformulaList()
            pass

        cumulative_values = cumulative_values + state.returnGenericExceptionList()

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
        print(f"Errore di conversione: {e} {ValueError}")

def lettura_tag(full_tag, initial_tag, part, i_max, j_max,state):

    for i in range(1, i_max + 1):
        for j in range(1, j_max + 1):
            if full_tag not in inserted_tags:
                description = tag_descriptions.get(full_tag, "Nessuna descrizione disponibile")
                tag_tree.insert("", tk.END, values=(full_tag, part, description), tags=('custom_tag',))
                print(full_tag)
                inserted_tags.add(full_tag)
                
                # Mapping tags to state attributes
                tag_to_state_mapping = {
                    "DXS01": "DXS01",
                    "DXS03": "DXS03",
                    "ID101": "ID101",
                    "ID102": "ID102",
                    "ID705": "ID705",
                    "VA101": ("VA101", float),
                    "VA301": ("VA301", float),
                    "EA301": "EA301",
                    "EA302": ("EA302", convertTagToData),
                    "EA303": ("EA303", convertTagToTime),
                    "EA305": ("EA305", convertTagToData),
                    "EA306": ("EA306", convertTagToTime),
                    "MA502": "MA502",
                    "CA101": "CA101",
                    "CA102": "CA102",
                    "CA802": "CA802",
                    "DA503": ("DA503", float),
                    "DB503": ("DB503", float),
                    "CA702": ("CA702", float),
                    "CA706": ("CA706", float),
                    "DA507": ("DA507", float),
                    "DB507": ("DB507", float),
                    "DA201": ("DA201", float),
                    "DB201": ("DB201", float),
                    "CA305": ("CA305", float),
                    "DA102": "DA102",
                    "DA401": ("DA401", float),
                    "DA601": ("DA601", float),
                    "DB401": ("DB401", float),
                    "DB601": ("DB601", float),
                    "CA1002": ("CA1002", float),
                    "CA307": ("CA307", float),
                    "CA403": ("CA403", float),
                    "CA404": ("CA404", float),
                    "TA201": ("TA201", float),
                    "TA205": ("TA205", float),
                    "DA301": ("DA301", float),
                    "DB301": ("DB301", float),
                    "DB505": ("DB505", float),
                    "DA505": ("DA505", float),
                }

                if full_tag in tag_to_state_mapping:
                    value = part
                    if isinstance(tag_to_state_mapping[full_tag], tuple):
                        attribute, converter = tag_to_state_mapping[full_tag]
                        if len(part) >= 4 if "Time" in converter.__name__ else 6:
                            value = converter(part)
                    else:
                        attribute = tag_to_state_mapping[full_tag]
                    setattr(state, attribute, value)

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


#FUNZIONE INERENTI ALLA APERTURA E LETTURA-------------------------------------------------------------------------------------
def apri_file(state):
    file_path = filedialog.askopenfilename()
    if file_path:
        dir_path, file_name = os.path.split(file_path)
        leggi_file(dir_path, file_name,state)

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
#------------------------------------------------------------------------------------------------------------------------------


#FUNZIONE INERENTI ALLA GESTIONE FINESTRA--------------------------------------------------------------------------------------
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


def pulisci_treeview():
    global tag_tree, inserted_tags
    for item in tag_tree.get_children():
        tag_tree.delete(item)
    inserted_tags.clear()


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
#------------------------------------------------------------------------------------------------------------------------------