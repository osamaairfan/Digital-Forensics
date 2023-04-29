# DF Lab 04
Name: M. Osama Irfan

Roll No: 21k-4772

Section: BCY-4B
## Q1
The ip used by the attacker is: 
> **192.168.0.106** 

## Q2
Based on the modsec_audit.log file, Path Traversal Attack (/../) is being attempted. This type of attack is commonly used to exploit vulnerabilities that allow attackers to access files or directories that are outside of the web root directory of an application.

## Q3
The attacker is using:
> **Mozilla Firefox version 102.0 on a Linux x86_64 system**

## Q4
The attacker used **"SQLmap"** as an automated tool during the attack. SQLmap is a popular open-source tool used for detecting and exploiting SQL injection vulnerabilities in web applications.

## Q5
The attacker couldn't get access to **/etc/shadow** file. It is a crucial file that stores user password information in an encrypted format.

## Q6
The attacker managed to read the contents of the file **"important_note.txt"** using the command below:
> **cmd=cat+%2Fimportant_note.txt**

Also the attacker found a secret password from that file.

## Q7
The attacker was able to find a password from **"important_note.txt"** which is as below:
> **sup3r_s3cr3t_4nd_1mp0rt4nt_p4ssw0rd**

## Q8
The message itself is a string concatenated with a series of character codes that represent ASCII characters. When the character codes are converted to their corresponding characters, the message appeared in a base64 string. After decoding, a readable message with a flag was found as below:
> **Gentlemen, it is with great pleasure I inform you that:**
> **flag{h1pp1ty_h0pp1ty_y0ur_w3bs1t3_1s_n0w_my_pr0p3rty!}**

## Q9
Some of the indicators that comfirmed that the system has been compromised are: 
* The logs show that there was an unusual amount of network activity during the time of the attack.
 The attacker have left behind suspicious files or processes on the compromised system.
 The attacker may have conducted actions on the system that were outside of normal user behavior, such as accessing unusual files or systems or performing unauthorized commands.

My key takeaways from this attack scenario are:
> 1. Cyber attacks can come in many forms and can be difficult to detect.
> 2. Security best practices such as regular patching, network segmentation, and strong access controls can help prevent attacks.
> 3. Organizations should have a strong incident response plan in place to quickly identify and respond to security incidents.
> 4. Regular security training and awareness for employees can help them recognize and report suspicious activity.

## Q10
Based on the attack described, these can be some indicators of compromise that could be used to detect future attacks:
> 1. Unusual or suspicious network traffic
> 2. Existence of suspicious files or processes
> 3. Detection of known malware or attack tools
> 4. User behavior anomalies
