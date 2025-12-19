# Phishing – Merry Clickmas

## Objective
- Understand what social engineering is
- Learn the types of phishing
- Explore how red teams create fake login pages
- Use the Social-Engineer Toolkit to send a phishing email

## Environment / Tools
### OS / VM
- AttackBox
- Virtual Machine

### Tools and Commands
- Social-Engineer Toolkit (SET)
- Python
- ls
- ./server.py
- setoolkit

## Process
I started the AttackBox and Virtual Machine to connect to the lab environment. The goal of this task was to acquire user login credentials through a phishing attack. A fake login page was already provided and needed to be hosted locally. This page was designed to capture any credentials entered by the user and display them in the terminal.

To host the fake login page, I navigated to the provided directory using `cd ~/Rooms/AoC2025/Day02` and listed the files using `ls`. The directory contained `index.html` and `server.py`, where `server.py` is responsible for hosting the phishing page. I started the server using `./server.py`. Once the server was running, it hosted the fake login page and began listening for credentials. Any credentials entered by the target user were displayed directly in the terminal.

After setting up the phishing page, I used the Social-Engineer Toolkit to compose and send a phishing email. I started SET using `setoolkit`, selected Social-Engineering Attacks, chose Mass Mailer Attack, and then selected the option to send an email attack to a single email address. During the setup, I configured the target email address, delivery method, spoofed sender details, SMTP server address, and port number. Since an open relay was used, the username and password fields were left blank. I then provided a suitable subject and a convincing email body containing the phishing link. After a short wait, the captured admin credentials appeared in the terminal running the phishing server.

## Answers
What is the password used to access the TBFC portal?  
`unranked-wisdom-anthem`

What is the total number of toys expected for delivery?  
`1984000`

## Result
- Credentials were successfully captured
- The obtained password was reused to access the email portal
- Task questions were answered using the captured information

## Notes
- The phishing page must be hosted before sending the email
- SET simplifies phishing email delivery
- Monitoring the terminal is required to capture credentials

## Takeaways
- Phishing relies more on user trust than technical exploits
- Credential harvesting can be set up with minimal effort
- Password reuse significantly increases attack impact
