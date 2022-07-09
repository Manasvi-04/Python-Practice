import pandas
import datetime as dt
import smtplib
import random

my_email = "kidaofspam@gmail.com"
password = "Sahil:05"


data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
today_day = today.day
today_month = today.month
today_tuple = (today_month, today_day)

data_dic = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in data_dic:
    b_person = data_dic[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        l = letter.read()
        letter_to_send = l.replace("[NAME]", b_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as email:
        email.starttls()
        email.login(user=my_email, password=password)
        email.sendmail(from_addr=my_email, to_addrs=b_person.email, msg=f"Subject:Happy Birthday\n\n{letter_to_send}")








