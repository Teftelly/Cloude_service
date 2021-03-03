from PIL import Image
import pytesseract
import cv2
import os

class Picture_to_text():

    def Get_text_from_picture(self, image):
        #image = 'Capture.JPG'
        image = cv2.imread(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.medianBlur(gray, 3)

        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        custom_config = r'-l rus --psm 6'
        text_from_file = pytesseract.image_to_string(Image.open(filename), config=custom_config)

        text_file_name = "Output.txt"
        text_file = open(text_file_name, "w")
        text_file.write(text_from_file)
        text_file.close()

        return text_file_name
    
        #text = pytesseract.image_to_string(Image.open(filename),config=custom_config)
        #os.remove(filename)
        
        #cv2.imshow("Image", image)
        #cv2.imshow("Output", gray)