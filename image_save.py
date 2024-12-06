from datasets import load_dataset
from PIL import Image

# Load the dataset
ds = load_dataset("BryanW/HumanEdit")

# Print the total number of samples and show the first sample
print(f"Total number of samples: {len(ds['train'])}")
print("First sample in the dataset:", ds['train'][0])

# Retrieve the first sample's data
data_dict = ds['train'][0]

# Save the input image (INPUT_IMG)
input_img = data_dict['INPUT_IMG']
input_img.save('input_image.jpg')
print("Saved input image as 'input_image.jpg'.")

# Save the mask image (MASK_IMG)
mask_img = data_dict['MASK_IMG']
mask_img.save('mask_image.png') # Note that the format of the mask image may need to be adjusted. Refer to https://github.com/viiika/HumanEdit/mask_convert.py for more details.
print("Saved mask image as 'mask_image.png'.")

# Save the output image (OUTPUT_IMG)
output_img = data_dict['OUTPUT_IMG']
output_img.save('output_image.jpg')
print("Saved output image as 'output_image.png'.")
