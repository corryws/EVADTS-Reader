# Dizionario per le spiegazioni dei tag
tag_descriptions = {
    'DXS01': 'Communication ID (of sender)',
    'DXS02': 'Functional Identifier',
    'DXS03': 'Version',
    
    'ST01': 'Transaction Set Header',
    'ST01': 'Transaction Set Control Number',
    
    'ID101': 'Machine Serial Number',
    'ID102': 'Machine Model Number',
    'ID103': 'Machine Build Standard',
    'ID104': 'Machine Location',
    'ID105': 'User Defined Data',
    'ID106': 'Machine Asset Number',
    'ID107': 'DTS Level',
    'ID108': 'DTS Revision',
    'ID401': 'Decimal Point Position',
    'ID402': 'Numeric Currency Code',
    'ID403': 'Alphabetic Currency Code',

    'MA501': 'Block Identifier',
    'MA502': 'Specific Configuration Data',
    'MA503': 'Optional Field #2',
    'MA504': 'Optional Field #3',
    'MA505': 'Optional Field #4',
    'MA506': 'Optional Field #5',
    'MA507': 'Optional Field #6',
    'MA508': 'Optional Field #7',
    'MA509': 'Optional Field #8',
    'MA510': 'Optional Field #9',
    'MA511': 'Optional Field #10',
    'MA512': 'Optional Field #11',
    'MA513': 'Optional Field #12',
    'MA514': 'Optional Field #13',
    'MA515': 'Optional Field #14',
    'MA516': 'Optional Field #15',
    'MA517': 'Optional Field #16',
    'MA518': 'Optional Field #17',
    'MA519': 'Optional Field #18',
    'MA520': 'Optional Field #19',
    'MA521': 'Optional Field #20',
    'MA522': 'Optional Field #21',
    'MA522': 'Optional Field #22',

    'CA101': 'Coin Mechanism Serial Number',
    'CA102': 'Coin Mechanism Model Number',
    'CA103': 'Coin Mechanism Software Revision',
    'CA104': 'User Defined Data',
    'CA105': 'Coin Mechanism Asset Number',
    'CA201': 'Value of Cash Sales Since Initialization',
    'CA202': 'Number of Cash Vends Since Initialization',
    'CA203': 'Value of Cash Sales Since Last Reset',
    'CA204': 'Number of Cash Vends Since Last Reset',
    'CA301': 'Value of Cash In Since Last Reset',
    'CA302': 'Value of Cash To Cash Box Since Last Reset',
    'CA303': 'Value of Cash to Tubes Since Last Reset',
    'CA304': 'Value of Bills In Since Last Reset',
    'CA305': 'Value of Cash In Since Initialization',
    'CA306': 'Value of Cash To Cash Box Since Initialization',
    'CA307': 'Value of Cash To Tubes Since Initialization',
    'CA308': 'Value of Bills In Since Initialization',
    'CA309': 'Value of Bills In Since Last Reset',
    'CA310': 'Value of Bills In Since Initialization',
    'CA401': 'Value of Cash Dispensed Since Last Reset',
    'CA402': 'Value of Cash Manually Dispensed Since Last Reset',
    'CA403': 'Value of Cash Dispensed Since Initialization',
    'CA404': 'Value of Cash Manually Dispensed Since Initialization',
    'CA501': 'Number of Power Outages Since Last Reset',
    'CA502': 'Number of Power Outages Since Initialization',
    'CA801': 'Value of Cash Overpay Since Last Reset',
    'CA802': 'Value of Cash Overpay Since Initialization',
    'CA901': 'Value of Pay Vends Exact Change Since Last Reset',
    'CA902': 'Value of Pay Vends Exact Change Since Initialization',
    'CA1001': 'Value of Cash Filled Since Last Reset',
    'CA1002': 'Value of Cash Filled Since Initialization',
    'CA1101': 'Value of Accepted Coin',
    'CA1102': 'Number of Coins In Since Last Reset',
    'CA1103': 'Number of Coins To Cash Box Since Last Reset',
    'CA1104': 'Number of Coins To Tubes Since Last Reset',
    'CA1105': 'Number of Coins In Since Initialization',
    'CA1106': 'Number of Coins To Cash Box Since Initialization',
    'CA1107': 'Number of Coins To Tubes Since Initialization',
    'CA1501': 'Value of Tube Contents',
    'CA1502': 'Block No Tube 1 = Coin Type 0-7, Tube 2 = Coin Type 8-15',
    'CA1503': 'Coin Type 0 or 8 count',
    'CA1504': 'Coin Type 1 or 9 count',
    'CA1505': 'Coin Type 2 or 10 count',
    'CA1506': 'Coin Type 3 or 11 count',
    'CA1507': 'Coin Type 4 or 12 count',
    'CA1508': 'Coin Type 5 or 13 count',
    'CA1701': 'Coin Type Number (per MDB coin tube)',
    'CA1702': 'Value of Coin',
    'CA1703': 'Number of Coins in Tube',

    'VA101': 'Value of All Paid Vends Since Initialization',
    'VA102': 'Number of All Paid Vends Since Initialization',
    'VA103': 'Value of All Paid Sales Since Last Reset',
    'VA104': 'Number of All Paid Vends Since Last Reset',
    'VA105': 'Value of All Discounts Given Since Initialization',
    'VA106': 'Number of All Discounted Paid Vends Since Initialization',
    'VA107': 'Value of All Discounts Given Since Last Reset',
    'VA108': 'Number of All Discounted Paid Vends Since Last Reset',
    'VA301': 'Free Vend Value of Sales Since Initialization',
    'VA302': 'Number of Free Vends Since Initialization',
    'VA303': 'Free Vend Value Of Sales Since Last Reset',
    'VA304': 'Number of Free Vends Since Last Reset',

    'DA101': 'Cashless 1 Serial Number',
    'DA102': 'Cashless 1 Model Number',
    'DA103': 'Cashless 1 Software Revision',
    'DA201': 'Value of Cashless 1 Sales Since Initialization',
    'DA202': 'Number Of Cashless 1 Vends Since Initialization',
    'DA203': 'Value of Cashless 1 Sales Since Last Reset',
    'DA204': 'Number of Cashless 1 Vends Since Last Reset',
    'DA301': 'Value Debited From Cashless 1 Since Initialization',
    'DA302': 'Value Debited From Cashless 1 Since last Reset',
    'DA401': 'Value Credited To Cashless 1 Since Initialization',
    'DA402': 'Value Credited To Cashless 1 Since Last Reset',
    'DA501': 'Value of Cashless 1 Discounts Since Last Reset',
    'DA502': 'Number Of Discount Cashless 1 Vends Since Last Reset',
    'DA503': 'Value Of Cashless 1 Discounts Since Initialization',
    'DA504': 'Number Of Discount Cashless 1 Vends Since Initialization',
    'DA505': 'Value of Cashless 1 Surcharges Since Last Reset',
    'DA506': 'Number of Surcharge Cashless 1 Vends Since Last Reset',
    'DA507': 'Value Of Cashless 1 Surcharges Since Initialization',
    'DA508': 'Number of Surcharge Cashless 1 Vends Since Initialization',
    'DA601': 'Revaluation Incentive on Cashless 1 Since Initialization',
    'DA602': 'Revaluation Incentive on Cashless 1 Since Last Reset',

    'DB201': 'Value of Cashless 2 Sales Since Initialization',
    'DB202': 'Number Of Cashless 2 Vends Since Initialization',
    'DB203': 'Value of Cashless 2 Sales Since Last Reset',
    'DB204': 'Number of Cashless 2 Vends Since Last Reset',
    'DB301': 'Value Debited From Cashless 2 Since Initialization',
    'DB302': 'Value Debited From Cashless 2 Since Last Reset',
    'DB401': 'Value Credited To Cashless 2 Since Initialization',
    'DB402': 'Value Credited To Cashless 2 Since Last Reset',
    'DB501': 'Value of Cashless 2 Discounts Since Last Reset',
    'DB502': 'Number Of Discount Cashless 2 Vends Since Last Reset',
    'DB503': 'Value Of Cashless 2 Discounts Since Initialization',

    'EA101': 'Event Identification',
    'EA102': 'Date of Event Occurrence',
    'EA103': 'Time of Event Occurrence',
    'EA104': 'Event Duration In Minutes',
    'EA105': 'Event Duration In Milliseconds',
    'EA106': 'User Defined Data',
    'EA201': 'Event Identification',
    'EA202': 'Number of Events Since Last Reset',
    'EA203': 'Number of Events Since Initialization',
    'EA204': 'User Defined Data',
    'EA205': 'Event Activity (1 - active, 0 or empty - inactive)',
    'EA301': 'Number Of Reads with RESET Since Initialization',
    'EA302': 'Date Of This Read Out',
    'EA303': 'Time Of This Read Out',
    'EA304': 'This Terminal / interrogator Identification',
    'EA305': 'Date Of Last Read Out',
    'EA306': 'Time Of Last Read Out',
    'EA307': 'Last Terminal / interrogator Identification',
    'EA308': 'User Defined Data',
    'EA309': 'Number of Reads with or without RESET since Initialization',
    'EA310': 'Number of Resets since Initialization',
    'EA701': 'Number of Power Outages Since Last Reset',
    'EA702': 'Number of Power Outages Since Initialization',

    'PA101': 'Product Identifier',
    'PA102': 'Product Price',
    'PA201': 'Number of Paid Products Vended Since Initialization',
    'PA202': 'Value Of Paid Product Sales Since Initialization',
    'PA203': 'Num. Of Paid Products Vended Since Last Reset',
    'PA204': 'Value Of Paid Product Sales Since Last Reset',

    'LA101': 'Pricelist Number',
    'LA102': 'Product Number',
    'LA103': 'Price',
    'LA104': 'Number of Vends Since Last Reset',

    'TA201': 'Value of Vend Token Vends Since Initialization',
    'TA202': 'No. of Vend Token Vends Since Initialization',
    'TA203': 'Value of Vend Token Sales Since Last Reset',
    'TA204': 'No. of Vend Token Sales Since Last Reset',
    'TA205': 'Value of Value Token Since Initialization',
    'TA206': 'No. of Value Token Since Initialization',
    'TA207': 'Value of Value Token Sales Since Last Reset',
    'TA208': 'No. of Value Token Vends Since Last Reset',
    'TA501': 'Value of Token Overpay Since Last Reset',
    'TA502': 'Value of Token Overpay Since Initialization',

    'AM101': 'Audit module',

    'G85': 'Integrity Check',
    'AM1': 'Audit module',
    'SE': 'End of Transmission Set',
    'DXE01': 'End of Transaction',
    'DXE02': 'Number of Included Sets',
    'XX101': 'Other'
}