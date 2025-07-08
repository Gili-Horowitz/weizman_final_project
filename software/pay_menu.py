from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import sum_photo####
import remain_money##
import tkinter as tk
import menu####
from cart import cart_ideams##
import pay_with_card##


def page2(r):
    r.destroy()
    sum = 0.0



    ##def open_cart():
        #new_window = tk.Toplevel(root)
        #new_window.title("cart")
        #new_window.geometry("300x200")

        ##label = tk.Label(new_window, text="This is a new window!")
       ## label.pack(pady=20)

    def select_photo():

        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file_path:
            load_image(file_path)
        sum = sum_photo.calculate_sum(file_path)
        price_lable = tk.Label(root,text="                                ", font=("Arial", 40, "bold")).place(x=390, y=510)
        money_lable = tk.Label(root, text="                       ",font=("Arial", 40, "bold")).place(x=345, y=510)
        lable= tk.Label(root,text="                            ",font=("Arial", 40, "bold")).place(x=300, y=510)
        remain = tk.Label(root,text="                     ",font=("Arial", 40, "bold")).place(x=358, y=540)
        price_lable = tk.Label(root, text=":סכום בתמונה", font=("Arial", 15, "bold"), fg="purple").place(x=390, y=510)

        money_lable = tk.Label(root, text=sum, font=("Arial", 15, "bold")).place(x=345, y=510)
        lable = tk.Label(root, text='ש"ח ', font=("Arial", 15, "bold")).place(x=300, y=510)
        remain = tk.Label(root, text=remain_money.remain_cart(sum, cart_sum), font=("Arial", 15, "bold")).place(x=358, y=540)




        print(sum)


    def load_image(file_path):
        img = Image.open(file_path)
        img = img.resize((250, 300))
        img = ImageTk.PhotoImage(img)

        img_label.config(image=img)
        img_label.image = img
        img_label.place(x=255,y=200)


    ###############################
    root = Tk()
    root.title('Pay Menu')
    root.geometry("900x600")
    root.state('zoomed')




    cart_sum = 0
    sum_in_photo = 0.00
    p = 140 ## place of the ideams in the cart
    print("in pay menu ")
    print(cart_ideams)
    for ideam in cart_ideams:
        l = Label(root, text=ideam,fg="purple",font=("Arial", 18, "bold")).place(x=1030,y=p)
        p = p +30
        cart_sum = cart_sum + cart_ideams.get(ideam)

    #print(cart_sum)


    # Variable to track if labels are shown



    img_label = tk.Label(root)
    img_label.place(x=250, y=150)

    cartL = Label(root,text=": עגלה ", font=("Arial", 20,"bold")).place(x=1030,y=100)
    money = Label(root, text="סכום בעגלה %d "%cart_sum,  font=("Arial", 18, "bold"))
    money.place(x=1030, y=p+ 10)

    label1 = Label(root, text="- תשלום -", fg="purple", font=("Arial", 45, "bold"))
    label1.place(x=650, y=40, anchor=CENTER)
    l = Label(root, text="~ סריקת מטבעות ~ " , fg="purple", font=("Arial", 20, "bold")).place(x=270,y=100)
    la = Label(root, text="- שימו לב שהתמונה ברורה -", fg="purple", font=("Arial", 13)).place(x=290, y=135)

    btn = tk.Button(root, text="העלאת תמונה", command=lambda :select_photo())
    btn.place(x=330, y=160)
    labels_shown = False
    Bcard= Button(root, text=" תשלום באשראי ", bg="blue", fg="white", font=("Arial", 13, "bold"), command=lambda: pay_with_card.pay_card(root)).place(x=1030,y=p+70)



    b2= Button(root,text="- תפריט הצעצועים -" ,fg="purple",command=lambda:menu.page1(root), font=("Courier New", 13,"bold"), background="light pink").place(x=1050, y=20)


    root.mainloop()



if  __name__ == '__main__':

   page2(Tk())