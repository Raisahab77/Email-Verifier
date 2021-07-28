import smtplib
import random

s = "0123456789"
# This will generate a 6 element list
otp = random.sample(s,6)
#This will convert list into string
otp = "".join(otp)
print(otp)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

# Here You have to Enter a Email address and a password If you face any error check your email setting and enable less secure device option. 
s.login("Your Email", "Your Password")

message = otp

# Here 6 digit OTP send on reciever's Email 
s.sendmail("Your Email", "Reciever Email", message)

s.quit()

userInput = input("Enter your OTP :")
if userInput == otp:
    print("OTP is correct")
else:
    print("OTP is wrong")