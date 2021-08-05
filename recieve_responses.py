from flask import Flask, request, redirect
from flask_ngrok import run_with_ngrok
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
run_with_ngrok(app) #automated way to use ngrok so you dont have to manually do it

@app.route('/sms', methods=['GET', 'POST'])
def incoming_sms():

    #writes every response any one of your phone numbers recieve to 'responses.txt' seperated by a line break
    file = open("responses.txt", "a")
    message = request.values.get('Body', None)
    file.write(message +"\n \n")

    return str(message)

if __name__ == "__main__":
    app.run()


"""

IMPORTANT - running this file should print the ngrok link in the console (ex: http://000000000000.ngrok.io

make sure you add /sms before you use this link in buynumbers.py / updateurl.py or else this will not work

"""



