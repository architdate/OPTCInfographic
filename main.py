import userinput
import images
import infographic
import PIL, os, glob
from PIL import Image, ImageFont, ImageDraw
import os

my_path = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(my_path, "images")

if not os.path.exists(PATH):
    os.makedirs(PATH)

output_dict = {}

#parts = userinput.getUserInputs()
parts = 3
i = 0
while i < parts:
    subpathlegends = 'part{}legends'.format(i+1)
    subpathrr = 'part{}rr'.format(i+1)
    dict1 = images.generate_clumped_image(subpathlegends)
    dict2 = images.generate_clumped_image(subpathrr)
    output_dict['part{}legends.png'.format(i+1)] = dict1
    output_dict['part{}rr.png'.format(i+1)] = dict2
    i += 1

os.chdir(PATH)
partlist = infographic.generate_all_parts(output_dict)
canvas = infographic.create_canvas(partlist, 56)
final = infographic.layeroncanvas(partlist, canvas, 56)

final.save('infographic.png')