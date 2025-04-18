def main(): 
    number = isPhoneNumber(input('Enter a US phone number: '))
    print(f"{number}")


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        if text[7] != '-':
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

main()
