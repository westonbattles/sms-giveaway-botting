
<h1 align="center", > SMS Giveaway Botting (Using Twilio)</h1>

A set of scripts that uses the twilio api to bot free coupons from sms response giveaways (I used this with a chipotle burrito coupon giveaway)




## Overview

- **Practicality** • The files in this project have a lot of practical applications with a wide variety of uses that aren't bound to botting coupon codes. These applications include (but are not limited to):

  - **Mass procurement of twilio phone numbers** • Useful for companies who do most of the server-user interaction using sms and therefore, need a large sum of phone numbers on hand (Food Delivery Services, Two Factor Authentication, etc..)
  - **Server automation for recieving sms messages using flask with ngrok** • Useful for apps that want to be able to recieve and save messages sent by the user
- **Ethical Dilemma** • While I am aware of the ethical dilemmas this entire project poses (spamming, ddos sms flooding), I do believe that this can equally do as much good. 
  - People can use these scripts to bot food giveaways (like the giveaway that started this whole project) and then give away the hundreds maybe even thousands of free coupons they get to homless people/shelters, kids and families who's soul source of food come from food vouchers, etc. The possibilities are literally endless. If you do end up using the code to bot coupon giveaways, I urge you to instead of finding a website where you can sell coupons easily for a quick profit, use the codes as a stepping stone to changing the world. It may not cure world hunger but 1000 free meals can go a long way.
  
 
 &nbsp;
   ```python
   from flask import Flask
   from flask_ngrok import run_with_ngrok
   ```
 &nbsp;
 
Flask is a python web framework that allows you to build localhost web applications with ease. Such ease in fact that it's widely considered one of the best options for client-side web frameworks in python. But for our use, in order to run a server that constantly checks all the incoming messages your twilio numbers are recieving, we have to expose this local server to the internet. This is where ngrok comes in. Now usually when setting up an ngrok server we have to first run our flask server, and then run ngrok in a seperate command shell, and then we finally get our ngrok url which we then need to put into updateurl.py script so we can automatically update
   
