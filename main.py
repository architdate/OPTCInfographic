import userinput
import images
import infographic
import PIL, os, glob
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import requests
import shutil
import os

my_path = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(my_path, "images")

if not os.path.exists(PATH):
    os.makedirs(PATH)
else:
    userinput.del_images()

output_dict = {}

banner_url = input("Please input banner image URL (refer: http://news.gb.onepiece-tc.jp/news/html/onepiece-tc-news.html): ")
response = requests.get(banner_url, stream=True, verify=False)
with open(os.path.join(PATH, 'banner.png'), 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response
banner = Image.open(os.path.join(PATH, 'banner.png')).convert('RGBA')

parts = userinput.getUserInputs()

parttexts = []
i = 0
while i < parts:
    parttexts.append(input("Please enter the Text to be displayed for Part {} (date): ".format(i+1)))
    i += 1

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
partlist = infographic.generate_all_parts(output_dict, parttexts)
canvas = infographic.create_canvas(partlist, 56, banner)
final = infographic.layeroncanvas(partlist, banner, canvas, 56)

final.save('infographic.png')