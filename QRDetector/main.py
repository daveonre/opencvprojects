import cv2
import webbrowser

def read_and_open_qr_code(img):
    # initialize the cv2 QRCode detector
    QRdetector = cv2.QRCodeDetector()
    
    # detect and decode
    data, bbox, _ = QRdetector.detectAndDecode(img)
    
    # check if there is a QRCode in the image
    if data:
        webbrowser.open(str(data))
        return True
    return False

# Example usage
Vid = cv2.VideoCapture(0)

while True:
    _, img = Vid.read()
    if read_and_open_qr_code(img):
        break
    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        break

Vid.release()
cv2.destroyAllWindows()
