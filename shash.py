#!/usr/bin/env python3

import json
import hashlib 
from itertools import product
import string
import os
import getpass
from colored import fg, bg, attr

# import sys        Maybe
# import argparse   Maybe

error = fg(9)
reset = attr(0)
bold = attr(1)

# Text
lime = fg(10)
gold_rod = fg(136)
dark_green = fg(22)

# BG
lime_bg = bg(10)
gold_rod_bg = bg(136)
dark_green_bg = fg(22)


def dict_attack():
    type_att = input("Please enter the type of password hash <\"MD5, SHA256\"> >>> ")
    type_att = type_att.upper()
    aloud_pass_types = ['MD5', 'SHA1', 'SHA224', 'SHA384', 'SHA256', 'SHA512']

    if type_att not in aloud_pass_types:
        print(f'''\n You can only use these hashes:
{aloud_pass_types}''')
        return

    password_hi = input(f"Please enter your {type_att} hash >>> ")
    pw_list = input("Please enter your password list's name >>> ")
    list_name = input("enter your json object (eg. data | passwords) >>> ")


    def hash(type_att):
        password_b = bytes(i, "utf-8")

        if type_att.lower() == 'md5':
            password_hash = hashlib.md5(password_b)
        elif type_att.lower() == 'sha256':
            password_hash = hashlib.sha256(password_b)
        elif type_att.lower() == 'sha224':
            password_hash = hashlib.sha224(password_b)
        elif type_att.lower() == 'sha384':
            password_hash = hashlib.sha384(password_b)
        elif type_att.lower() == 'sha512':
            password_hash = hashlib.sha512(password_b)
        elif type_att.lower() == 'sha1':
            password_hash = hashlib.sha1(password_b)

        password_s = password_hash.hexdigest()

        password = i
        pass_type = type_att

        if password_hi in password_s:
            print(f'''
Password:
{gold_rod_bg}{pass_type}{reset}({password_hi}) | = | {lime}{bold}{password}{reset}''' + reset)
            return True
        else:
            return False

    if '.json' not in pw_list:
        pw_list = f'{pw_list}.json'

    kali_parrot = f'/usr/share/wordlists/simple-hash/{pw_list}'

    win_usr = getpass.getuser()
    windows = f'C:/Users/{win_usr}/.simple-hash/{pw_list}'

    if os.path.exists(kali_parrot):
        with open(kali_parrot) as passwords:
            password_load = json.load(passwords)

            for i in password_load[list_name]:
                type_att = type_att.lower()

                if hash(type_att):
                    return

            print('\nPassword was not found')
            return

    elif os.path.exists(windows):
        with open(windows) as passwords:
            password_load = json.load(passwords)

            for i in password_load[list_name]:
                type_att = type_att.lower()

                if hash(type_att):
                    return

            print('\nPassword was not found')
    else:
        print(error+ '\r\nE: Cannot find wordlist or directory!' + reset)
        return


#######################################
#                WIP                  #
#######################################

# def wordlist_gen():
#     min_len = int(input("Enter min length >>> "))
#     max_len = int(input("Enter max length >>> "))
#     counter = 0
#     characters = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
#     wordlist_file = input("Please enter a path and file name to write your wordlist")

#     file_open = open(wordlist_file, 'w')

#     for i in range(min_len, max_len+1):
#         for j in product(characters, repeat=1):
#             word = "".join(j)
#             file_open.write(word)
#             file_open.write('\n')
#             counter += 1
#     print(f'Wordlist of {counter} passwords created at {os.path.abspath(wordlist_file)}')


def hash_tool():
    type_en = input("Please enter the type of password hash <\"MD5, SHA256\"> >>> ")
    type_en = type_en.upper()
    aloud_pass_types = ['MD5', 'SHA1', 'SHA224', 'SHA384', 'SHA256', 'SHA512']

    if type_en not in aloud_pass_types:
        print(f'''\n You can only use these hashes:
{aloud_pass_types}''')
        return

    password = input(f"Please enter a password to convert ({type_en}) >>> ")

    password_b = bytes(password, "utf-8")

    if type_en.lower() == 'md5':
        password_hash = hashlib.md5(password_b)
    elif type_en.lower() == 'sha256':
        password_hash = hashlib.sha256(password_b)
    elif type_en.lower() == 'sha224':
        password_hash = hashlib.sha224(password_b)
    elif type_en.lower() == 'sha384':
        password_hash = hashlib.sha384(password_b)
    elif type_en.lower() == 'sha512':
        password_hash = hashlib.sha512(password_b)
    elif type_en.lower() == 'sha1':
        password_hash = hashlib.sha1(password_b)

    password_s = password_hash.hexdigest()
    print(f"password: {type_en}({password_s})")


ascii_art = '''
  /$$$$$$  /$$                         /$$                 /$$   /$$                     /$$      
 /$$__  $$|__/                        | $$                | $$  | $$                    | $$      
| $$  \__/ /$$ /$$$$$$/$$$$   /$$$$$$ | $$  /$$$$$$       | $$  | $$  /$$$$$$   /$$$$$$$| $$$$$$$ 
|  $$$$$$ | $$| $$_  $$_  $$ /$$__  $$| $$ /$$__  $$      | $$$$$$$$ |____  $$ /$$_____/| $$__  $$
 \____  $$| $$| $$ \ $$ \ $$| $$  \ $$| $$| $$$$$$$$      | $$__  $$  /$$$$$$$|  $$$$$$ | $$  \ $$
 /$$  \ $$| $$| $$ | $$ | $$| $$  | $$| $$| $$_____/      | $$  | $$ /$$__  $$ \____  $$| $$  | $$
|  $$$$$$/| $$| $$ | $$ | $$| $$$$$$$/| $$|  $$$$$$$      | $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$
 \______/ |__/|__/ |__/ |__/| $$____/ |__/ \_______/      |__/  |__/ \_______/|_______/ |__/  |__/
                            | $$                                                                  
                            | $$                                                                  
                            |__/                                                                  
'''


help_opt = f'''
_____________________________________________________________
        |
    -dict         / -d    |   Initiate a dictionary attack on an any kind of hash
    -hash         / -h	  |   hashes a password into an any kind of hash
    -wordlist     / -w    |   Creates a wordlist (WIP)
        |
  Supported HashTypes:
  MD5, SHA1, SHA224, SHA384, SHA256, SHA512
-------------------------------------------------------------
'''

if __name__ == '__main__':
    print(ascii_art)
    print(help_opt)

    option = input('[-dict]  [-hash]: ')

    invalid = f'{option} is not a valid option.'


    if option == '-dict' or option == '-d':
        dict_attack()
    elif option == '-hash' or option == '-h':
        hash_tool()
    elif option == '-wordlist' or option == '-w':
        wordlist_gen()
    else:
        print(invalid)

    exit_prog = input("Press any enter to exit... ")
    if exit_prog:
        exit()
