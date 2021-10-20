import mysql.connector
import datetime
import smtplib
import imghdr

conn = mysql.connector.connect(host="<Yoursqlserverhost>", user="<yoursqlusername>", passwd="<yoursqlserverpass>", database='<databasename>')
cur = conn.cursor()


def todays():
    tod = datetime.date.today()
    return tod


def monthed(tod):
    mon = tod.month
    return mon


def dayed(tod):
    day = tod.day
    return day


cur.execute(f"select name, email_id from datas where day(dob) = {dayed(todays())} AND MONTH(dob) = {monthed(todays())};")
r = cur.fetchall()
conn.close()
contacts = []
for rs in r:
    contacts.append(rs[1])

if not contacts:
    print("No birthdays")
else:
    from email.message import EmailMessage

    email_id = "<youremailid>@gmail.com"
    email_pwd = '<youremailpassword>'
    msg = EmailMessage()
    msg['Subject'] = "Happy Birthday To You"
    msg['From'] = email_id
    msg['To'] = contacts
    msg.set_content("Its your birthday! we wish you good fortune.\n Celebrate the most..\n From ARK-6")
    with open("birthday tempelate.png", 'rb') as f:
        filedat = f.read()
    filetype = imghdr.what(f.name)
    filensme = f.name
    msg.add_attachment(filedat, maintype="image", subtype="image-type", filename=filensme)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pwd)
        smtp.send_message(msg)
    print("success")

