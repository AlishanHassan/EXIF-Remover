__author__ = "Alishan Hassan"

import sys
from PIL import Image

print("EXIF Info Remover")
file = input('What photo do you want to purge? ')
print('Cleaning ', file, '...')

original_image = Image.open(file)

image_data = list(original_image.getdata()) #doesn't copy EXIF data
cleansed_image = Image.new(original_image.mode, original_image.size)
cleansed_image.putdata(image_data)

cleansed_image.save('cleansed_' + file)
print(file, "purged!")
