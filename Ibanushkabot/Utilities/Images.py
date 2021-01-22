import cv2
import pytesseract

class ImageService():

    def read_image(self,path):
        #The next line is only for Windows machine, it's necessary to get the program installed in the next path
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        img=cv2.imread(path)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        text=pytesseract.image_to_string(img)
        if text.split() !=[]:
            return text
        else:
            return None