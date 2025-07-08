
import pay_menu###
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import cart###
import sum_photo###
import remain_money ####

def page1(r):
    r.destroy()

    root = Tk()
    root.title('Toys Menu')
    root.geometry("900x600")
    root.state('zoomed')
    label1 = Label(root, text="- תפריט צעצועים -", fg="blue", font=("Arial", 25, "bold")).place(x=100, y=100)

    def show(name):
        messagebox.showinfo("Added to Cart", " !המוצר נוסף לעגלה")
        cart.add_to_cart(name)


    # Create A Main Frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    my_label = Label(second_frame, text="  ").grid(padx=1300, pady=1000)
    label1 = Label(second_frame, text="- תפריט צעצועים -", fg="blue", font=("Arial", 25, "bold"))

    label1.place(x=650, y=40, anchor=CENTER)

    toy1 = Image.open("barbie.png")
    toy1 = toy1.resize((200, 250))
    toy1 = ImageTk.PhotoImage(toy1)
    barbie = Label(second_frame, image=toy1)
    barbie.place(x=70, y=100)

    Lbarbie = Label(second_frame, text=" ~ ברבי ~ ", fg="blue", font=("Arial", 15, "bold"))

    Lbarbie.place(x=120, y=355)

    Pbarbie = Label(second_frame, text='מחיר: 55 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Pbarbie.place(x=120, y=390)

    Bbarbie = Button(second_frame, text=" + ", fg="blue", command=lambda: show("ברבי"),
                     font=("Courier New", 13, "bold"), background="light blue")
    Bbarbie.place(x=150, y=430)

    toy2 = Image.open("bear.png")
    toy2 = toy2.resize((200, 250))
    toy2 = ImageTk.PhotoImage(toy2)
    bear = Label(second_frame, image=toy2)
    bear.place(x=370, y=100)

    Lbear = Label(second_frame, text="~ בובת דובי ~", fg="blue", font=("Arial", 15, "bold"))
    Lbear.place(x=410, y=355)

    Pbear = Label(second_frame, text='מחיר: 35 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Pbear.place(x=430, y=390)

    Bbear = Button(second_frame, text=" + ", fg="blue", command=lambda: show("בובת דובי"), font=("Courier New", 13, "bold"),
                   background="light blue")
    Bbear.place(x=450, y=430)

    toy3 = Image.open("car.png")
    toy3 = toy3.resize((200, 250))
    toy3 = ImageTk.PhotoImage(toy3)
    car = Label(second_frame, image=toy3)
    car.place(x=670, y=100)

    Lcar = Label(second_frame, text="~ מכונית ~", fg="blue", font=("Arial", 15, "bold"))
    Lcar.place(x=730, y=355)

    Pcar = Label(second_frame, text='מחיר: 20 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Pcar.place(x=720, y=390)

    Bcar = Button(second_frame, text=" + ", fg="blue", command=lambda: show("מכונית"), font=("Courier New", 13, "bold"),
                  background="light blue")
    Bcar.place(x=750, y=430)

    toy4 = Image.open("lego.png")
    toy4 = toy4.resize((200, 250))
    toy4 = ImageTk.PhotoImage(toy4)
    lego = Label(second_frame, image=toy4)
    lego.place(x=970, y=100)

    Llego = Label(second_frame, text="~ לגו ~", fg="blue", font=("Arial", 15, "bold"))
    Llego.place(x=1050, y=355)

    Plego = Label(second_frame, text='מחיר: 60 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Plego.place(x=1020, y=390)

    Blego = Button(second_frame, text=" + ", fg="blue", command=lambda: show("לגו"), font=("Courier New", 13, "bold"),
                   background="light blue")
    Blego.place(x=1050, y=430)

    toy5 = Image.open("ball.png")
    toy5 = toy5.resize((200, 250))
    toy5 = ImageTk.PhotoImage(toy5)
    ball = Label(second_frame, image=toy5)
    ball.place(x=70, y=510)

    Lball = Label(second_frame, text=" ~ כדור ~ ", fg="blue", font=("Arial", 15, "bold"))

    Lball.place(x=120, y=770)

    Pball = Label(second_frame, text='מחיר: 15 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Pball.place(x=120, y=810)

    Bball = Button(second_frame, text=" + ", fg="blue", command=lambda: show("כדור"), font=("Courier New", 13, "bold"),
                   background="light blue")
    Bball.place(x=150, y=855)

    toy6 = Image.open("taki.png")
    toy6 = toy6.resize((200, 250))
    toy6 = ImageTk.PhotoImage(toy6)
    taki = Label(second_frame, image=toy6)
    taki.place(x=370, y=510)

    Ltaki = Label(second_frame, text=" ~ טאקי ~ ", fg="blue", font=("Arial", 15, "bold"))
    Ltaki.place(x=410, y=770)

    Ptaki = Label(second_frame, text='מחיר: 40 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Ptaki.place(x=420, y=810)

    Btaki = Button(second_frame, text=" + ", fg="blue", command=lambda: show("טאקי"), font=("Courier New", 13, "bold"),
                   background="light blue")
    Btaki.place(x=450, y=855)

    toy7 = Image.open("playmobil.png")
    toy7 = toy7.resize((200, 250))
    toy7 = ImageTk.PhotoImage(toy7)
    playmobil = Label(second_frame, image=toy7)
    playmobil.place(x=670, y=510)

    Lplaymobil = Label(second_frame, text=" ~ פליימוביל ~ ", fg="blue", font=("Arial", 15, "bold"))
    Lplaymobil.place(x=710, y=770)

    Pplaymobil = Label(second_frame, text='מחיר: 75 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Pplaymobil.place(x=720, y=810)

    Bplaymobil = Button(second_frame, text=" + ", fg="blue", command=lambda: show("פליימוביל"),
                        font=("Courier New", 13, "bold"), background="light blue")
    Bplaymobil.place(x=750, y=855)

    toy8 = Image.open("coloringBook.png")
    toy8 = toy8.resize((200, 250))
    toy8 = ImageTk.PhotoImage(toy8)
    coloringBook = Label(second_frame, image=toy8)
    coloringBook.place(x=970, y=510)

    LcoloringBook = Label(second_frame, text=" ~ חוברת צביעה ~ ", fg="blue", font=("Arial", 15, "bold"))
    LcoloringBook.place(x=1000, y=770)

    PcoloringBook = Label(second_frame, text='מחיר: 15 ש"ח', fg="blue",
                          font=("Courier New", 13, "bold"))
    PcoloringBook.place(x=1020, y=810)

    BcoloringBook = Button(second_frame, text=" + ", fg="blue", command=lambda: show("חוברת צביעה"),
                           font=("Courier New", 13, "bold"), background="light blue")
    BcoloringBook.place(x=1050, y=855)

    toy9 = Image.open("light.png")
    toy9 = toy9.resize((200, 250))
    toy9 = ImageTk.PhotoImage(toy9)
    light = Label(second_frame, image=toy9)
    light.place(x=70, y=930)

    Llight = Label(second_frame, text=" ~ מנורה ~ ", fg="blue", font=("Arial", 15, "bold"))
    Llight.place(x=120, y=1190)

    Plight = Label(second_frame, text='מחיר: 30 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Plight.place(x=130, y=1230)

    Blight = Button(second_frame, text=" + ", fg="blue", command=lambda: show("מנורה"),
                    font=("Courier New", 13, "bold"), background="light blue")
    Blight.place(x=150, y=1270)

    toy10 = Image.open("dinosaurs.png")
    toy10 = toy10.resize((200, 250))
    toy10 = ImageTk.PhotoImage(toy10)
    dinosaurs = Label(second_frame, image=toy10)
    dinosaurs.place(x=370, y=930)

    Ldinosaurs = Label(second_frame, text=" ~ דינוזאורים ~ ", fg="blue", font=("Arial", 15, "bold"))
    Ldinosaurs.place(x=410, y=1190)

    Pdinosaurs = Label(second_frame, text='מחיר: 35 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Pdinosaurs.place(x=430, y=1230)

    Bdinosaurs = Button(second_frame, text=" + ", fg="blue", command=lambda: show("דינוזאורים"),
                        font=("Courier New", 13, "bold"), background="light blue")
    Bdinosaurs.place(x=450, y=1270)

    toy11 = Image.open("cat.png")
    toy11 = toy11.resize((200, 250))
    toy11 = ImageTk.PhotoImage(toy11)
    cat = Label(second_frame, image=toy11)
    cat.place(x=670, y=930)

    Lcat = Label(second_frame, text=" ~ בובת חתול ~ ", fg="blue", font=("Arial", 15, "bold"))
    Lcat.place(x=710, y=1190)

    Pcat = Label(second_frame, text='מחיר: 50 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Pcat.place(x=720, y=1230)

    Bcat = Button(second_frame, text=" + ", fg="blue", command=lambda: show("בובת חתול"), font=("Courier New", 13, "bold"),
                  background="light blue")
    Bcat.place(x=750, y=1270)

    toy12 = Image.open("plane.png")
    toy12 = toy12.resize((200, 250))
    toy12 = ImageTk.PhotoImage(toy12)
    plane = Label(second_frame, image=toy12)
    plane.place(x=970, y=930)

    Lplane = Label(second_frame, text=" ~ מטוס ~ ", fg="blue", font=("Arial", 15, "bold"))
    Lplane.place(x=1020, y=1190)

    Pplane = Label(second_frame, text='מחיר: 25 ש"ח', fg="blue", font=("Courier New", 13, "bold"))
    Pplane.place(x=1030, y=1230)

    Bplane = Button(second_frame, text=" + ", fg="blue", command=lambda: show("מטוס"),
                    font=("Courier New", 13, "bold"), background="light blue")
    Bplane.place(x=1050, y=1270)
    b1= Button(second_frame,text="- סל קניות - " ,fg="blue",command=lambda:pay_menu.page2(root), font=("Courier New", 13,"bold"), background="light blue").place(x=1050, y=20)


    root.mainloop()


if  __name__ == '__main__':
 page1(Tk())