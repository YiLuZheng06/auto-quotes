About: AutoQuote is a simple, comfy, Studio Ghibli-themed website that authenticates users. Once authenticated, the user will see a live time and quote displayed. Simultaneously, an email will be sent to a recipient. 

Features: In the frontend, I used CSS to create the dynamics of user interaction with the buttons and log-in form. Additionally, the AOS library was used to create moving elements on the page. In the backend, I used the smtp library to create a log-in functionality that authenticates users with Zoho mail. I used an API call to get random quotes. 

Time Spent: I would estimate that I spent around 5 hrs on this project, including researching, debugging, and testing. 

How to run:
Video - https://youtu.be/Rir8JIH0EJg
1) Before replicating the repository, please create a personal Zoho mail (https://www.zoho.com/mail/). It's free to sign up and should be quick! I ask to do this because authentication with SMTP with other email clients such as Gmail and Outlook runs into complications with their two-step verification. Zoho mail has no issues with that 👍.
2) Replicate the repository into Vscode. You may have to install the libraries flask, flask_cors, requests, and anything else (will be indicated by a squiggly line). Make sure to use pip install <library> in a virtual environment (.venv\Scripts\activate) 
3) IMPORTANT - Go into the main.py file and CHANGE the TO_EMAIL to your desired recipient. (located on line 35) Note this email could be other email clients other than Zoho. (I used Gmail in my demo)
4) Finally, enter - python main.py - to run the program
5) Enjoy :)
