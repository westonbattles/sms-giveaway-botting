import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

list = open("phonenumbers.txt").read()
numbers = list.splitlines() #creates a list of the phone numbers you own based off of what's in each line of 'phonenumbers.txt'

#sets the recipients phone number and message you want to mass send to them
endpoint = input("Enter the phone number of the recipient (Remember the format has to be '+15555555555' and Twilio doesn't support sending messages to short numbers): ")
message = input("Enter the message you want to send: ")



client = Client(account_sid, auth_token)

for number in numbers:
    client.messages.create(
        to=endpoint,
        from_=number,
        body=message
    )


