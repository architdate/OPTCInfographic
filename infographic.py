## File that layers the final image
# Notes:
# imgwidth on each side of the clustered units
# 2 img width on top
# 1 img width between legs and rr
# half imgwidth between each part

import PIL, os, glob
from PIL import Image, ImageFont, ImageDraw
from math import ceil, floor
import textwrap

my_path = os.path.abspath(os.path.dirname(__file__))
OUTPUTS = os.path.join(my_path, "images\\outputs")

def generate_part(legend_img, rr_img, img_width, img_height, rows, name, text):
    part_width = img_width * 7
    part_height = rows * img_height + int(3.5 * img_height)
    part_img = Image.new('RGBA', (part_width, part_height), (0,0,0,190))
    part_img.paste(legend_img, (img_width, 2 * img_height), legend_img)
    part_img.paste(rr_img, (img_width ,legend_img.height + 3 * img_height), rr_img)
    draw = ImageDraw.Draw(part_img)
    font = ImageFont.truetype(os.path.join(my_path,"Comic Sans MS.ttf"), 32)
    partfont = ImageFont.truetype(os.path.join(my_path,"Comic Sans MS.ttf"), 40)
    y_text = img_height//4
    draw.text(((part_width-partfont.getsize(name)[0])/2, y_text), name, fill="white", font=partfont)
    for line in text.split('\\n'):
        w, h = font.getsize(line)
        y_text += h
        draw.text(((part_width-w)/2, y_text), line, fill="white", font=font)
    return part_img

def generate_all_parts(output_dict, parttexts):
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
        partlist.append(generate_part(legends, rrs, width, height, rows, 'Part {}'.format(i+1), parttexts[i]))
        i += 1
    return partlist

def layeroncanvas(partlist, banner, canvas, margin):
    canvas.paste(banner, ((canvas.width//2) - (banner.width//2), 0), banner)
    for i in range(len(partlist)):
        if i == 0:
            canvas.paste(partlist[i], ((i+1) * margin, margin + banner.height), partlist[i])
        else:
            canvas.paste(partlist[i], (((i+1) * margin) + (partlist[i-1].width * i), margin + banner.height), partlist[i])
    return canvas

def create_canvas(partlist, margin, banner):
    # Calculate largest part height
    max_height = 0
    for i in partlist:
        if i.height > max_height:
            max_height = i.height
    height = max_height + 2 * margin + banner.height
    width = (partlist[0].width * len(partlist)) + (margin * (len(partlist) + 1))
    if not os.path.exists(os.path.join(my_path, 'images\\background.png')):
        return Image.new('RGBA', (width, height), (0,255,255,255))
    else:
        img = Image.open(os.path.join(my_path, 'images\\background.png'))
        return img.resize((width, height), PIL.Image.ANTIALIAS)