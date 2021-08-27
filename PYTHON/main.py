import pytesseract
import os
from difflib import SequenceMatcher

#TODO make SQL database
Auchan_IDs = ("CYDR.LUBELSKI 1L", "P/Z.KOKARDK 400G L", "ACTI 6X400TR.4X100", "LAY'S-SER-SIEL-CEB", \
    "PRZYSM.CEBUL.DYM.1", "HARIBO.JELL.175G", "X01E.PRZEW", "PITNY JAGODA 330ML")

Kaufland_IDs = ("K.WarzywNaPatAzja750", "Favita16%tl. 270g", "K.Szpinak450g", "Cebula zolta kg")

Carrefour_IDs = ("C_MC SER GOUDA 300", "C_JZN CZOSNEK POLSK", "C_JOGURT NATURALNY", "C_MC MIX SALAT Z SA", \
    "C_WINOGRONO BIALE L", "C_JOG.D/P SKYR 330M", "C_OGOREK KROTKI LUZ", "C_TORTILLA WRAPS 24", \
        "C_FASOLKA CZERW.DAW", "C_MAKARON LUBELLA P", "C_PRZYPRAWA PRYMAT")

Available_shops = ("auchan", "kaufland", "carrefour")

#check how many letters are the same, returns value from 0.00 to 1.00 according to how similar inputs are
def stringSimilarity(ID_0, ID_1):
    return SequenceMatcher(None, ID_0, ID_1).ratio()

def getShopsName(readReceipt):
    readLines = readReceipt.split(' ')
    result_power = 0.0
    result = None
    for line in readLines:
        buffer, buffer_power = matchString(Available_shops, line.lower(), 0.6)
        if buffer_power > result_power:
            result = buffer
            result_power = buffer_power
    return result, result_power

def matchString(database, input, minimal_power = 0.0):
    result_index = 0
    results_power = minimal_power
    for i in range(len(database)):
        buffer = stringSimilarity(input, database[i])
        if buffer > results_power:
            results_power = buffer
            result_index = i
    if results_power == minimal_power:
        return "Not found anything", 0.00
    return database[result_index], results_power

def test(receipt, shops_IDs):
    #print("Starting testing OCR\n---------------")
    readText = pytesseract.image_to_string(receipt)
    #print(readText)
    #print("---------------\nTesting OCR finished")
    for text in readText.split('\n'):
        if text is None:
            continue
        #print(text, "->", matchString(shops_IDs, text, 0.5))
    print(getShopsName(readText))


def main():
    test(r'Tests\Receipts\test000.jpg', Auchan_IDs)
    test(r'Tests\Receipts\test001.jpg', Kaufland_IDs)
    test(r'Tests\Receipts\test002.jpg', Carrefour_IDs)
    test(r'Tests\Receipts\test003.jpg', Auchan_IDs)

    print("Exit succesful")

main()