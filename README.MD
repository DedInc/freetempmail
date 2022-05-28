

<h1 align="center">freetempmail - Temp-Mail.org API wrapper.</h1>
<h1 align="center"> -WARINING!!!- </h1>

```
You must have Google Chrome installed for token generation!
```

<h1 align="center"> -How to use?- </h1>

<h2 align="center"> -Quickstart- </h2>

```python
from freetempmail import as ft

if __name__ == '__main__':
	ft.generateMail() #you can use generateMail(chromeVersion), by default it detects it automatically Example: generateMail(101)
	email = ft.getEmail() #returns email
	print(email)
	messages = ft.getMessages() #get messages
	print(messages)
	message = messages[0]['_id'] #read a first message
	print(message)
```

<h2 align="center"> -Detect and get a new message- </h2>

```python
from freetempmail import as ft

if __name__ == '__main__':
	ft.generateMail()
	email = ft.getEmail() #returns email
	#This send message function or wait
	message = ft.waitMessage() #wait and get a new message
	print(message)
```