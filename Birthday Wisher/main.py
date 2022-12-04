import smtplib

MY_EMAIL = "chiefdurotan@gmail.com"
PASSWORD = "durotan1996"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="adityasngh770@gmail.com", msg="Subject:Hello\n\nHello World")
