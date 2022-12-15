## **Legit or Bit** 	

    is it legit or a bit?

Legit or Bit is a fact checking service bot that lives in Whats App. This bot is designed for those who have Meta subsided internet plans. These plans offer extra gibibytes or unlimited data for Meta products **ONLY**. It is unreasonable to expect people without easy and reliable internet access to be meticulous and thorough in verifying the veracity of the information they receive. So this tool offers those who have these plans a way to fact check websites and claims that may be shared to them or they may have themselves; without the risk of overages and charges on their phone plans.
We are powered by the Claim Busters Fact Checking API created by The University of Texas at Arlington. Which scores all user submissions. We also provide similar articles and information for article submissions which is done by contacting the Google Fact Explorer API.  

## Folder Contents 📁

xyz(TBD)

## How to 🤷‍♀️
#### How to use Legit or Bit as a user:
Send us a message through a device with Whats App installed.

📲 +13479054969

We accept any non-pay walled news article URL or a text submission:
#### Some examples:

     ➡ Was Tom Sawyer a real person

     ➡Is Messi Taller than Ronaldo

     ➡City College of New York is the best school for computer science

     ➡https://nonpaywalled_newsarticle.com


#### How to use Legit or Bit as a developer: 💻

Download the Legit or bit Folder located in this repo.

Install any requirements with the `requirements.txt` file.

Install Ngrok at https://ngrok.com/

Download their provided `Ngrok.exe`

Run it and make sure your account is verified ✅

Open Ngrok.exe

type in the command `ngrok.exe http 80` to get it running

Copy the Forwarding address 

* It should look something like this: 'https://some_numbers_yada_yada.ngrok.io'

Login to our Twilio page and go to: 
	
* Messaging in the side bar ➡ Senders ➡ WhatsApp Senders ➡ Scroll down to our WhatsApp number and click it. 🖱

Copy and paste the forwarding address to the ***Webhook URL for incoming messages*** and make sure to leave the */webhook* without any space in between. 

Finally scroll down and hit the blue button that says *Update WhatsApp Sender*
  
Go back to your favorite IDE 💻 and run `main.py`
  
The Ngrok tunnel will be connected to your console and you'll be able to see any and all traffic 🚦 to our code base.
	

*If you run into any errors, try to submit the same query again. This usually does the trick*

	🏁🏁 Now we are ready to rock and roll 🏁🏁

## Sample Images

<img src="https://user-images.githubusercontent.com/44910053/207897300-d785c3bd-6133-4753-beb6-b127c12bd59e.png" width=40% height=40%>   <img src="https://user-images.githubusercontent.com/44910053/207901492-76fa2009-43e9-4ce4-a2fa-cb752ea5a4e6.jpg" width=40% height=40%>

## Notes:

This application is still in testing and production, if you the user or developer messages the number provided above without having the Ngrok tunnel set up, you will recive no output. The tunnel currently is the only way we have connection to our code base.

Images are not accepted at this moment, for the future we want to have that service added to our project. 

We want to send back to the user information about the image:
		
		Meta Data
		
		If the image was altered
		
		Original source (done via reverse image search)
		
We also would like to find an additional service to provide professionaly facted checked articles. Since the Google Fact Check Explorer is very limted.
		
		This can be in the form of a API
		
		Or Simply a large dataset we can match similar queries and pull out of.
		
If you would like to add to out project, shoot us a message. We would love colaborators and fresh new ideas added to this service.
So we may all together help those with limited internet access!!
	

 
