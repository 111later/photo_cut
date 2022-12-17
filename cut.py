from operator import index
from rembg import remove
from PIL import Image
from pathlib import Path
import os

def remove_bg():
    list_of_extensions = ["*.png", "*.jpg", "*.jpeg"]
    all_files = []

    for ext in list_of_extensions:
        all_files.extend(Path("/home/ibragim/photo_cut/1_REMOVE_BACKGROUND/input_imgs/photos").glob(ext))


    for item in all_files:
        input_path = Path(item)
        file_name = input_path.stem
        output_path = f"/home/ibragim/photo_cut/1_REMOVE_BACKGROUND/output_imgs/photos/{file_name}_output.png"
        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)
        print(f"Complete:{index(+1)} / {len(all_files)}")

#  проверка на чтение готового пути и фотки
def send_photo():
    # get the path/directory
    folder_dir = "/home/ibragim/photo_cut/1_REMOVE_BACKGROUND/output_imgs/photos"
    for images in os.listdir(folder_dir):

        # check if the image ends with png
        if (images.endswith(".png")):
            print(images)


def main():
    remove_bg()

if __name__ == "__main__":
    main()


