from tkinter import Tk, StringVar, ttk
from tkinter import *
from PIL import ImageTk, Image

def imaj():
 #add an image to the form and resize the image 
 p="C:\\Users\\Ozgur\\Desktop\\htm\\img.jpg"
 p2="C:\\Users\\Ozgur\\Desktop\\htm\\img2.jpg"
 size=150,200
 image = Image.open(p)
 image.thumbnail(size, Image.ANTIALIAS)
 image.save("C:\\Users\\Ozgur\\Desktop\\htm\\img2.jpg", "JPEG")
 
 image = ImageTk.PhotoImage(Image.open(p2))
 
 
 label = Label(root,image=image)
 label.image=image
 label.grid(column=0, row=1)
 


def boxy2():
 l2=['B','G','D']
 value = StringVar()
 box2 = ttk.Combobox(root, textvariable=value, state='readonly')
 box2['values'] =l2
 box2.current(0)
 box2.grid(column=0, row=3)



def boxy():
 l=['A','Z','C']
 l2=['B','G','D']
 value = StringVar()
 box = ttk.Combobox(root, textvariable=value, state='readonly')
 box['values'] =l
 box.current(0)
 box.grid(column=0, row=1) #function ends here
 dugme2=Button(root,text="Combobox2",command=boxy2)
 dugme2.grid(column=0,row=2)
 


root = Tk()
root.title("Pencere")
root.geometry("300x300")

dugme=Button(root,text="Combobox",command=imaj)
dugme.grid(column=0,row=0)

root.mainloop()

