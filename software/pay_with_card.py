from tkinter import messagebox
import tkinter as tk
import pay_menu###
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
from datetime import datetime
def pay_card(r):
    r.destroy()
    root = Tk()
    root.title('Pay with card')
    root.geometry("900x600")
    root.state('zoomed')

    def check_luhn(card_number):
        card_number = card_number.replace(" ", "")  # Remove spaces if any
        if not card_number.isdigit():
            return False

        total = 0
        reverse_digits = card_number[::-1]

        for i, digit in enumerate(reverse_digits):
            num = int(digit)
            if i % 2 == 1:  # Double every second digit
                num *= 2
                if num > 9:
                    num -= 9  # Subtract 9 if greater than 9
            total += num

        return total % 10 == 0  # Valid if divisible by 10

    def validate_expiration_date(expiration_date):
        try:
            exp_month, exp_year = map(int, expiration_date.split('/'))
            current_date = datetime.now()
            card_date = datetime(exp_year, exp_month, 1)
            return card_date > current_date
        except ValueError:
            return False

    def validate_cvv(cvv):
        if cvv.isdigit() and (len(cvv) == 4 or len(cvv) == 3):
            return True
        else:
            return False

    def on_entry_click(event, default_text):
        if event.widget.get() == default_text:
            event.widget.delete(0, tk.END)
            event.widget.config(fg="black")

    def on_focusout(event, default_text):
        if event.widget.get() == "":
            event.widget.insert(0, default_text)
            event.widget.config(fg="light gray")

    def create_error_label(text, x, y):
        global error_label
        error_label = Label(root, text=text, fg="red", font=("Arial", 15))
        error_label.place(x=x, y=y)

    def valid_pay(name,num, date, cvv):
        if "error_label" in globals() and error_label.winfo_exists():
            error_label.destroy()

        if  name.get().startswith("                                          שם בעל הכרטיס"):
            create_error_label("הכנס שם בעל הכרטיס", 300,135)

        elif  num.get().startswith("                                    מספר כרטיס אשראי"):
            create_error_label("הכנס מספר כרטיס", 300,175)
        elif check_luhn(num.get()) == False:
            create_error_label("מספר כרטיס אשראי לא תקין", x=250, y=175)

        elif  date.get().startswith("                                     (MM/YYYY)  תוקף "):
            create_error_label("הכנס תוקף כרטיס", 300,215)
        elif validate_expiration_date(date.get()) == False:
            create_error_label("תוקף אשראי לא תקין", x=250, y=215)

        elif  cvv.get().startswith("                                                           cvv"):
            create_error_label("cvv הכנס ", 300,255)
        elif validate_cvv(cvv.get()) == False:
            create_error_label("CVV לא תקין", x=250, y=255)

        elif check_luhn(num.get()) == True and validate_expiration_date(date.get()) == True and validate_cvv(
                cvv.get()) == True:
            messagebox.showinfo("Payment Successful", " !התשלום עבר בהצלחה ")

    # Function to validate payment details
    label1 = Label(root, text="- תשלום באשראי -", fg="blue", font=("Arial", 40, "bold")).place(x=650, y=40,
                                                                                               anchor=CENTER)
    b1= Button(root,text="  חזרה --> " ,fg="blue",command=lambda:pay_menu.page2(root), font=("Arial", 14,"bold"), background="light blue").place(x=1090, y=20)

    name_on_the_card = tk.Entry(root, font=("Arial", 14), width=30, fg="light gray")
    name_on_the_card.insert(0, "                                          שם בעל הכרטיס")
    name_on_the_card.bind("<FocusIn>", lambda e, text="                                          שם בעל הכרטיס": on_entry_click(e, text))
    name_on_the_card.bind("<FocusOut>", lambda e, text="                                           שם בעל הכרטיס": on_focusout(e, text))
    name_on_the_card.place(x=500, y=140)

    credit_card_num = tk.Entry(root, font=("Arial", 14), width=30, fg="light gray")
    credit_card_num.insert(0, "                                    מספר כרטיס אשראי")
    credit_card_num.bind("<FocusIn>", lambda e, text="                                    מספר כרטיס אשראי": on_entry_click(e, text))
    credit_card_num.bind("<FocusOut>", lambda e, text="                                    מספר כרטיס אשראי": on_focusout(e, text))
    credit_card_num.place(x=500, y=180)

    expiration_date = tk.Entry(root, font=("Arial", 14), width=30, fg="light gray")
    expiration_date.insert(0, "                                     (MM/YYYY)  תוקף ")
    expiration_date.bind("<FocusIn>", lambda e, text="                                     (MM/YYYY)  תוקף ": on_entry_click(e, text))
    expiration_date.bind("<FocusOut>", lambda e, text="                                     (MM/YYYY)  תוקף ": on_focusout(e, text))
    expiration_date.place(x=500, y=220)

    cvv = tk.Entry(root, font=("Arial", 14), width=30, fg="light gray")
    cvv.insert(0, "                                                           cvv")
    cvv.bind("<FocusIn>", lambda e, text="                                                           cvv": on_entry_click(e, text))
    cvv.bind("<FocusOut>", lambda e, text="                                                           cvv": on_focusout(e, text))
    cvv.place(x=500, y=260)
    Bpay = Button(root, text=" - שלם - ", command=lambda: valid_pay(name_on_the_card,credit_card_num, expiration_date, cvv), background="blue", fg="white", font=("Arial", 14,"bold")).place(x=620,
                                                                                                            y=310)

    root.mainloop()


if __name__ == '__main__':
    pay_card(Tk())

