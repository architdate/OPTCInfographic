import PIL, os, glob
from PIL import Image
from math import ceil, floor

my_path = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(my_path, "images")

frame_width = 1920 #default
images_per_row = 5
padding = 0

def generate_clumped_image(subpath):
    retdict = {}
    os.chdir(os.path.join(PATH, subpath))

    images = glob.glob("*.png")
    images = images[:30]                #get the first 30 images

    img_width, img_height = Image.open(images[0]).size
    retdict['img_width'] = img_width # 112 for OPTC
    retdict['img_height'] = img_height # 112 for OPTC
    frame_width = img_width * images_per_row
    sf = (frame_width-(images_per_row-1)*padding)/(images_per_row*img_width)       #scaling factor
    scaled_img_width = ceil(img_width*sf)                   #s
    scaled_img_height = ceil(img_height*sf)

    number_of_rows = ceil(len(images)/images_per_row)
    retdict['rows'] = number_of_rows
    frame_height = ceil(sf*img_height*number_of_rows) 

    new_im = Image.new('RGBA', (frame_width, frame_height), (0, 0, 0, 0))

    i,j=0,0
    reset_i = False
    for num, im in enumerate(images):
        if num%images_per_row==0:
            i=0
        im = Image.open(im)
        #Here I resize my opened image, so it is no bigger than 100,100
        im.thumbnail((scaled_img_width,scaled_img_height))
        #Iterate through a 4 by 4 grid with 100 spacing, to place my image
        y_cord = (j//images_per_row)*scaled_img_height
        
        if (j//images_per_row) + 1 == number_of_rows and reset_i == False:
            # Set i to centre the last row
            remaining_images = len(images) - j
            last_row_width = remaining_images * img_width + (padding * (remaining_images - 1))
            i = (frame_width - last_row_width)//2
            reset_i = True
        
        new_im.paste(im, (i,y_cord))
        i=(i+scaled_img_width)+padding
        j+=1

    if not os.path.exists(os.path.join(PATH, 'outputs')):
        os.makedirs(os.path.join(PATH, 'outputs'))
    new_im.save("{}/{}.png".format(os.path.join(PATH, 'outputs'), subpath), "PNG")
    return retdict