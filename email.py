import smtplib

user="ishita2277@gmail.com"
receiver="jaindhairya2001@gmail.com"
psd="password"
msg="Hey there..!!! I send you this via python......"

s=smtplib.SMTP_SSL('smtp.gmail.com',587)
print('opening gmail')
s.starttls()
s.login(user,psd)
print('logged in')
s.sendmail(user,receiver,msg)
print('sending mail')
s.quit()
print("logged out")
