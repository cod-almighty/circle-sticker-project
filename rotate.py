from PIL import Image, ImageFont, ImageDraw, ImageTk
import math as m
import tkinter as tk

ppmm = 7620 # pixels per mm (300 dpi * 25.4)

def process_fields():
    text = "cod almighty"#e1.get()
    fntsize = 72#int(e2.get())
    size = 200 #int(e3.get() * ppmm) # get size in mm, convert to pixels, and store as an int.
    draw_text(text, fntsize, size)
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)

def draw_text(text, fntsize, size):
    font = ImageFont.truetype(r'/home/donnie/.fonts/Homework.otf', fntsize)
    diameter = size
    imgsize = (diameter + 25, diameter + 25)
    radius = int((diameter + 25) / 2)
    imgbase = Image.new('RGBA', imgsize, (255,255,255,255)) #create new image
    draw1 = ImageDraw.Draw(imgbase)
    xcenter = int(radius)
    ycenter = int(radius)

    offset = 3.3
    px, py = 10, 10
    k = 0
    chardeg = 90

    for c in text:

        k = k + 1
        # find x, y coords to place character on imgbase
        xpos = int(xcenter + radius * m.cos(-((1*k*m.pi)/len(text)) + offset))
        ypos = int(ycenter - radius * m.sin(-((1*k*m.pi)/len(text)) + offset))

        imgchar = Image.new('RGBA', (font.getsize(c)), (255,255,255,0)) # create temp canvas for character
        d = ImageDraw.Draw(imgchar) # declare d as ImageDraw.Draw(imgchar)
        d.text((0, 0), text=c, font=font, fill=(0,0,0,255)) #Draw character on canvas

        angle = 180/len(text)
        imgchar = imgchar.rotate(chardeg, expand=1)
        chardeg = chardeg - angle

        imgbase.paste(imgchar, (xpos, ypos), imgchar)

        imgbase.save('base.png', 'png', dpi=(300,300))

## Start of GUI
root = tk.Tk()

#canvas = tk.Canvas(root, width = 300, height = 300)
#canvas.pack()

tk.Label(root, text="Top line").grid(row=0)
tk.Label(root, text="Font size").grid(row=1)
tk.Label(root, text="Sticker size").grid(row=2)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
e3.grid(row = 2, column = 1)

tk.Button(root, text="Show", command=process_fields).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(root, text="Quit", command=root.quit).grid(row=4, column=1, sticky=tk.W, pady=4)

#canvas.create_image(20, 20, anchor = NW, image = "imgbase")

root.mainloop()
## END of GUI

#text = input("enter top line: ")
#fntsize = int(input("enter font size: "))

