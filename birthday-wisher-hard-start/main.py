
import pandas
from datetime import datetime
import random
import smtplib
my_email = "faizamohamed0511@gmail.com"    
password = "zjudhwzcgawskhxb"

today=datetime.now()
today_tuple=(today.day,today.month)



data= pandas.read_csv("birthdays.csv")
birthday_dict={(data_row["month"],data_row["day"]):data_row for(index,data_row)in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content= letter_file.read()
        name=content.replace("[NAME]",birthday_person["name"])
        print(name)
    
   


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="pythonfaizal@gmail.com",
                            msg=name
        )




