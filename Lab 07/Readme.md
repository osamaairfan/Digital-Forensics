# DF Lab 07
Name: M. Osama Irfan

Roll No: 21k-4772

Section: BCY-4B

## task1:

Found the flag by taking the hex values assigned to the data types by converting them using Swap endianness with word length 8 and hexadecimal values to their ASCII representation.
> **"flag{s0m3_susp1c10us_str1ng}"**


## task2:
Firstly I converted the hex values given in the code (if statements) to decimal and then executing the code using ltrace command. After inputting the decimal values as the magic numbers, the flag would be found.
> **"flag{sup3r_s1mpl3_x0r}"**

![image](https://github.com/osamaairfan/Digital-Forensics/assets/115397536/88950c59-da05-45bc-8216-4d7f25c0e8aa)



## task3:
I changed the dword [var_bch] hex value to the ones currently available in the main function and then executed the code by ltrace command. In this way the flag was found.
> **"flag{r3v3rs2_2ng0n22r0ng_0z0}"**

![image](https://github.com/osamaairfan/Digital-Forensics/assets/115397536/d7a24179-960c-48ec-994d-9aa65584ff51)
