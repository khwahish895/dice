import tkinter as tk
from cProfile import label

from PIL import Image,ImageTk
import random

window = tk.Tk()
window.geometry("500*360")
window.title("Dice Roll")


dice = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.label(window,image=image1)
label2 = tk.label(window,image=image2)

label1.image = image1
label2.image = image2


label1.place(x = 0, y = 100)
label2.place(x = 300, y = 100)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
     label2.configure(image = image2)
      label2.image = image2

button = tk.Button(window,text="Roll",bg = "green",fg = "white",font= "Times 20 bold",command=dice_roll)
button.place(x = 230, y = 0)
window.mainloop()