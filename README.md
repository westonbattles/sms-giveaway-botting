
<h1 align="center", > SMS Giveaway Botting (Using Twilio)</h1>

A set of scripts (using the twilio api) that among other things, can bot sms response giveaways




## Overview

- **Practicality** • The files in this project have a lot of practical applications with a wide variety of uses that aren't bound to botting coupon codes. These applications include (but are not limited to):

  - **Mass procurement of twilio phone numbers** • Useful for companies who do most of the server-user interaction using sms and therefore, need a large sum of phone numbers on hand (Food Delivery Services, Two Factor Authentication, etc..)
  - **Server automation for recieving sms messages using [flask with ngrok](README.md#About-Flask)** • Useful for apps that want to be able to recieve and save messages sent by the user
- **Ethical Dilemma** • While I am aware of the ethical dilemmas this entire project poses (spamming, ddos sms flooding), I do believe that this can equally do as much good. 
  - People can use these scripts to bot food giveaways (like the giveaway that started this whole project) and then give away the hundreds maybe even thousands of free coupons they get to homless people/shelters, kids and families who's soul source of food come from food vouchers, etc. The possibilities are literally endless. If you do end up using the code to bot coupon giveaways, I urge you to instead of finding a website where you can sell coupons easily for a quick profit, use the codes as a stepping stone to changing the world. It may not cure world hunger but 1000 free meals can go a long way.
  
## Table of Contents

<ul>
    <li><a href="#Installing">Installing</a></li>
    <li><a href="#Setup">Setup</a></li>
    <li><a href="#Running">Running the bot</a></li>
    <li><a href="#Inspiration">Inspiration</a></li>
    <li><a href="#About-Flask">About Flask</a></li>
  </ul>

## Installing
 
Before you begin, make sure you have Python 3 + pip installed. To check if you have these installed run `python -V` (make sure the version is python 3.X.X) and `python -m pip -V`. If you don't have these installed please read the guide below

### Installing Python 3 for Windows

Click on the following link and open it once it's downloaded:

`https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe`

Once you have opened the installer, make sure that you add Python 3.8 to path. Your installer should look like this:

<img align="center" src="https://i.imgur.com/SkviBw6.png">

### Installing Python for MacOS.

Click on the following link and install:

`https://www.python.org/ftp/python/3.8.0/python-3.8.0-macosx10.9.pkg`

### Installing Python for Linux

Since there are a multitude of package installers for Linux, we'll choose `apt` which is used in Debian-derived distros such as Ubuntu as an example.

Go to the terminal and type in the following:

```shell
sudo apt update && sudo apt upgrade
sudo apt install -y python3 python3-pip
```


# Setup

### Getting Access to the Twilio API

The first thing you have to do is sign up to Twilio if you don't already have an account

<br>

Click on the link to the [Twilio Login Page](https://www.twilio.com/try-twilio) and sign up

Once you are logged in navigate to the [Console](https://console.twilio.com/?frameUrl=/console) and there you should see your Account Sid and Auth Token

<img src="https://i.imgur.com/r8Qtxzc.png"
   width="1000">
   
These two codes are what will let you talk to Twilio using the API, so make sure no one else sees them or else they'll have access to all of your phone numbers

 &nbsp;
   ```python
   from flask import Flask
   from flask_ngrok import run_with_ngrok
   ```
 &nbsp;
 
## About Flask
 
Flask is a python web framework that allows you to build localhost web applications with ease. Such ease in fact that it's widely considered one of the best options for client-side web frameworks in python. But for our use, in order to run a server that constantly checks all the incoming messages your twilio numbers are recieving, we have to expose this local server to the internet. This is where ngrok comes in. Now usually when setting up an ngrok server we have to first run our flask server, and then run ngrok in a seperate command shell, and then we finally get our ngrok url which we then need to put into updateurl.py script so we can automatically update
   
