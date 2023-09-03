<h1 align="center">freetempmail - Temp-Mail.org API wrapper.</h1>

<h3 align="center">How to Use?</h3>

<h4 align="center">Quickstart Guide</h4>

```python
import asyncio
from freetempmail import FreeTempMail

if __name__ == '__main__':
    ftm = FreeTempMail()  # Instantiate class
    asyncio.run(ftm.generate_mail())  # Generate a temporary mail
    email = ftm.get_email()  # Fetch email info
    print(email)

    messages = ftm.get_messages()  # Fetch messages in mailbox
    print(messages)

    message_id = messages[0]['_id']  # Fetch a specific message by ID
    message_content = ftm.get_message(message_id)
    print(message_content)
```

<h4 align="center">Receive and Process a New Message</h4>

```python
import asyncio
from freetempmail import FreeTempMail

if __name__ == '__main__':
    ftm = FreeTempMail()  # Instantiate class
    asyncio.run(ftm.generate_mail())  # Generate a temporary mail
    email = ftm.get_email()  # Fetch email info
    print(email)

    new_message = ftm.wait_message()  # Wait and fetch a new message
    print(new_message)
```