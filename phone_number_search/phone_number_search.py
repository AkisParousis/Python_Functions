def isPhoneNumber(text):
    if len(text) != 12:
        return False
    digit_pos = [0, 1, 2, 4, 5, 6, 8, 9, 10, 11]
    for i in digit_pos:
        if not text[i].isdecimal():
            return False
    if text[3] != '-' or text[7] != '-':
        return False
    return True


def text_part(text, i):
    part = text[i:i+12]
    return part

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'


for i in range(len(message)):
    part = text_part(message, i)
    if isPhoneNumber(part):
        print(f"{part} is a phone number")
