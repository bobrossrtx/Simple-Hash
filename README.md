# Simple Hash

## <strong style="color: red;">Warning: I do not condone any illegal use using this tool. Any use of this tool shall be used under educational uses only or penetration testing.<br>Any Illegal use of this tool is the users responsibility and I do not account myself responsible!</strong>

## Hey there
This is a simple and self explanatory tool, but I"m gonna give brief explanation on it anyway!

When using this tool, at the moment there are 2 options,
- A dictionary attack
- Password encoding (Hashing)

## dictionary attack
When it comes to the dictionary attack, You can crack these types of hashes: 
```json
["MD5", "SHA1", "SHA224", "SHA384", "SHA256", "SHA512"]
```
As long as the password is in the word list you are using, you will be able to crack the hash as long as it fits within all of those hash types.
Here is an example of the process of cracking the a password.
```
$ python main.py

_____________________________________________________________
        |
  -dict   / -d  |  Initiate a dictionary attack on an any kind of hash
  -encode / -e  |  Encodes a password into an any kind of hash
        |
  All hashtypes supported:
  MD5, SHA1, SHA224, SHA384, SHA256, SHA512
-------------------------------------------------------------

[-dict]  [-encode]: -dict
Please enter the type of password hash <"MD5, SHA256" > >>> md5
Please enter your MD5 hash >>> 42d8aa7cde9c78c4757862d84620c335
Please enter your password list's name >>> passwords.json
enter your json object (eg. data | passwords) >>> passwords
md5(42d8aa7cde9c78c4757862d84620c335) | = | q1w2e3r4t5
```
As you can see the password is: q1w2e3r4t5
It is the last line you see here looking like:
> md5(42d8aa7cde9c78c4757862d84620c335) | = | q1w2e3r4t5
As you can see it is very easy to crack a password using this tool, You can even create or add to the password list in the pass_lists directory. There is also a simple Tutorial on how to create a list in that directory in the [README.MD](./pass_lists/README.MD).

## Password encoding (Hashing)
When it comes to encoding passwords, there are a lot of online tools to use for that like [CyberChef](https://gchq.github.io/CyberChef), But this is just a simple tool that can get it done quick just like there tools. When you want to convert a password, or matter of fact, any word on number or anything into a hash, you can do it. All it takes are 2 inputs:
- Enter what type of hash you want.
- Input what you want to be hashed
Here is an example of what you can do:
```
$ python main.py

_____________________________________________________________
        |
  -dict   / -d  |  Initiate a dictionary attack on an any kind of hash
  -encode / -e  |  Encodes a password into an any kind of hash
        |
  All hashtypes supported:
  MD5, SHA1, SHA224, SHA384, SHA256, SHA512
-------------------------------------------------------------

[-dict]  [-encode]: -encode
Please enter the type of password hash <"MD5, SHA256" > >>> sha1
Please enter a password to convert (SHA1) >>> NN2903n)**ksdf
password: SHA1(093fbc8d612ed5e9d3d7e35f15aef508ba33357d)
```
As you can see the password: NN2903n)**ksdf
Returned a hash of: 093fbc8d612ed5e9d3d7e35f15aef508ba33357d
It is that easy to encode what you want.
