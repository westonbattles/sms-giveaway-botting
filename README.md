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
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Inspiration">Inspiration</a></li>
    <li><a href="#Flask-and-Ngrok">Flask and Ngrok</a> (Networking frameworks used in tandom to allow the creation of this project and many other web applications</li>
  </ul>

## Installing
 
Before you begin, make sure the number you want to send messages to complies with the [Twilio SMS Limitations](https://support.twilio.com/hc/en-us/articles/223134047-Can-my-Twilio-number-send-SMS-to-a-non-Twilio-short-code-).

In addition, make sure you have Python 3 + pip installed. To check if you have these installed run `python -V` (make sure the version is python 3.X.X) and `python -m pip -V`. If you don't have these installed please read the guide below

### Installing Python3 for Windows

Click on the following link and open it once it's downloaded:

`https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe`

Once you have opened the installer, make sure that you add Python 3.8 to path. Your installer should look like this:

<img align="center" src="https://i.imgur.com/SkviBw6.png">

### Installing Python3 for MacOS.

Click on the following link and install:

`https://www.python.org/ftp/python/3.8.0/python-3.8.0-macosx10.9.pkg`

### Installing Python3 for Linux

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

Click on the link to the [Twilio Login Page](https://www.twilio.com/try-twilio) and follow the steps to create an account

Once you are logged in navigate to the [Console](https://console.twilio.com/?frameUrl=/console) and there you should see your Account Sid and Auth Token

<img src="https://i.imgur.com/r8Qtxzc.png"
   width="1000">
   
These two codes are what will let you talk to Twilio using the API, so make sure no one else sees them or else they'll have access to pretty much your entire account

### Setting your environment variables on Windows


<br>
  
```python
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
```

<br>

As you can see, my code accesses the data from two environment variables, one called `TWILIO_ACCOUNT_SID` and one called `TWILIO_AUTH_TOKEN`

The first step is to press ``⊞ Win`` + ``R`` and type in the command `sysdm.cpl`

<br>

This should open up your system properties

Next, you want to navigate to the `Advanced` tab and click `Environment Variables...`

<img src="https://user-images.githubusercontent.com/50222899/128274669-36df8d2d-161c-4b6e-a72f-b74de0dfaabf.JPG">

You then want to click `New...` under user variables or system variables (depending on if you want these variables to be accessible by ever user on your computer or just by you)

Then, carefully type in the variable name slot: `TWILIO_ACCOUNT_SID`

Next, copy & paste your account sid from earlier into the variable key like so:

<img src="https://user-images.githubusercontent.com/50222899/128275175-0142193d-aa4d-4ee1-9ce9-83b8d081b869.JPG">

Hit `OK`, and then do the same thing but this time name the new variable: `TWILIO_AUTH_TOKEN` 

paste your auth token into the key slot and hit `OK` again

### Setting your environment variables on macOS/Linux

I don't currently have an operational macOS/Linux device, however after 2 minutes of research I found this article and I wanted to give credit instead of essentially copy and pasting the tutorial into here so:
<a href="https://www.schrodinger.com/kb/1842">https://www.schrodinger.com/kb/1842</a>

<br>

### Installing the files



There are two ways to install the files, using `git` or manually

For the first option, all you have to do is navigate (using the command line) to the folder you want to install the files into
make sure you have git installed and run the command:

`git clone https://github.com/westonbattles/sms-giveaway-botting.git`

If your computer tells you that git isn't installed, please follow <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">this guide</a> on installing git

<br>

For the manual way, all you have to do is download the zip of this repository and extract it to where you want all the files to be stored

<br>

### Installing the requried packages

Now that we've installed all the files (including `requirments.txt`) we need to install all the requried packages

All we have to do to achieve this is go into the command line and navigate to the folder you installed everything to (it should contain the `requirements.txt` file)

Once you're in the folder run the command `pip install -r requirments.txt`

<br>

## Usage

The very first step is to figure out how many Twilio phone numbers you want to use. The price of each number is 1 USD, so we need to fill up our twillio account with the funds neccescary to purchase all the numbers we need.

- Ideally, the total number of Twilio phone numbers you want should be divisible by 30. This is because that is the max amount of available numbers you can search for at a time with the Twilio API. My code then asks you how many sets (of the `limit` variable, 30 by default) you would like to buy. 
- If you want to change this number, the variable is located in `buynumbers.py`, but a fair warning, making the limit lower so you can get a more percise number is horribly more ineffecient.
- I urge you to leave the variable unchanged if the exact number isn't important

Once you figure out how much money needs to be in your Twilio account, you can head over to your [billing overview](https://console.twilio.com/us1/billing/manage-billing/billing-overview?frameUrl=%2Fconsole%2Fbilling%3Fx-target-region%3Dus1) and add the funds neccessary

Congratulations! You are now ready to purchase your Twilio numbers

<br>

The next step is to run your ngrok server


### Setting up your server

In order to start your server, all you really have to do is run the `recieve_responses.py` file

running this file should start the server, and you'll see three addresses, the one you want to copy is the one that contains: `ngrok.io`

<img src="https://user-images.githubusercontent.com/50222899/128288201-4dc13210-7b93-46a9-b23b-62b8998b0cb6.JPG">

Now we can purchase our numbers

<br>

### Buying the numbers

Now all we have to do is run `buynumbers.py`

Running this script should prompt the user to enter their ngrok server **(with /sms added)**
Simply paste the server adress you just copied and type: `/sms` (be careful not to add anything else)

Before you hit enter your address should look like this:
`http://ex2amp1e3.ngrok.io/sms`

<br>

Next, you should be prompted to enter the number of sets you want to buy. Remember, (unless you changed the `limit` variable, there are 30 numbers in each set, so if I were to type in `10`, I would buy 300 phone numbers and therefore need 300 dollars in my account beforehand

Press enter if you believe you did everything correctly

The program should run for a bit and then close on its own without error. Congratulations, you are now the proud owner of a crazy amount of Twilio phone numbers! :)

<br>

### Updating the ouput address of old phone numbers

If you haven't purchased any phone numbers before this project, or if you have no intrest of automatically changing the output server address of any of your old Twilio phone numbers, you can go ahead and skip this section

I only wrote this because I had manually bought 20 numbers before I got the idea to automate it and I wanted to automate a way to change the address of those numbers so I didn't have to manually go through and do it.

All you have to do is run `updateurl.py` and then when you are prompted to enter your ngrok address, follow the same steps as before

Paste in your address and **BE SURE** to remember to add `/sms` at the end, it should look like this: `http://ex2amp1e3.ngrok.io/sms`

<br>

The program will then loop through every phone number in your account and update the urls that arent already the url you gave 

<br>

### The time has come to send the messages

The last step is to run: `send.py`

<br>

Once this file runs, it will prompt you to enter the phone number of the recipient. The format of this phone number should be as follows: 

`+15550001111`


After entering a valid phone number, the program will then ask you to enter the message you want to send that number. Once you hit enter the program will then loop through every phone number you own and send one text containing that message to the recipient from each number.

<br>

## Inspiration

A few weeks ago, I was working on a discord bot when my friend messages me on discord with this article:

<a href="https://www.fastcompany.com/90653871/chipotle-is-giving-away-1-million-in-free-burritos-heres-how-to-get-yours">https://www.fastcompany.com/90653871/chipotle-is-giving-away-1-million-in-free-burritos-heres-how-to-get-yours</a>

<br>

The article describes a marketing event Chipotle announced they were doing. For this event, they announced that for every game in the NBA championship Chiptole would have a special commerical. During this commerical, a special code would be released. The first 40,000 people to text this code to the Chipotle number would instantly recieve a free burrito coupon.

I thought this was interesting but my plan didn't formulate until I took a shower. It kind of just hit me like an out of place water droplet. I got out and instantly started work on this massive project.

## Flask and Ngrok
 
Flask is a python web framework that allows you to build localhost web applications with ease. Such ease in fact that it's widely considered one of the best options for client-side web frameworks in python. 

But for our use, in order to run a server that constantly checks all the incoming messages your twilio numbers are recieving, we have to expose this local server to the internet. This is where ngrok comes in. Now usually when setting up an ngrok server we have to first run our flask server, and then run ngrok in a seperate command shell, and then, finally, get our ngrok url.

Thankfully, to ease our pain a little bit, theres a program called `flask-ngrok` devloped by [Grant Stafford](https://pypi.org/user/gstaff/) which just acts as a way to automate the process of setting up an ngrok server

 &nbsp;
   ```python
   from flask import Flask
   from flask_ngrok import run_with_ngrok
   ```
 &nbsp;

When we call run_with_ngrok and pass in our flask app, all you have to do is watch as flask-ngrok automatically sets up an ngrok server for us and outputs the link to console
   
