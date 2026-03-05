import os
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] JOIN WHATSAPP GROUP')
os.system('xdg-open https://chat.whatsapp.com/BmxmNHAMjLj5i59vqB2uKw')
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    os.system('chmod 777 random64;./random64')
else:
    exit('\033[91;1m [•] SORRY YOU DEVICE NOT SUPPORT')