# BirthdayWisher

Requirements: "mysqlserver", "email id and password", "Mysqlconnector"

In-Built Modules: "smtplib", "datetime","imghdr"

In Mysql:
 A table with three columns "name, dateofbirth(dob), email id of users"

Logic:
  --> Fetching month and day using datetime module
  --> Writing sql query using f strings and selecting emails from database
  --> Adding all emails which are fetched into an list
  --> Using smtplib making birthday wishes and adding an image attachment
  --> With smtp_SSL and port 465 sending email
  

CREDITS: [Ihyth](https://github.com/ihyth),  [Anvith](https://github.com/Anvith-01)
