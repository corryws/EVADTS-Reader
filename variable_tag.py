from function import convert_to_decimal, valida_scelta_campo


class GlobalState:
    def __init__(self):
        self.ID101 = self.CA101 = self.EA302 = self.EA303 = self.EA305 = self.EA306 = self.EA301 = self.ID102 = self.ID705 = self.DA102 = self.MA502 = self.DXS03 = ""
        self.VA101 = self.VA301 = self.CA201 = self.DA201 = self.DA601 = self.DB601 = self.CA305 = self.DA401 = self.DB401 = self.CA1002 = self.CA307 = self.CA403 = self.CA404 = self.CA102 = self.CA802 = 0
        self.DA503 = self.DB503 = self.CA702 = self.CA706 = self.DA507 = self.DB507 = self.DB201 = self.TA201 = self.TA205 = self.DA301 = self.DB301 = self.DB505 = self.DA505 = 0

    def azzera(self):
        self.ID101 = self.CA101 = self.EA302 = self.EA303 = self.EA305 = self.EA306 = self.EA301 = self.ID102 = self.ID705 = self.DA102 = self.MA502 = self.DXS03 = ""
        self.VA101 = self.VA301 = self.CA201 = self.DA201 = self.DA601 = self.DB601 = self.CA305 = self.DA401 = self.DB401 = self.CA1002 = self.CA307 = self.CA403 = self.CA404 = self.CA802 = 0
        self.DA503 = self.DB503 = self.CA702 = self.CA706 = self.DA507 = self.DB507 = self.DB201 = self.TA201 = self.TA205 = self.DA301 = self.DB301 = self.DB505 = self.DA505 = 0

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
            ("IncassatoVendita", "CA305 - CA1002 - DA401 + DB401"),
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
            ("TotaleResoTubiResto", f"{convert_to_decimal(self.DA503 + self.DB503)}€"),
            ("TotalePrelevatoTubiResto", f"{convert_to_decimal(self.CA702)}€"),
            ("TotaleCaricatoTubiResto", f"{convert_to_decimal(self.CA706 + self.DA507 + self.DB507)}€"),
            ("TotaleIncassatoMeccanico", f"{convert_to_decimal(self.DA301 + self.DB301)}€"),
            ("TotaleIncassatoBillValidator", f"{convert_to_decimal(self.DA505 + self.DB505)}€"),
            ("LEGGENDA", ""),
            ("TotaleResoTubiResto", "DA503 + DB503"),
            ("TotalePrelevatoTubiResto", "CA702"),
            ("TotaleCaricatoTubiResto", "CA706 + DA507 + DB507"),
            ("TotaleIncassatoMeccanico", "DA301 + DB301"),
            ("TotaleIncassatoBillValidator", "DA505 + DB505"),
        ]
        return cumulative_genericException_values