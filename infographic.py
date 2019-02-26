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

def generate_part(legend_img, rr_img, img_width, img_height, rows, name):
    part_width = img_width * 7
    part_height = rows * img_height + int(3.5 * img_height)
    part_img = Image.new('RGBA', (part_width, part_height), (0,0,0,200))
    part_img.paste(legend_img, (img_width, 2 * img_height), legend_img)
    part_img.paste(rr_img, (img_width ,legend_img.height + 3 * img_height), rr_img)
    return part_img

def generate_all_parts(output_dict):
    parts = len(output_dict)/2
    partlist = []
    i = 0
    while i < parts:
        legendimgname = 'part{}legends.png'.format(i+1)
        rrimgname = 'part{}rr.png'.format(i+1)
        legends = Image.open(os.path.join(OUTPUTS, legendimgname))
        rrs = Image.open(os.path.join(OUTPUTS, rrimgname))
        width = output_dict[legendimgname]['img_width']
        height = output_dict[legendimgname]['img_height']
        rows = output_dict[legendimgname]['rows'] + output_dict[rrimgname]['rows']
        partlist.append(generate_part(legends, rrs, width, height, rows, 'part{}'.format(i+1)))
        i += 1
    return partlist

def layeroncanvas(partlist, canvas, margin):
    for i in range(len(partlist)):
        if i == 0:
            canvas.paste(partlist[i], ((i+1) * margin, margin), partlist[i])
        else:
            canvas.paste(partlist[i], (((i+1) * margin) + (partlist[i-1].width * i), margin), partlist[i])
    return canvas

def create_canvas(partlist, margin):
    # Calculate largest part height
    max_height = 0
    for i in partlist:
        if i.height > max_height:
            max_height = i.height
    height = max_height + 2 * margin
    width = (partlist[0].width * len(partlist)) + (margin * (len(partlist) + 1))
    im = Image.new('RGBA', (width, height), (0,255,255,255))
    return im

