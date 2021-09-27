from pyzbar import pyzbar
import cv2
import pytesseract
import time



set_language = "POL"

def readBarcode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    barcodes = []
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        barcodes.append(int(obj.data))
    return image, barcodes

def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=2)
    return image

def readFrame(frame):
    readString = pytesseract.image_to_string(frame)
    return readString.splitlines()

def readReceiptLive():
    result = []
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        _, frame = cap.read()
        cv2.imshow("live feed", frame)
        userKey = cv2.waitKey(1)
        if userKey == ord("q"):
            break
        elif userKey == ord(" "):
            result.append(readFrame(frame))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            result.append(readFrame(frame))
            frame = cv2.fastNlMeansDenoising(frame)
            result.append(readFrame(frame))
            frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,2)
            result.append(readFrame(frame))
    cap.release()
    cv2.destroyAllWindows()
    return result

def readBarcodeLive():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        _, frame = cap.read()
        frame, barcode = readBarcode(frame)
        cv2.imshow("live feed", frame)
        cv2.waitKey(1)
        if not( barcode == []):
            break
    cap.release()
    cv2.destroyAllWindows()
    return barcode

if __name__ == "__main__":
    for string in readReceiptLive():
        for line in string:
            print(line)
        print("\n-----------------")
        