from PIL import Image
import random
import os
import sys

L1 = [".", "'", "`", ",", "^", ":", ";", "~", '"']
L2 = ["-", "_", "+", "<", ">", "i", "!", "l", "I", "?"]
L3 = ["/", "|", "(", ")", "1", "{", "}", "[", "]"]
L4 = ["r", "c", "v", "u", "n", "x", "z", "j", "f", "t"]
L5 = ["L", "C", "J", "U", "Y", "X", "Z", "O", "0", "Q"]
L6 = ["o", "a", "h", "k", "b", "d", "p", "q", "w", "m"]
L7 = ["*", "W", "M", "B", "8", "&", "%", "$", "#", "@"]

args = sys.argv
size = 10
run = False
infile = None
outfile = None
for i in range(0, len(args)):
    if args[i].lower() == "-h" or len(args) == 1:
        print("A program to convert images to ASCII art.\n"
              "List of commands:\n"
              "     -h --- Shows this text\n"
              "     -i --- Specifies input file\n"
              "     -o --- Specifies output file\n"
              "     -s --- Value to divide image size by (default 10)\n"
              "Example command: img2ascii.py -i input.jpg -o output.txt -s 200\n"
              "Created by Matthew Vandenbold, matthew.vandenbold@gmail.com")

    if args[i].lower() == "-s":
        try:
            size = int(args[i+1])
        except TypeError:
            print("Invalid size")

    if args[i].lower() == "-i":
        if os.path.isfile(args[i+1]):
            infile = str(args[i+1])
        else:
            print("Invalid input file")

    if args[i].lower() == "-o":
        if not os.path.isfile(args[i + 1]):
            outfile = str(args[i+1])
        else:
            print("Output file already exists")

if infile is not None and outfile is not None:
    print("Size:", size, "   Input:", infile, "   Output:", outfile)
    run = True

if run:
    f = open(outfile, "w+")

    L1 = random.choice(L1)
    L2 = random.choice(L2)
    L3 = random.choice(L3)
    L4 = random.choice(L4)
    L5 = random.choice(L5)
    L6 = random.choice(L6)
    L7 = random.choice(L7)

    im = Image.open(infile).convert('LA')
    w, h = im.size
    im = im.resize((int(w/size), int(h/size)), Image.ANTIALIAS)

    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    for i in pixels:
        f.write("\n")
        for e in i:
            if e[1] == 255:
                if e[0] in range(0, 32):
                    f.write(L7)
                if e[0] in range(32, 64):
                    f.write(L6)
                if e[0] in range(64, 96):
                    f.write(L5)
                if e[0] in range(96, 120):
                    f.write(L4)
                if e[0] in range(120, 160):
                    f.write(L3)
                if e[0] in range(160, 192):
                    f.write(L2)
                if e[0] in range(192, 224):
                    f.write(L1)
                if e[0] in range(224, 255):
                    f.write(" ")
            if e[1] == 0:
                f.write(" ")

    with open(outfile) as filehandle:
        lines = filehandle.readlines()

    with open(outfile, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)
