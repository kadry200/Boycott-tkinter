from tkinter import *

# function to search in a text file
def click1():
    name=Entry1.get().capitalize()
    with open (r"C:\Users\Kadry\Downloads\Boycott Brands.txt",'r+') as file :
        boycott=file.read()
        try:
            int(name)  
            label3["text"]="Output: this is a wrong please enter a string"
        except ValueError:

         if name in boycott :
              label3["text"]="Output: thank you for using the application"
         else:
               label3["text"]="Output: thank you for using the application"
               file.write(name)
        

def click3():
     window1.destroy()

window1=Tk()
window1.geometry("800x600")
window1.title("Add Boycott")
window1.config(bg="light yellow")

label1=Label(window1,text="Add company here ",font=("aria",18),bg="light yellow",fg="black")
label1.place(x=250,y=60)


Entry1=Entry(window1,font=("aria",16),bg="old lace",width=40)
Entry1.place(x=125,y=130,height=40)

Button1=Button(window1,width=50,text="Search",bg="gold",command=click1)
Button1.place(x=170,y=180,height=30)


label3=Label(window1,text="Output: ",font=("aria",14),bg="light yellow",fg="black")
label3.place(x=20,y=250)

Button2=Button(window1,text="pervious page",bg="gold",font="aria",width=15,command=click3)
Button2.place(x=0,y=320)


Button3=Button(window1,text="Exit",bg="gold",font="aria",width=8,command=click3)
Button3.place(x=0,y=400)



window1.mainloop()
