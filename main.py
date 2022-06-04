# #################### Extra Hard Starting Project ######################

import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = "your"
MY_PASSWORD = "ggggh"
placeholder = "[NAME]"
birthdays_file = "birthdays.csv"

# 1. Update the birthdays.csv
birthdays = pd.read_csv(birthdays_file)
# birthdays_dict = birthdays.to_dict(orient="records")
# print(birthdays_dict)

# 2. Check if today matches a birthday in the birthdays.csv
datatime_now = dt.datetime.now()
day_now = datatime_now.date().day
month_now = datatime_now.date().month
tuple_now = (month_now, day_now)

new_dict_birthdays = {(row.month, row.day): {"name": row["name"], "email": row.email}
                      for index, row in birthdays.iterrows()}
if tuple_now in new_dict_birthdays:
    """
        3. If step 2 is true, pick a random letter from letter templates
        and replace the [NAME] with the person's actual name from birthdays.csv
    """
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        full_text = letter.read()
        result = full_text.replace(placeholder, new_dict_birthdays[tuple_now]["name"])
        # print(result)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=new_dict_birthdays[tuple_now]["email"],
                            msg=f"subject:Happy Birthday!\n\n{result}")


# for item in birthdays_dict:
#     if item["month"] != month_now and item["day"] != day_now:
#         """
#             3. If step 2 is true, pick a random letter from letter templates
#              and replace the [NAME] with the person's actual name from birthdays.csv
#         """
#         with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
#             full_text = letter.read()
#             result = full_text.replace(placeholder, item["name"])
#             print(result)


# 4. Send the letter generated in step 3 to that person's email address.
