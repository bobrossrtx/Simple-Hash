import json
import hashlib


def dict_attack():
    type_att = input("Please enter the type of password hash <\"MD5, SHA256\" > >>>")
    type_att = type_att.upper()
    aloud_pass_types = ['MD5', 'SHA1', 'SHA224', 'SHA384', 'SHA256', 'SHA512']

    if type_att not in aloud_pass_types:
        exit(f'''\n You can only use these hashes:
{aloud_pass_types}''')

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
            password_hash = hashlib.sha244(password_b)
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
            print(f'{pass_type}({password_hi}) | = | {password}')

    if '.json' not in pw_list:
        pw_list = f'{pw_list}.json'

    with open(f'pass_lists/{pw_list}') as passwords:
        password_load = json.load(passwords)

        for i in password_load[list_name]:
            type_att = type_att.lower()

            hash(type_att)


def encode():
    type_en = input("Please enter the type of password hash <\"MD5, SHA256\" > >>>")
    type_en = type_en.upper()

    password = input(f"Please enter a password to convert ({type_en}) >>> ")

    password_b = bytes(password, "utf-8")

    if type_en.lower() == 'md5':
        password_hash = hashlib.md5(password_b)
    elif type_en.lower() == 'sha256':
        password_hash = hashlib.sha256(password_b)
    elif type_en.lower() == 'sha224':
        password_hash = hashlib.sha244(password_b)
    elif type_en.lower() == 'sha384':
        password_hash = hashlib.sha384(password_b)
    elif type_en.lower() == 'sha512':
        password_hash = hashlib.sha512(password_b)
    elif type_en.lower() == 'sha1':
        password_hash = hashlib.sha1(password_b)

    password_s = password_hash.hexdigest()
    print(f"password: {type_en}({password_s})")


help_opt = f'''
_____________________________________________________________
        |
  -dict  / -d	|  Initiate a dictionary force attack on an any kind of hash
  -encode / -e	|  Encodes a password into an any kind of hash
        |
  All hashtypes supported:
  MD5, SHA1, SHA224, SHA384, SHA256, SHA512
-------------------------------------------------------------
'''

print(help_opt)

option = input('[-dict]  [-encode]: ')

invalid = f'{option} is not a valid option.'


if option == '-dict' or option == '-d':
    dict_attack()
elif option == '-encode' or option == '-e':
    encode()
else:
    print(invalid)
