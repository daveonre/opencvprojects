# QR Code Scanner

This project is a simple QR Code Scanner using OpenCV and Python. It captures video from the webcam, detects QR codes in the video frames, and opens the URL encoded in the QR code using the default web browser.

## Requirements

- Python 3.x
- OpenCV
- Webbrowser (standard library)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install OpenCV using pip:

    ```sh
    pip install opencv-python
    ```

## Usage

1. Clone the repository or download the `main.py` file.
2. Run the `main.py` script:

    ```sh
    python main.py
    ```

3. The script will open a window displaying the video feed from your webcam.
4. When a QR code is detected, the URL encoded in the QR code will be opened in your default web browser.
5. Press `q` to quit the application.

## Code Explanation

The main functionality is implemented in the `read_and_open_qr_code` function:

```python
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
```

The script captures video frames from the webcam and passes them to this function. If a QR code is detected, the URL is opened in the default web browser.

```python
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
```
