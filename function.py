def convert_to_decimal(value):
    # Trasforma il valore in intero, se è float
    if isinstance(value, float):
        value = int(value)
    
    # Converte il valore in una stringa
    value_str = str(value)
    #print(f"Valore originale: {value_str}")  # Stampa il valore originale

    # Controlla se il numero è sufficientemente lungo
    if len(value_str) > 2:
        # Separa la parte intera dalla parte decimale
        integer_part = value_str[:-2]
        decimal_part = value_str[-2:]
    else:
        # Se il numero è corto, assume che sia tutto la parte decimale
        integer_part = '0'
        decimal_part = value_str.zfill(2)
    
    # Unisci le due parti con una virgola
    result = f"{integer_part},{decimal_part}"
    #print(f"Valore convertito: {result}")  # Stampa il valore convertito
    return result


#vedi file di testo cpi_calcolo_cumulati.txt per il funzionamento logico
def valida_condizione(campo, condizione):
    # Dividi la condizione in tre parti: campo1, operatore, valore
    parti = condizione.split('|')
    if len(parti) != 3:
        raise ValueError("La condizione non è nel formato corretto")

    campo1, operatore, valore = parti

    # Rimuovi spazi extra
    campo1 = campo1.strip()
    operatore = operatore.strip()
    valore = valore.strip()

    # Gestisci le operazioni supportate (es. =, >, <, >=, <=, <>)
    if operatore == '=':
        return campo == campo1 and campo1 == valore
    elif operatore == '>':
        try:
            return campo == campo1 and float(campo1) > float(valore)
        except ValueError:
            return False
    elif operatore == '<':
        try:
            return campo == campo1 and float(campo1) < float(valore)
        except ValueError:
            return False
    elif operatore == '>=':
        try:
            return campo == campo1 and float(campo1) >= float(valore)
        except ValueError:
            return False
    elif operatore == '<=':
        try:
            return campo == campo1 and float(campo1) <= float(valore)
        except ValueError:
            return False
    elif operatore == '<>':
        return campo == campo1 and campo1 != valore
    else:
        raise ValueError(f"Operatore non supportato: {operatore}")
    
    # Esempi di utilizzo:

    # Condizione: EA204(EA201|=|VALORE|)
    """ campo = "EA204"
    condizione = "EA201|=|VALORE|"
    valido = valida_condizione(campo, condizione)
    print(f"Il campo '{campo}' soddisfa la condizione '{condizione}': {valido}")

    # Condizione: DA201(DA301|>|0|)
    campo = "DA201"
    condizione = "DA301|>|0|"
    valido = valida_condizione(campo, condizione)
    print(f"Il campo '{campo}' soddisfa la condizione '{condizione}': {valido}") """