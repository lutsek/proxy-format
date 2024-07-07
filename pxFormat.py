import sys


file = ''
socks = ''
username = ''
password = ''
if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("Usage:\n pxFormat.py [pathToFile] [socksType] [userName] [passWord] \n Print any Key to exit...")
else:
    try:
        file = sys.argv[1]; 
        socks = (sys.argv[2]);
        username = (sys.argv[3] + " ");
        password = (sys.argv[4])
    except Exception:
        pass
    if len(file) <= 1:
        file = input("Input Path to file: ")
    if (len(socks)) <= 1:
        socks = input("Input Proxy Protocol:   ")
        socks = socks + " "
    if len(username) <= 1:
        oauth = input("Enter Username and Password. If no auth leave blank:  ")
    else:
        oauth = f" {username} {password}"
    
    with open(file, 'r') as fp:
        with open('output.txt', 'w') as dp:
            for x in fp:
                ips = x.split(':')
                ipsF = f"{socks} {ips[0]} {ips[1]} {oauth}\n"
                #print(ips)
                print(ipsF)
                dp.write(ipsF)

 
    print("saved as 'output.txt'. Proxy list now follows Proxychains4.conf format")
    input("Press any key to exit.. ")      