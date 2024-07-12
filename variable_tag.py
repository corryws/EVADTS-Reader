from function import convert_to_decimal, valida_scelta_campo


class GlobalState:
    def __init__(self):
        self.CA1002 = self.CA101 = self.CA102 = self.CA201 = self.CA305 = self.CA307 = self.CA403 = self.CA404 = self.CA702 = self.CA706 = self.CA802 = 0
        self.DA102 = self.DA201 = self.DA301 = self.DA401 = self.DA503 = self.DA505 = self.DA507 = self.DA601 = 0
        self.DB201 = self.DB301 = self.DB401 = self.DB503 = self.DB505 = self.DB507 = self.DB601 = 0
        self.DXS01 = self.DXS03 = ""
        self.EA301 = self.EA302 = self.EA303 = self.EA305 = self.EA306 = ""
        self.ID101 = self.ID102 = self.ID705 = ""
        self.MA502 = ""
        self.TA201 = self.TA205 = 0
        self.VA101 = self.VA301 = 0

    def azzera(self):
        self.CA1002 = self.CA101 = self.CA102 = self.CA201 = self.CA305 = self.CA307 = self.CA403 = self.CA404 = self.CA702 = self.CA706 = self.CA802 = 0
        self.DA102 = self.DA201 = self.DA301 = self.DA401 = self.DA503 = self.DA505 = self.DA507 = self.DA601 = 0
        self.DB201 = self.DB301 = self.DB401 = self.DB503 = self.DB505 = self.DB507 = self.DB601 = 0
        self.DXS01 = self.DXS03 = ""
        self.EA301 = self.EA302 = self.EA303 = self.EA305 = self.EA306 = ""
        self.ID101 = self.ID102 = self.ID705 = ""
        self.MA502 = ""
        self.TA201 = self.TA205 = 0
        self.VA101 = self.VA301 = 0


    def returnNewFormulaList(self):
        cumulative_newformula_values = [
            ("VALORI CUMULATI DELLA MACCHINA - NUOVA FORMULA",""),
            ("Venduto", f"{convert_to_decimal(self.VA101 - self.DA503 - self.DB503 - self.CA702)}€"),
            ("VendutoContante", f"{convert_to_decimal(self.CA201)}€"),
            ("VendutoNoContante", f"{convert_to_decimal(self.DA201)}€"),
            ("Incassato", f"{convert_to_decimal(self.CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(self.DA401 + self.DB401)}€"),
            ("IncassatoVendita", f"{convert_to_decimal(self.CA305 - (self.DA401 + self.DB401) - self.CA1002)}€"),
            ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA",""),
            ("Venduto", "VA101-DA503-DB503-CA702"),
            ("VendutoContante", "CA201"),
            ("VendutoNoContante", "DA201"),
            ("Incassato", "CA305"),
            ("IncassatoRicarica", "DA401 + DB401"),
            ("IncassatoVendita", "CA305 - CA1002 - DA401 - DB401"),
            ("___________________________________________________________________",""),
        ]
        return cumulative_newformula_values
    
    def returnMeiFormulaList(self):
        cumulative_meiformula_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA MEI | CPI - GENERICO",""),
            ("Venduto", f"{convert_to_decimal( (self.VA101-self.DA503-self.DB503-self.CA702) + (self.CA706+self.DA507+self.DB507) )}€"),
            ("VendutoContante", f"{convert_to_decimal( (self.CA201-self.CA702) + self.CA706 )}€"),
            ("VendutoNoContante", f"{convert_to_decimal( (self.DA201+self.DB201) - (self.DA503+self.TA201+self.TA205+self.DA507+self.DB507) )}€"),
            ("Incassato   ", f"{convert_to_decimal(self.CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(valida_scelta_campo(self.DA201,self.DA301,'>',0) + valida_scelta_campo(self.DB201,self.DB301,'>',0) + self.DA401 + self.DB401 - (self.DA301 - self.DB301 - self.DB505 - self.DA505))}€"),
            ("IncassatoVendita   ", f"{convert_to_decimal(self.CA305 - self.CA1002 - self.DA401 - self.DB401)}€"),
            ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA MEI", ""),
            ("Venduto", "VA101 - DA503 - DB503 - CA702 + CA706 + DA507 + DB507"),
            ("VendutoContante", "CA201 - CA702 + CA706"),
            ("VendutoNoContante", "DA201 + DB201 - DA503 - DB503 + TA201 + TA205 + DA507 + DB507"),
            ("Incassato", "CA305"),
            ("IncassatoRicarica", "DA401 + DB401"),
            ("IncassatoVendita", "CA305 - CA1002 - DA401 + DB401"),
            ("___________________________________________________________________",""),
        ]
        return cumulative_meiformula_values
    
    def returnNriformulaList(self):
        cumulative_nriformula_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA NRI | SUZOHAPP", ""),
            ("Venduto", f"{convert_to_decimal((self.VA101 - self.DA503 - self.DB503))}€"),
            ("VendutoContante", f"{convert_to_decimal((self.CA201 - self.CA702) + self.CA706)}€"),
            ("VendutoNoContante", f"{convert_to_decimal((self.DA201 + self.DB201) - (self.DA503 - self.DB503) + self.TA201 + self.TA205)}€"),
            ("Incassato", f"{convert_to_decimal(self.CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(valida_scelta_campo(self.DA201, self.DA301, '>', 0) + valida_scelta_campo(self.DB201, self.DB301, '>', 0) + self.DA401 + self.DB401 - (self.DA301 - self.DB301 - self.DA503 - self.DB503 - self.DA601 - self.DB601))}€"),
            ("IncassatoVendita", f"{convert_to_decimal(self.CA305 - self.CA1002 - self.DA401 - self.DB401)}€"),
            ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA NRI | SUZ0HAPP", ""),
            ("Venduto", "VA101 - DA503 - DB503"),
            ("VendutoContante", "CA201 - CA702 + CA706"),
            ("VendutoNoContante", "DA201 + DB201 - DA503 - DB503 + TA201 + TA205"),
            ("Incassato", "CA305"),
            ("IncassatoRicarica", "DA201(DA301 > 0) + DB201(DB301 > 0) + DA401 + DB401 - DA301 - DB301 - DA503 - DB503 - DA601 - DB601"),
            ("IncassatoVendita", "CA305 - CA1002 - DA401 - DB401"),
            ("___________________________________________________________________", ""),
        ]
        return cumulative_nriformula_values

    def returnMhdformulaList(self):
        cumulative_mhdformula_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA MHD | MICROHARD", ""),
            ("Venduto", f"{convert_to_decimal(self.VA101)}€"),
            ("VendutoContante", f"{convert_to_decimal((self.CA201 - self.CA702) + self.CA706)}€"),
            ("VendutoNoContante", f"{convert_to_decimal((self.DA201 + self.DB201) - (self.DA503 + self.TA201 + self.TA205 + self.DA507 + self.DB507))}€"),
            ("Incassato", f"{convert_to_decimal(self.CA305 + self.DA301 + self.DB301)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(self.DA401 + self.DB401)}€"),
            ("IncassatoVendita", f"{convert_to_decimal(self.CA305 - self.CA1002 - self.DA401 - self.DB401)}€"),
            ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA MHD | MICROHARD", ""),
            ("Venduto", "VA101"),
            ("VendutoContante", "CA201 - CA702 + CA706"),
            ("VendutoNoContante", "DA201 + DB201 - DA503 - DB503 + TA201 + TA205 + DA507 + DB507"),
            ("Incassato", "CA305 + DA301 + DB301"),
            ("IncassatoRicarica", "DA401 + DB401"),
            ("IncassatoVendita", "CA305 - CA1002 - DA401 - DB401"),
            ("___________________________________________________________________", ""),
        ]
        return cumulative_mhdformula_values
    
#ECCEZIONE ELK-------------------------------------------------------------------------------
    def returnElkformulaList(self):
            cumulative_elkformula_values = [
                ("VALORI CUMULATI DELLA MACCHINA - FORMULA ELK | MICROHARD", ""),
                ("Venduto", f"{convert_to_decimal(self.VA101)}€"),
                ("VendutoContante", f"{convert_to_decimal((self.CA201))}€"),
                ("VendutoNoContante", f"{convert_to_decimal((self.DA201 + self.DB201))}€"),
                ("Incassato", f"{convert_to_decimal(self.CA305)}€"),
                ("IncassatoRicarica", f"{convert_to_decimal((self.CA305 - self.CA201 - self.CA403) + self.CA404 - (self.CA802))}€"),
                ("IncassatoVendita", f"{convert_to_decimal((self.CA201 + self.CA403) - self.CA404 + (self.CA802))}€"),
                ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA ELK | ELKEY BUBBLE", ""),
                ("Venduto", "VA101"),
                ("VendutoContante", "CA201"),
                ("VendutoNoContante", "DA201 + DB201"),
                ("Incassato", "CA305"),
                ("IncassatoRicarica", "CA305 - CA201 - CA403 + CA404 - CA802"),
                ("IncassatoVendita", "CA201 + CA403 - CA404 + CA802"),
                ("___________________________________________________________________", ""),
            ]
            return cumulative_elkformula_values

#ECCEZIONI COGES-----------------------------------------------------------------------------
    def returnCogformulav0List(self):
        cumulative_cogformulav0_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA COG | COGES V0", ""),
            ("Venduto", f"{convert_to_decimal(self.VA101 + self.VA301)}€"),
            ("VendutoContante", f"{convert_to_decimal(self.CA201)}€"),
            ("VendutoNoContante", f"{convert_to_decimal(self.VA101 + self.CA201)}€"),
            ("Incassato", f"{convert_to_decimal(self.CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal((self.DA401 + self.DA601) - (self.DB401 - self.DB601))}€"),
            ("IncassatoVendita", f"{convert_to_decimal((self.CA305 - self.CA1002 - self.DA401) + (self.DA601) - self.DB401 + (self.DB601))}€"),
            ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA COG | COGES V0", ""),
            ("Venduto", "VA101 + VA301"),
            ("VendutoContante", "CA201"),
            ("VendutoNoContante", "VA101 + CA201"),
            ("Incassato", "CA305"),
            ("IncassatoRicarica", "DA401 - DA601 + DB401 - DB601"),
            ("IncassatoVendita", "CA305 - CA1002 - DA401 + DA601 - DB401 + DB601"),
            ("___________________________________________________________________", ""),
        ]
        return cumulative_cogformulav0_values

    def returnCogformulav1List(self):
        cumulative_cogformulav1_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA COG | COGES V1", ""),
            ("Venduto", f"{convert_to_decimal(self.VA101 + self.VA301)}€"),
            ("VendutoContante", f"{convert_to_decimal(self.CA201)}€"),
            ("VendutoNoContante", f"{convert_to_decimal(self.VA101 + self.CA201)}€"),
            ("Incassato", f"{convert_to_decimal(self.CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(self.DA401 + self.DA601)}€"),
            ("IncassatoVendita", f"{convert_to_decimal((self.CA305 - self.CA1002 - self.DA401) + (self.DA601))}€"),
            ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA COG | COGES V1", ""),
            ("Venduto", "VA101 + VA301"),
            ("VendutoContante", "CA201"),
            ("VendutoNoContante", "VA101 + CA201"),
            ("Incassato", "CA305"),
            ("IncassatoRicarica", "DA401 - DA601"),
            ("IncassatoVendita", "CA305 - CA1002 - DA401 + DA601"),
            ("___________________________________________________________________", ""),
        ]
        return cumulative_cogformulav1_values

    def returnCogformulav2List(self):
        cumulative_cogformulav2_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA COG | COGES V2", ""),
            ("Venduto", f"{convert_to_decimal(self.VA101)}€"),
            ("VendutoContante", f"{convert_to_decimal(self.CA201)}€"),
            ("VendutoNoContante", f"{convert_to_decimal(self.VA101 + self.CA201)}€"),
            ("Incassato", f"{convert_to_decimal(self.CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(self.DA401)}€"),
            ("IncassatoVendita", f"{convert_to_decimal((self.CA305 - self.DA401) + (self.DA601))}€"),
            ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA COG | COGES V2", ""),
            ("Venduto", "VA101"),
            ("VendutoContante", "CA201"),
            ("VendutoNoContante", "VA101 + CA201"),
            ("Incassato", "CA305"),
            ("IncassatoRicarica", "DA401"),
            ("IncassatoVendita", "CA305 - DA401 + DA601"),
            ("___________________________________________________________________", ""),
        ]
        return cumulative_cogformulav2_values
    
    def returnCogformulav3List(self):
        cumulative_cogformulav3_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA COG | COGES V3", ""),
            ("Venduto", f"{convert_to_decimal(self.VA101 + self.VA301)}€"),
            ("VendutoContante", f"{convert_to_decimal(self.CA201)}€"),
            ("VendutoNoContante", f"{convert_to_decimal(self.VA101 + self.CA201)}€"),
            ("Incassato", f"{convert_to_decimal(self.CA305 + self.CA1002)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(self.DA401 - self.DA601)}€"),
            ("IncassatoVendita", f"{convert_to_decimal((self.CA305 - self.DA401) + (self.DA601))}€"),
            ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA COG | COGES V3", ""),
            ("Venduto", "VA101 + VA301"),
            ("VendutoContante", "CA201"),
            ("VendutoNoContante", "VA101 + CA201"),
            ("Incassato", "CA305 + CA1002"),
            ("IncassatoRicarica", "DA401 - DA601"),
            ("IncassatoVendita", "CA305 - DA401 + DA601"),
            ("___________________________________________________________________", ""),
        ]
        return cumulative_cogformulav3_values
    
    def returnCogformulav4List(self):
        cumulative_cogformulav4_values = [
            ("VALORI CUMULATI DELLA MACCHINA - FORMULA COG | COGES V4", ""),
            ("Venduto", f"{convert_to_decimal(self.VA101 + self.VA301)}€"),
            ("VendutoContante", f"{convert_to_decimal(self.CA201)}€"),
            ("VendutoNoContante", f"{convert_to_decimal(self.VA101 + self.CA201)}€"),
            ("Incassato", f"{convert_to_decimal(self.CA305)}€"),
            ("IncassatoRicarica", f"{convert_to_decimal(self.DA401 - self.DA601)}€"),
            ("IncassatoVendita", f"{convert_to_decimal((self.CA305 - self.DA401) + (self.DA601))}€"),
            ("VALORI CUMULATI DELLA MACCHINA - LEGGENDA COG | COGES V4", ""),
            ("Venduto", "VA101 + VA301"),
            ("VendutoContante", "CA201"),
            ("VendutoNoContante", "VA101 + CA201"),
            ("Incassato", "CA305"),
            ("IncassatoRicarica", "DA401 - DA601"),
            ("IncassatoVendita", "CA305 - DA401 + DA601"),
            ("___________________________________________________________________", ""),
        ]
        return cumulative_cogformulav4_values

    def returnGenericExceptionList(self):
        cumulative_genericException_values = [
            ("VALORI CUMULATI DELLA MACCHINA IDENTICI PER TUTTE LE ECCEZIONI", ""),
            ("TotaleResoTubiResto", f"{convert_to_decimal(self.CA403)}€"),
            ("TotaleCaricatoTubiResto", f"{convert_to_decimal(self.CA307)}€"),
            ("TotaleResoManualeTubiResto", f"{convert_to_decimal(self.CA404)}€"),
            ("TotaleCaricatoManualeTubiResto", f"{convert_to_decimal(self.CA1002)}€"),
            ("LEGGENDA", ""),
            ("TotaleResoTubiResto", "DA503 + DB503"),
            ("TotaleCaricatoTubiResto", "CA702"),
            ("TotaleResoManualeTubiResto", "CA706 + DA507 + DB507"),
            ("TotaleCaricatoManualeTubiResto", "DA301 + DB301"),
        ]
        return cumulative_genericException_values
    

    def RicavaMarcaModelloGettoniera_(self):

        MarcaModello = ""

        # RICAVO MODELLO CPI
        if self.CA102 != "":
            if self.CA102 in ["CF8000EXEC", "CF8000MDB", "CF690", "CF6000EXEC", "EC6000MDB", "CF7900EXEC", "CF7900MDB"]:
                MarcaModello = "MEI|" + self.CA102
        print("NON E' CPI")

        # RICAVO MODELLO COGES
        if MarcaModello == "":
            if self.ID102 != "":
                if self.ID102 in ["93", "97", "77", "64", "76", "38", "30", "AETERNA", "85"]:
                    MarcaModello = "COGES|" + self.ID102
                    return MarcaModello + "|" + self.DXS03
            elif self.CA101.startswith("COG"):
                if self.CA403 == "":
                    MarcaModello = "COGES|IDEA4COL" 
                    return MarcaModello + "|" + self.DXS03
        print("NON E' COGES")

        # RICAVO MODELLO PAYTEC
        if MarcaModello == "":
            if self.ID102 != "":
                if self.ID102.startswith("FAG"):
                    # Controlla l'ultimo carattere di self.MA502
                    if self.MA502[-1] in ["1", "2", "3", "4"]:
                        MarcaModello = f"PAYTEC|PAYTECV{self.MA502[-1]}"
                        return MarcaModello
        print("NON E' PAYTEC")

        # RICAVO MODELLO SUZOHAPP
        if MarcaModello == "":
            if self.CA102 != "":
                if self.CA102.startswith("C2"):
                    MarcaModello = "SUZ0HAPP|CURRENZA"
                    return MarcaModello
        print("NON E' SUZOHAPP|CURRENZA")

        if self.ID102 != "":
            if  self.ID102.startswith("WKL"):
                MarcaModello = "SUZ0HAPP|WORLDKEY"
                return MarcaModello
            elif self.ID102.startswith("EKN"):
                MarcaModello = "SUZ0HAPP|EURO KEY NEXT"
                return MarcaModello
         

        if self.ID705 != "":
            print("SUZ0HAPP|ID705")
            if  self.ID705.startswith("WKL"):
                MarcaModello = "SUZ0HAPP|WORLDKEY"
                return MarcaModello
            elif self.ID705.startswith("EKN"):
                MarcaModello = "SUZ0HAPP|EURO KEY NEXT"
                return MarcaModello
            
        print("NON E' SUZ0HAPP|WORLDKEY O SUZ0HAPP|EURO KEY NEXT")
        
        # RICAVO MODELLO ELKEY
        if MarcaModello == "":
            if self.DA102 != "" and self.DA102.startswith("1"):
                MarcaModello = "ELKEY|BUBBLE"
                return MarcaModello
            if self.DA102 != "" and self.DA102 == "ELK Bubble":
                MarcaModello = "ELKEY|BUBBLE"
                return MarcaModello
        
        print("NON E' ELKEY")

        # RICAVO MODELLO GENERICO
        if isinstance(self.ID101, int):
            self.ID101 = str(self.ID101) 

        if self.ID101 != "" and not self.ID101[0].isdigit():
            first_three_chars = self.ID101[:3]
            MarcaModello = first_three_chars + "|XXX"
        else:
            if self.DXS01 != "":
                first_three_chars = self.DXS01[:3]
                MarcaModello = first_three_chars + "|XXX"
            else:
                MarcaModello = ""
            

        return MarcaModello