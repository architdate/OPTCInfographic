import userinput
import images
import os

my_path = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(my_path, "images")

if not os.path.exists(PATH):
    os.makedirs(PATH)

parts = userinput.getUserInputs()
i = 0
while i < parts:
    subpathlegends = 'part{}legends'.format(i+1)
    subpathrr = 'part{}rr'.format(i+1)
    images.generate_clumped_image(subpathlegends)
    images.generate_clumped_image(subpathrr)
    i += 1