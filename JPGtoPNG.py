import sys
import os
from PIL import Image
#grab first and second argumnet
image_folder=sys.argv[1]
output_folder=sys.argv[2]

print(image_folder,output_folder)
#check if new/ exists if not create new
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

#loop entire public folder
for filename in os.listdir(image_folder):
	img=Image.open(f'{image_folder}{filename}')
	clean_name=os.path.splitext(filename)[0]
	img.save(f'{output_folder}{clean_name}.png','png')
	print("done")

#convert mages to png

#save to the new folder