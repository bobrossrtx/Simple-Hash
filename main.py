import json
import hashlib


def brute_force():
    password_hi = input("Please enter your MD5 hash >>> ")
    pw_list = input("Please enter your password list's name >>> ")
    list_name = input("enter your json object (eg. data | passwords) >>> ")

    if '.json' not in pw_list:
        pw_list = f'{pw_list}.json'

    with open(f'word_list/{pw_list}') as passwords:
        password_load = json.load(passwords)

        for i in password_load[list_name]:
            password_b = bytes(i, "utf-8")
            password_hash = hashlib.md5(password_b)
            password_s = password_hash.hexdigest()

            password = i
            if password_hi in password_s:
                print(f'{password_hi} | = | {password}')


def encode():
    password = input("Please enter a password to convert (MD5) >>> ")

    password_b = bytes(password, "utf-8")
    password_hash = hashlib.md5(password_b)
    password_s = password_hash.hexdigest()

    print(f"password: {password_s}")


help_opt = '''
_____________________________________________________________
        |
  -brute  / -b	|  Initiate a brute force attack on an MD5 hash
  -encode / -e	|  encodes a password into an MD5 hash
        |
-------------------------------------------------------------
'''

print(help_opt)

option = input('[-brute]  [-encode]: ')

invalid = f'{option} is not a valid option.'


if option == '-brute' or option == '-b':
    brute_force()
elif option == '-encode' or option == '-e':
    encode()
else:
    print(invalid)
