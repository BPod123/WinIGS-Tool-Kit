import cv2
import pytesseract

img = cv2.imread('winigs.png')

text = pytesseract.image_to_string(img)
print(text)