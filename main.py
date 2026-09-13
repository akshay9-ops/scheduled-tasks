##################### Extra Hard Starting Project ######################
import os
import random
import smtplib
import datetime as dt

# Secrets come from environment variables (set as GitHub Actions secrets),
# never hardcoded here.
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
current_date = now.day
current_month = now.month

# 1. Update the birthdays.csv
with open("birthdays.csv", "r") as bday_file:
    birthdays = bday_file.readlines()
    for birthday in birthdays[1:]:
        birthday_data = birthday.split(",")
        name = birthday_data[0]
        email = birthday_data[1]
        year = int(birthday_data[2])
        month = int(birthday_data[3])
        date = int(birthday_data[4])

        # 2. Check if today matches a birthday in the birthdays.csv
        if current_date == date and current_month == month:
            letter_list = [
                "letter_templates/letter_1.txt",
                "letter_templates/letter_2.txt",
                "letter_templates/letter_3.txt",
            ]
            random_letter = random.choice(letter_list)
            with open(random_letter, "r") as file:
                contents = file.read()
                contents = contents.replace("[NAME]", f"{name}")

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: Happy Birthday!\n\n{contents}",
                )
