# DF Lab 08
Name: M. Osama Irfan

Roll No: 21k-4772

Section: BCY-4B

### For the learning purpose:

Here are some commonly used characters for creating masks in Hashcat:

    ?l: This represents a lowercase letter (a-z).
    ?u: This represents an uppercase letter (A-Z).
    ?d: This represents a digit (0-9).
    ?s: This represents a special character, such as !, @, or #.
    ?a: This represents any character (lowercase letter, uppercase letter, digit, or special character).

Here are some examples of how to use masks in Hashcat:

    ?l?l?l: This mask will generate all possible combinations of three lowercase letters.
    ?u?l?d?d: This mask will generate all possible combinations of an uppercase letter, a lowercase letter, and two digits.
    ?l?l?l?l?d?d: This mask will generate all possible combinations of four lowercase letters followed by two digits.


## Q1
![Screenshot from 2023-05-14 05-00-27](https://github.com/osamaairfan/Digital-Forensics/assets/115397536/1d7395ff-20e3-45e7-99bf-5dea7de76bce)
By using hashcat -m 0 -a 3 48bb6e862e54f2a795ffc4e541caed4d ?l?l?l?l

> 48bb6e862e54f2a795ffc4e541caed4d:easy 

## Q2
'By using' └─$ john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha512 hash.txt'
