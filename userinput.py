## File to get user input from the user
import os
import requests
import shutil
import json

def del_images():
    my_path = os.path.abspath(os.path.dirname(__file__))
    PATH = os.path.join(my_path, "images")
    a = [x[0] for x in os.walk(PATH)]
    a.pop(0)
    for i in a:
        shutil.rmtree(i)

def createPartDirs(n):
    i = 0
    while i < n:
        legenddir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images/part{}legends'.format(i+1))
        rrdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images/part{}rr'.format(i+1))
        if not os.path.exists(legenddir):
            os.makedirs(legenddir)
        if not os.path.exists(rrdir):
            os.makedirs(rrdir)
        i += 1

def checkJSONvalidity(sugo):
    if 'parts' not in sugo.keys():
        return False
    else:
        if len(sugo.keys()) != (2 * int(sugo['parts']) + 1):
            return False
        i = 0
        while i < int(sugo['parts']):
            if 'part{}legends'.format(i+1) not in sugo.keys():
                return False
            if 'part{}rr'.format(i+1) not in sugo.keys():
                return False
            i += 1
        return True

def getUserInputs():
    if os.path.exists(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sugofest.json')):
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sugofest.json')) as f:
            sugo = json.load(f)
    if checkJSONvalidity(sugo):
        parts = int(sugo['parts'])
        createPartDirs(parts)
        i = 0
        while i < parts:
            legends = sugo['part{}legends'.format(i+1)]
            rrs = sugo['part{}rr'.format(i+1)]
            legendpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images/part{}legends'.format(i+1))
            rrpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images/part{}rr'.format(i+1))
            c = 0
            for x in legends:
                downloadThumbnail(x, legendpath, c + 1)
                c += 1
            c = 0
            for x in rrs:
                downloadThumbnail(x, rrpath, c + 1)
                c += 1
            i += 1
        print("Done Downloading Character Thumbnails")
        return parts

    parts = int(input("How Many parts exist in this sugofest? "))
    createPartDirs(parts)
    i = 0

    while i < parts:
        print("To end inputs for a specific part, type 'end' without quotes")
        charid = input("What is the character id of the boosted legend in Part {}: ".format(i+1))
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images/part{}legends'.format(i+1))
        count = 0
        while charid.lower() != 'end':
            if charid.isdigit():
                downloadThumbnail(charid, path, count + 1)
            else:
                print("Invalid Character ID. Type 'end' to stop adding characters to this category")
            charid = input("What is the character id of the boosted legend in Part {}: ".format(i+1))
            count += 1

        charid = input("What is the character id of the boosted rare recruit in Part {}: ".format(i+1))
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images/part{}rr'.format(i+1))
        count = 0
        while charid.lower() != 'end':
            if charid.isdigit():
                downloadThumbnail(charid, path, count + 1)
            else:
                print("Invalid Character ID. Type 'end' to stop adding characters to this category")
            charid = input("What is the character id of the boosted rare recruit in Part {}: ".format(i+1))
            count +=  1

        i += 1
    print("Done Downloading Character Thumbnails")
    return parts


def downloadThumbnail(charid, path, priority = 0):
    url = getCharUrl(charid)
    response = requests.get(url, stream=True)
    with open(os.path.join(path, '{}_{}.png'.format(str(priority).zfill(2), charid)), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def getCharUrl(charid):
    idstr = str(charid).zfill(4)
    # Account for global exclusives
    if charid == 2502: return 'http://onepiece-treasurecruise.com/en/wp-content/uploads/sites/2/f5013.png'
    elif charid == 2503: return 'http://onepiece-treasurecruise.com/en/wp-content/uploads/sites/2/f5014.png'
    elif charid == 2505: return 'http://onepiece-treasurecruise.com/en/wp-content/uploads/sites/2/f5015.png'
    elif charid == 742: return 'http://onepiece-treasurecruise.com/en/wp-content/uploads/f0742-2.png' # Wanze for some reason lol
    else: return 'https://onepiece-treasurecruise.com/wp-content/uploads/f' + idstr + '.png'