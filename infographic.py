## File that layers the final image
# Notes:
# imgwidth on each side of the clustered units
# 2 img width on top
# 1 img width between legs and rr
# half imgwidth between each part

import PIL, os, glob
from PIL import Image, ImageFont, ImageDraw
from math import ceil, floor

my_path = os.path.abspath(os.path.dirname(__file__))
OUTPUTS = os.path.join(my_path, "images\\outputs")

def calculate_width(parts, img_width):
    part_width = img_width * 7
    width = (part_width * parts) + ((img_width * (parts + 1))//2)
    return width

def calculate_height(rows, img_height):
    part_height = rows * img_height + int(3.5 * img_height)
    height = part_height + img_height
    return height

def generate_part(legend_img, rr_img, img_width, img_height, rows, name):
    part_width = img_width * 7
    part_height = rows * img_height + int(3.5 * img_height)
    part_img = Image.new('RGBA', (part_width, part_height), (0,0,0,200))
    part_img.paste(legend_img, (img_width, 2 * img_height), legend_img)
    part_img.paste(rr_img, (img_width ,legend_img.height + 3 * img_height), rr_img)
    part_img.save('{}.png'.format(name))

def generate_all_parts(output_dict):
    parts = len(output_dict)/2
    i = 0
    while i < parts:
        legendimgname = 'part{}legends.png'.format(i+1)
        rrimgname = 'part{}rr.png'.format(i+1)
        legends = Image.open(os.path.join(OUTPUTS, legendimgname))
        rrs = Image.open(os.path.join(OUTPUTS, rrimgname))
        width = output_dict[legendimgname]['img_width']
        height = output_dict[legendimgname]['img_height']
        rows = output_dict[legendimgname]['rows'] + output_dict[rrimgname]['rows']
        generate_part(legends, rrs, width, height, rows, 'part{}'.format(i+1))
        i += 1

im = Image.new('RGBA', (calculate_width(3, 112), calculate_height(6, 112)), (0,255,255,255))
im.save('canvas.png')

