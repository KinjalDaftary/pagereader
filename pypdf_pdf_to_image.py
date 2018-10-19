import os
from PIL import Image
import io
from pdf2image import convert_from_path

filename = "California Endowment-990-2013(1).pdf"

# Open PDF Source #
app_path = os.path.dirname(__file__) + "/Documents/990 Forms - Sample/California Endowment"
src_path = os.path.join(app_path, filename)

images = convert_from_path(src_path , output_folder=app_path, first_page=0, last_page=3, fmt="png",thread_count=1)
for image in images:
    print("Image name is:")
    print(image.filename) 
    
