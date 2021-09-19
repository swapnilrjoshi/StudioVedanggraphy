import os
from pathlib import Path
from PIL import Image
from config import *
from tqdm import tqdm

input_folder = os.path.join(os.getcwd(),INPUT_FOLDER_PATH)
output_folder = os.path.join(os.getcwd(),OUTPUT_FOLDER_PATH)


for folder in tqdm(os.listdir(input_folder)):
    current_folder_path = os.path.join(input_folder, folder)
    if os.path.isdir(current_folder_path):
        for image in tqdm(os.listdir(current_folder_path), leave=False):
            if image.endswith(FILE_EXTENSION):
                img_path = os.path.join(current_folder_path, image)
                img = Image.open(img_path)
                for size in RESIZE_LIST:
                    resize_folder = os.path.join(output_folder, folder, 
                                                 'resize_'+str(size[0])\
                                                 +'x'+str(size[1]))
                    resize_img_path = os.path.join(resize_folder, image)
                    Path(resize_folder).mkdir(parents=True, exist_ok=True)
                    new_image = img.resize(size)
                    dpi = img.info['dpi']
                    new_image.save(resize_img_path, dpi=dpi, quality=100)