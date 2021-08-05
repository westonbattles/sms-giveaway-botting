import os
from twilio.rest import Client
from requests import post

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)
url = input("enter ngrok url (dont forget to add /sms): ")


numbers = client.incoming_phone_numbers.list()

#makes sure that every phone number you own has the correct url, changes it if it doesnt
for i in numbers:
    if i.sms_url != url:
        i.update(sms_url=url)
