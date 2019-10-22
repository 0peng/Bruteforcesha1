#!usr/bin/env python

from urllib.request import urlopen, hashlib

sha1hash = input("WelCome InPUT THE HASH To Crack.\n>")

LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
    if hashedGuess == sha1hash:
        print("The PassWord is", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print ("PassWord guess ",str(guess)," does not match, trying next..")
print("PassWord not in database, we'll get them next time")
