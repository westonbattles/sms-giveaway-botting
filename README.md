
<h1 align="center", > sms-giveaway-botting</h1>

A set of scripts that uses the twilio api to bot free coupons from sms response giveaways (I used this with a chipotle burrito coupon giveaway)




## Overview

- **Practicality** • The files in this project have a lot of practical applications with a wide variety of uses that aren't limited to botting coupon codes. These applications include (but are not limited to):

  - **Mass procurement of twilio phone numbers** • Useful for companies who do most of the server-user interaction using sms and therefore, need a large sum of phone numbers on hand (Food Delivery Services, Two Factor Authentication, etc..)
  - **Server automation for recieving sms messages using flask with ngrok** • Useful for apps that want to be able to recieve and save messages sent by the user
  
 
 &nbsp;
   ```python
   from flask import Flask
   from flask_ngrok import run_with_ngrok
   ```
 &nbsp;
 
Flask is a python web framework that allows you to build localhost web applications with ease. Such ease in fact that it's widely considered one of the best options for client-side web frameworks in python. But for our use, in order to run a server that constantly checks all the incoming messages your twilio numbers are recieving, we have to expose this local server to the internet. This is where ngrok comes in. Now usually when setting up an ngrok server we have to first run our flask server, and then run ngrok in a seperate command shell, and then we finally get our ngrok url which we then need to put into updateurl.py script so we can automatically update
   
