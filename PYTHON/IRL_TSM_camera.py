from pyzbar import pyzbar
import cv2
import pytesseract
import time

set_language = "POL"

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    result = []
    for obj in decoded_objects:
        # draw the barcode
        # print barcode type & data
        result.append(int(obj.data))
    return result




# if __name__ == "__main__":
#     cap = cv2.VideoCapture(0)
#     for i in range(100):
#         # read the frame from the camera
#         _, frame = cap.read()
#         # decode detected barcodes & get the image
#         # that is drawn
#         decode(frame)
#         cv2.imshow("img", frame)
#         if cv2.waitKey(1) == ord("q"):
#             break

def readFrame(frame):
    readString = pytesseract.image_to_string(frame)
    return readString.splitlines()

def readReceiptLiveFromCamera():
    result = []
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    i = 0
    while True:
        _, frame = cap.read()
        cv2.imshow("live feed", frame)
        cv2.waitKey(1)
        buffer = readFrame(frame)
        print(buffer, len(buffer))
        if len(buffer) < 4:
            i += 1
        else:
            i = 0
            result.append(buffer)
        if i == 5:
            break
        print(i)
    cap.release()
    cv2.destroyAllWindows()
    return result

if __name__ == "__main__":
    for string in readReceiptLiveFromCamera():
        for line in string:
            print(line)
        print("\n\n----------------------------\n")