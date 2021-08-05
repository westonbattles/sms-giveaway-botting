import os
from twilio.rest import Client
from requests import post

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

#ngrok url with /sms added
url = input("enter ngrok url (dont forget to add /sms): ")

limit = 30 #limit to increase effeciency for higher quantity
           #twilio caps the phone number search at 30 so going any higher wont do anything

# how many times you want to buy numbers (in sets of the limit)
n = int(input("How many sets of phone numbers (each set is "+str(limit)+" numbers) do you want to buy?"))

for i in range(n):
    available = client.available_phone_numbers('US').local.list(limit=limit)

    for each in available:
        get_phone_number = client.incoming_phone_numbers \
              .create(phone_number=each.phone_number)

        #writes every phone number you buy to a text file to use for when you send the message
        file = open("phonenumbers.txt", "a")
        file.write("\n"+each.phone_number)

        #automatically changes the webhook url to your ngrok url so you
        #dont have to manually go through each number on the website and change it
        get_phone_number.update(sms_url=url)

