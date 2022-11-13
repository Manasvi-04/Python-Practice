import smtplib
import datetime as dt
import random


my_email = "kidaofspam@gmail.com"
password = "Sahil:05"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    with open("quotes.txt") as quotes:
        list = quotes.readlines()
        now = dt.datetime.now()
        day_of_week = now.weekday()
        if day_of_week == 1 :
            connection.sendmail(from_addr=my_email, to_addrs="rajsahil1228@yahoo.com",
                                msg=f"Subject:Tuesday Quote\n\n{random.choice(list)}")

