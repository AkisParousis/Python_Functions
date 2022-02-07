import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

while True:
    mo = phoneNumRegex.search(message)
    if mo == None:
        break
    message = message[mo.end():]
    print("Phone number found: " + mo.group())
