# Phishing - Merry Clickmas

## Objective

- Understand what social engineering is
- Learn the types of phishing
- Explore how red teams create fake      login pages
- Use the Social-Engineer Toolkit to send a phishing email

## Environment / Tools

## OS / VM / AttackBox
- AttackBox
- Virtual Machine
Tools and commands used

## Process

To connect to the virtual environment, I first started the AttackBox and Virtual Machine. 


This task aims to acquire the login credentials of the user. For this, I had to send a phishing email to the user with the help of a Social Engineering Toolkit (SET). There already exists a fake login page here which has to be hosted by running the script. This script is designed in such a way so as to capture the user credentials when entered into the login page.


To first host this fake login page, run the script by changing the directory to 
```~/Rooms/AoC2025/Day02```


By using the ```ls``` command one can see that there are two files index.html and server.py. 
The server.py file consists of the script and to run it, use 
```./server.py```


This server now hosts a fake login page and starts listening for credentials. If the target user enters the credentials, it will be shown on the same terminal.


Result

Flag / answer obtained

Output that mattered

Notes

Observations made while doing the task.

Why a step was required

What worked as expected

Any mistakes or adjustments

Takeaways

What this task reinforced or introduced.

Concept learned

Technique practiced

Thing to remember for later

