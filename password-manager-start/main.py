from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle 
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters =[choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    
    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    password= password_input.get()
    email_input =  email.get()
    new_data ={
        website:{
            "email": email_input,
            "password": password
        }
        
    }

    
    if len(password)==0  or len(website)==0 :
        messagebox.showinfo(title="Oops", message="You have left some fields empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
               
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving the new data
                json.dump(new_data, data_file, indent=4)
                data.update(new_data)
       
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving the new data
                json.dump(data, data_file, indent=4)
               
        
        finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
               
def find_password():
    website= website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website_input.get() in data:
            email = data[website]["email"]
            password =data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
        elif website_input.get() not in data:
            messagebox.showinfo(title="Error", message=f"No data for the {website} exists")
        
# ---------------------------- UI SETUP ------------------------------- #



window= Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
Input_details=Text(window)

#creating a canvas
canvas= Canvas(height=200,width=200)
logo_img= PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)


# creating various labels
website= Label(text="Website:")
website.grid(column=0,row=1)

Email = Label(text="Email/Username:")
Email.grid(column=0,row=2, columnspan=1)

password= Label(text="Password:")
password.grid(column=0,row=3)


# creating Entries
website_input= Entry(width=21)
website_input.grid(column=1,row=1)
website_input.focus()

email= Entry(width=35)
email.grid(column=1,row=2,columnspan=2)
email.insert(0,"faizalautomation0513@gmail.com")


password_input =Entry(width=21)
password_input.grid(column=1,row=3)



generate_password= Button(text="Generate Password",bg="white",command=generate_passwords)
generate_password.grid(column=2,row=3)


add= Button(bg="white",text="Add",width="36",command=save)
add.grid(column=1,row=4,columnspan=2)

search_button = Button(bg="white", text="Search",command=find_password, width=13)
search_button.grid(column=2,row=1,columnspan=3)



window.mainloop()
