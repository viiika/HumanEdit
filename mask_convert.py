import os
from PIL import Image
input_folder = "./mask/"
output_folder = "./mask_01/"

for i, filename in enumerate(os.listdir(input_folder)):
    if i % 10 == 0:
        print(i)
    if filename.endswith(".png"):  
        input_path = os.path.join(input_folder, filename)  
        output_path = os.path.join(output_folder, filename) 

        input_img = Image.open(input_path).convert("RGB")
        gray_img = input_img.convert("L")
        binary_img = gray_img.point(lambda x: 255 if x == 0 else 0, '1')
        binary_img.save(output_path)
