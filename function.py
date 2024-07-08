from tkinter import messagebox


def convert_to_decimal(value):
    # Trasforma il valore in intero, se è float
    if isinstance(value, float):
        value = int(value)
    
    # Converte il valore in una stringa
    value_str = str(value)

    # Controlla se il numero è sufficientemente lungo
    if len(value_str) > 2:
        integer_part = value_str[:-2]
        decimal_part = value_str[-2:]
    else:
        integer_part = '0'
        decimal_part = value_str.zfill(2)
    
    # Unisci le due parti con una virgola
    result = f"{integer_part},{decimal_part}"
    return result

def convertTagToData(part):
    return f"{part[4:6]}/{part[2:4]}/{part[0:2]}"

def convertTagToTime(part):
    return f"{part[0:2]}:{part[2:4]}"


""" es. DA201(DA301|>|0|)
prendi DA201 solo se DA301 è > a 0 """   
#      campo,seleziona,condizione,valore
""" es. DA201(DA301|      >        |0|)"""
def valida_scelta_campo(campo,seleziona,condizione,valore):
    #Logica: es. DA201(DA301|>|0|) seleziona DA201 solo se DA301 è > a 0

    #prendi campo solo se seleziona è condizione a valore

    if condizione == "=":
        if seleziona == valore:
            return campo
        else: return 0
    
    if condizione == ">":
        if seleziona > valore:
            return campo
        else: return 0

    if condizione == "<":
        if seleziona < valore:
            return campo
        else: return 0
    
    if condizione == ">=":
        if seleziona >= valore:
            return campo
        else: return 0

    if condizione == "<=":
        if seleziona <= valore:
            return campo
        else: return 0

    if condizione == "<>":
        if seleziona != valore:
            return campo
        else: return 0

def mostra_info_sviluppatore():
    info = """
    Developer   : Corrado Trigilia
    WorkPosition: Software Developer at Sisoft s.r.l.
    """
    messagebox.showinfo("Developer Information", info)

    