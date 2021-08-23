import pytesseract
from difflib import SequenceMatcher

Auchan_IDs = ("CYDR.LUBELSKI 1L", "P/Z.KOKARDK 400G L", "ACTI 6X400TR.4X100", "LAY'S-SER-SIEL-CEB", \
    "PRZYSM.CEBUL.DYM.1", "HARIBO.JELL.175G", "X01E.PRZEW", "PITNY JAGODA 330ML")

#check how many letters are the same, returns value from 0.00 to 1.00 according to how similar inputs are
def compareIDs(ID_0, ID_1):
    return SequenceMatcher(None, ID_0, ID_1).ratio()


def matchIDs(IDs_database, input):
    result_index = 0
    results_power = 0.00
    for i in range(len(IDs_database)):
        buffer = compareIDs(input, IDs_database[i])
        if buffer > results_power:
            results_power = buffer
            result_index = i
    if results_power == 0.00:
        return "Not found anything"
    return IDs_database[result_index]



def main():
    print("Starting testing OCR\n---------------")
    readText = pytesseract.image_to_string(r'Tests\Receipts\test000.jpg')
    print(readText)
    print("---------------\nTesting OCR finished")

    for text in readText.split('\n'):
        if text is None:
            continue
        print(text, "->", matchIDs(Auchan_IDs, text))
    print("Exit succesful")

main()