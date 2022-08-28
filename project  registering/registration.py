from msilib.schema import CheckBox
from tkinter import *
import smtplib
import random
from tkinter import messagebox, filedialog
import math

# from PIL import ImageTk

rndm_number = digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]



def sending_email():
    reciever = gml.get()
    if reciever == '':
        messagebox.showerror("invalid!", "invalid Email!")
    else:

        sender = "b01naimboss1@gmail.com"
        pasword = "jfeszmlulismrcyx"
        mesage = f"""
        your verification code is : {OTP}

        """
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        
        server.login(sender,pasword)
        server.sendmail(sender,reciever,mesage)
        messagebox.showinfo("Success!!", "Your verification mail has been sent!")
        sending_verification_code_entry.config(state=DISABLED)
        send_verification_code_button.config(state=DISABLED)
    

def verify():
    if OTP == verification_code_verify.get():
        messagebox.showinfo("verification", "Verification success!")
        verify_button.config(state=DISABLED)
        password_entry.config(state=NORMAL)
    else:
        messagebox.showerror("verification", "invalid verification code.")

def show_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')


def submit_function():
    if gml.get() == '' or verification_code_verify.get() == '' or first_name_input.get() == '' or last_name_input.get() == '' or username_input.get() == '':
        messagebox.showerror("Error!!", "Registration form not filled!")
        return
    else:
        print(f"{gml.get()}\n {first_name_input.get()}\n {last_name_input.get()}\n {username_input.get()}\n ")
        messagebox.showinfo("Success!!", "Registration successful!")
        submit_button.config(state=DISABLED)

    
win = Tk()
win.geometry("500x300")
win.resizable(width=False, height=False)
win.config(bg="Black")
win.title("Registration")

#getting input from user
gml = StringVar()
verification_code_verify = StringVar()
first_name_input = StringVar()
last_name_input = StringVar()
username_input = StringVar()
password_entry_input = StringVar()




background_img = PhotoImage(file="bg.png")

background_image = Label(win, image=background_img,anchor=NW)
background_image.place(x=0, y=0, relwidth=1, relheight=1)

getting_gmail_text = Label(win, text="Gmail Adress",bg="#05c9f5")
getting_gmail_text.grid(row=0,column=0,padx=2, pady=2)

sending_verification_code_entry = Entry(win, width=25, textvariable=gml,bg="#05c9f5",fg="Black",font=("Arial", 15))
sending_verification_code_entry.grid(row=0,column=1,padx=2, pady=2)

send_verification_code_button = Button(win,width=10,text= "Send", command=sending_email, bg="#03fc4e")
send_verification_code_button.grid(row=0, column=2, padx=5, pady=5)


checking_verifcation_code_text = Label(win, text="Verify", bg="#05c9f5",width=10)
checking_verifcation_code_text.grid(row=1, column=0, padx=3, pady=3)

checking_verifcation_code = Entry(win, width=15, textvariable=verification_code_verify, bg="#05c9f5",fg="Black")
checking_verifcation_code.grid(row=1, column=1, padx=2, pady=2)

verify_button = Button(win, text="Verify",width=10,command= verify, bg="#03fc4e")
verify_button.grid(row=1, column=2, padx=3, pady=3)

first_name_Label = Label(win, text="First Name", bg="#05c9f5", width=10)
first_name_Label.grid(row=2, column=0, padx=5, pady=5)

first_name_entry = Entry(win, width=30, textvariable=first_name_input, bg="#05c9f5", fg="black")
first_name_entry.grid(row=2, column=1)

last_name_label = Label(win, text="Last Name", bg="#05c9f5", width=10)
last_name_label.grid(row=3, column=0)

last_name_entry = Entry(win,width=30, textvariable=last_name_input, bg="#05c9f5", fg="black")
last_name_entry.place(x=135, y= 100)

username_label = Label(win, text="Username", bg="#05c9f5", width=10)
username_label.place(x=5, y=125)

username_entry = Entry(win, width=30, textvariable=username_input, bg="#05c9f5", fg="black")
username_entry.place(x=135, y=125)

password_label = Label(win, text="Password", bg="#05c9f5", width=10)
password_label.place(x=5, y=150)

password_entry = Entry(win, width=30, textvariable=password_entry_input,bg="#05c9f5", fg="black",show="*", state=DISABLED)
password_entry.place(x=135, y=150)

show_password_checkbox = Checkbutton(win, text="show password", command=show_password, bg="#05c9f5")
show_password_checkbox.place(x=135, y=175)

submit_button = Button(win,text="Submit", width=10, command=submit_function, bg="#03fc4e")
submit_button.place(x=140,y= 205)



if __name__=='__main__':
    win.mainloop()
    