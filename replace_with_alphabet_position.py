def alphabet_position(text):
    res = [item for item in [ord(x)-96 if ord(x)-96 > 0 else ord(x) - 64 for x in text] if item > 0]
    res = str(res).replace(",","")
    res = str(res).replace("[","")
    res = str(res).replace("]","")
    return res
    pass
