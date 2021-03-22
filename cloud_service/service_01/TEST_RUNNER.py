from .Picture.OCR import Picture_to_text as PTT
from .Sound.Pooper import Sound_builder as SB
import pathlib

class Main():

    def I_Do_Somthing(self, Picture_file_name = 'Capture.JPG'):
        # Initialize working directory
        Working_directory = str(pathlib.Path(__file__).parent.absolute())

        # Get path to picture loaded by user
        Path_to_picture =  Working_directory +'\\'+ Picture_file_name
        
        # Get text from the picture and write it to the file.
        # Return filename where text from the picture.
        Text_file_name = PTT().Get_text_from_picture(Path_to_picture)
        
        # Get the path to file where text from picture
        Path_to_text_file = Working_directory +'\\'+ Text_file_name
        
        # Start building PooP
        # As output: a path to sound file with generated PooP
        Sound_file_name = SB().Build_Output_Sound(Working_directory, Path_to_text_file)
        
        # Get the path to file where sound from picture
        Path_to_text_file = Working_directory +'\\'+ Sound_file_name

        return 'I did it!'

print(Main().I_Do_Somthing())
