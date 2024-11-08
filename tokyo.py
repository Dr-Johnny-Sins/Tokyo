import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/BmxmNHAMjLj5i59vqB2uKw')
djs=platform.architecture()[0]
if djs=="32bit":
    __import__("tokyo32")
elif djs=="64bit":
    __import__("tokyo64")
