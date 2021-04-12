from PIL import Image
import pytesseract
import logging
import cv2
import os

class Picture_to_text():

    def Get_text_from_picture(self, image):
        logging.basicConfig(filename="Text_Graber.log", level=logging.INFO)
        logging.debug("initializing...")

        try:
            logging.info("Opening image: {}".format(image))
            image = cv2.imread(image)

            logging.info("Cleare image from junk")
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 3)

            #filename = "{}.png".format(os.getpid())
            #cv2.imwrite(filename, gray)
            
            custom_config = r'-l rus --psm 6'
            logging.info("Try to read russian text from picture")
            text_from_file = pytesseract.image_to_string(Image.open(image), config=custom_config)

        except:
            logging.info("Error! Check input file, it should be here: {}".format(image))
            text_from_file = "Кажеться ты обосрался"

        text_file_name = "Output.txt"
        logging.info("Create output file with text")
        text_file = open(text_file_name, "w")
        text_file.write(text_from_file)
        text_file.close()

        return text_file_name