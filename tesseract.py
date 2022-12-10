from pyAutoSS import screenshot
from pyAutoSS import writeTextToBox
import cv2
import pytesseract
import time

def takeScreenshot():
    screenshot()
    
def readImageToText(image):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\kenley\AppData\Local\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(image)
    return text

#get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#removes noise
def remove_noise(image):
    return cv2.medianBlur(image,5)

def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    
def main():
    while True:    
        takeScreenshot()
        image = cv2.imread('10Fast.png')
        # image = get_grayscale(image)
        # image = remove_noise(image)
        # image = thresholding(image)
        text = readImageToText(image)
        print(text)
        writeTextToBox(text)
        time.sleep(.1)
main()
    
