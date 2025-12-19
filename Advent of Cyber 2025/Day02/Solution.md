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
- `ls`
- `./server.py`

## Process

I started the AttackBox and Virtual Machine to connect to the lab environment.

The goal of this task was to acquire user login credentials through a phishing attack. A fake login page was already provided and needed to be hosted locally. This page was designed to capture any credentials entered by the user and display them in the terminal.

To host the fake login page, I navigated to the provided directory:

```bash
cd ~/Rooms/AoC2025/Day02
```

I listed the files in the directory:

```bash
ls
```

The directory contained `index.html` and `server.py`. The `server.py` script is responsible for hosting the phishing page.

I started the server using:

```bash
./server.py
```

Once the server was running, it hosted the fake login page and began listening for credentials. Any credentials entered by the target user were displayed directly in the terminal.

## Result
- Credentials were successfully captured
- The obtained password was reused to access the email portal
- Task questions were answered using the captured information

## Notes
- The phishing page must be hosted before sending the email
- SET simplifies the process of crafting and sending phishing emails
- Monitoring the terminal is required to capture submitted credentials

## Takeaways
- Phishing attacks rely more on user trust than technical exploits
- Credential harvesting can be set up with minimal effort
- Password reuse significantly increases the impact of phishing attacks
