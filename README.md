# Simple-Hash - C++ (wip)
___
 Work in progress

## How to use:
When cracking a hash, at the moment it only supports "md5" hashes, but more options are comming in the future;
But to crack a hash, all it takes is 1 small little command.
```bash
./shash -wL <password list> -m <hash type (only md5)> -h <hash>
```
Heres an example one:
```bash
./shash -wL passwords.txt -m md5 -h a17a41337551d6542fd005e18b43afd4
```
Try it for yourself and see what you get
