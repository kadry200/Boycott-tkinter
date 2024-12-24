from tkinter import *
from PIL import Image, ImageTk

# function to search in a text file
def click1():
 pass
#function to go to next page
def click2():
    pass
#function to destroy the ui
def click3():
    pass

window1=Tk()
window1.geometry("800x600")
window1.title("Boycott")

label1=Label(window1,text="Israeli Product Checker: Verified Boycott List")
label1.place(x=190,y=60)

Entry1=Entry(window1)
Entry1.place(x=20,y=130)

Button1=Button(window1,width=5,command=click1)
Button1.place(x=500,y=130)

label2=Label(window1,text="Add Product To Boycott ")
label2.place(x=0,y=250)

label3=Label(window1,text="Output: ")
label3.place(x=20,y=180)

Button2=Button(window1,text="Press",command=click2)
Button2.place(x=250,y=250)

Button3=Button(window1,text="Exit",command=click3)
Button3.place(x=0,y=350)



window1.mainloop()
