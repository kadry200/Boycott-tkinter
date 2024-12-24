from tkinter import *
from PIL import Image, ImageTk

# function to search in a text file
def click1():
    Name=Entry1.get().capitalize()
    try:
      int(Name)  
      label3["text"]="Output: this is a wrong please enter a string"
    except ValueError:
    
     with open (r"C:\Users\Kadry\Downloads\Boycott Brands.txt","r") as file:
         boycott=file.read()
              
    if Name in boycott :
               
           label3["text"]="Output: This is a Boycott"
    else:
           label3["text"]="Output: This isn't a Boycott"   
#function to go to next page
def click2():
    window1.destroy()
    import win2
    
#function to destroy the ui
def click3():
    window1.destroy()
#window
window1=Tk()
window1.geometry("800x600")
window1.title("Boycott")


# Create a Canvas widget
canvas = Canvas(window1,width=3000,height=3000,bg="light yellow")
canvas.pack()

# Draw shapes
canvas.create_rectangle(3000,0,0,110,fill="gold",outline="black")


#first image of esrael boycott
image1 = Image.open(r"C:\Users\Kadry\Desktop\boycott-israel-israeli-all-products-600nw-2386842211.webp")  # Replace with the path to your image
photo1 = ImageTk.PhotoImage(image1)
label1 = Label(window1, image=photo1)
resized_image1 = image1.resize((50, 50)) 
photo1 = ImageTk.PhotoImage(resized_image1)
label_image1 = Label(window1, image=photo1)
label_image1.place(x=0,y=0)

image2 = Image.open(r"C:\Users\Kadry\Desktop\flat,750x,075,f-pad,750x1000,f8f8f8.jpg")  # Replace with the path to your image
photo2 = ImageTk.PhotoImage(image2)
label2 = Label(window1, image=photo2)
resized_image2 = image2.resize((50, 50)) 
photo2 = ImageTk.PhotoImage(resized_image2)
label_image2 = Label(window1, image=photo2)
label_image2.place(x=150,y=0)

image3 = Image.open(r"C:\Users\Kadry\Desktop\11.jpg")  # Replace with the path to your image
photo3 = ImageTk.PhotoImage(image3)
label3 = Label(window1, image=photo3)
resized_image3 = image3.resize((50, 50)) 
photo3 = ImageTk.PhotoImage(resized_image3)
label_image3 = Label(window1, image=photo3)
label_image3.place(x=300,y=0)


image4 = Image.open(r"C:\Users\Kadry\Desktop\images.jpg")  # Replace with the path to your image
photo4 = ImageTk.PhotoImage(image4)
label4 = Label(window1, image=photo4)
resized_image4 = image4.resize((50, 50)) 
photo4 = ImageTk.PhotoImage(resized_image4)
label_image4 = Label(window1, image=photo4)
label_image4.place(x=450,y=0)

image5 = Image.open(r"C:\Users\Kadry\Desktop\n00300030-b.jpg")  # Replace with the path to your image
photo5 = ImageTk.PhotoImage(image5)
label5 = Label(window1, image=photo5)
resized_image5 = image5.resize((50, 50)) 
photo5 = ImageTk.PhotoImage(resized_image5)
label_image5 = Label(window1, image=photo5)
label_image5.place(x=600,y=0)

image6 = Image.open(r"C:\Users\Kadry\Desktop\22.jpg")  # Replace with the path to your image
photo6 = ImageTk.PhotoImage(image6)
label6 = Label(window1, image=photo6)
resized_image6 = image6.resize((50, 50)) 
photo6 = ImageTk.PhotoImage(resized_image6)
label_image6 = Label(window1, image=photo6)
label_image6.place(x=750,y=0)


label1=Label(window1,text="Israeli Product Checker: Verified Boycott List",font=("aria",18),bg="gold",fg="black")
label1.place(x=190,y=60)

Entry1=Entry(window1,font=("aria",16),bg="old lace",width=40)
Entry1.place(x=20,y=130,height=40)

Button1=Button(window1,width=5,text="Search",bg="gold",command=click1)
Button1.place(x=500,y=130,height=41)

label2=Label(window1,text="Add Product To Boycott ",font=("aria",16),bg="light yellow",fg="dark slate gray")
label2.place(x=0,y=250)

label3=Label(window1,text="Output: ",font=("aria",14),bg="light yellow",fg="black")
label3.place(x=20,y=180)

Button2=Button(window1,text="Press",command=click2,width=20,bg="gold",font="aria")
Button2.place(x=250,y=250,height=30)

Button3=Button(window1,text="Exit",bg="gold",font="aria",width=10,command=click3)
Button3.place(x=0,y=350)



window1.mainloop()