import random
import time
import os
import shutil
import re
from urllib.parse import unquote
import platform
from base64 import b64decode
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip3 install requests')
    os.system('pip3 install bs4')



def isAndroid() -> bool: 
    for item in list(os.environ.keys()): 
        if "ANDROID" in item.upper(): 
            return True
        else:
            return False 



def installTor():
    if shutil.which('tor'):
        if isAndroid == False:
            os.system('sudo service tor start')
        if isAndroid == True:
            os.system('tor')
        pass
    else:
        if isAndroid() == False:
            os.system('clear')
            print("Oh I'm so sorry you don't have Tor !")
            time.sleep(1)
            print("But don't worry Skiplier will install Tor and setup it")
            time.sleep(2)
            print('\tInstalling a Tor...')
            os.system('sudo apt-get install tor')
            print('Tor is installed')
            time.sleep(2)
            print('Everything is being prepared...')
            time.sleep(3)
            res = requests.get('https://raw.githubusercontent.com/Enmn/Skiplier/main/src/proxychains4.txt')
            with open('/etc/proxychains4.conf', 'wb') as f:
                for data in res.iter_content(chunk_size=8192):
                    f.write(data)
            print('Everything has been successfully completed, you can now run Skiplier again')
            os.system('sudo service tor start')
            pass
        if isAndroid() == True:
            os.system('clear')
            print("Oh I'm so sorry you don't have Tor !")
            time.sleep(1)
            print("But don't worry Skiplier will install Tor and setup it")
            time.sleep(2)
            print('\tInstalling a Tor...')
            os.system('pkg install tor')
            print('Tor is installed')
            time.sleep(2)
            print('Everything is being prepared...')
            time.sleep(3)
            res = requests.get('https://raw.githubusercontent.com/Enmn/Skiplier/main/src/proxychains4.txt')
            with open('/etc/proxychains4.conf', 'wb') as f:
                for data in res.iter_content(chunk_size=8192):
                    f.write(data)
            print('Everything has been successfully completed, you can now run Skiplier again')
            os.system('tor')
            pass
installTor()



def headers():
    useragent_list = [
        "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101"\
        "Firefox/41.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)"\
        "AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2"\
        "Safari/601.3.9",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)"\
        "Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"\
        "(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"\
        "Edge/12.246"\
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1"\
        "Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11"\
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/604.1"
        ]
    randuser = random.choice(useragent_list)
    return randuser



def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
    return session



useragent = headers()
os.system("clear")
session = get_tor_session()

# colors
boldgreen = "\033[1;32m"
cyan = "\033[0;36m"
boldblue = "\033[1;34m"
blue = "\033[0;34m"
blanco="\033[1;37m"
reset = "\033[0;0m"



print(boldblue + '''
       ________  __   ___   __       _______   ___        __     _______    _______ 
      /"       )|/"| /  ") |" \     |   __ "\ |"  |      |" \   /"     "|  /"      \ 
     (:   \___/ (: |/   /  ||  |    (. |__) :)||  |      ||  | (: ______) |:        | 
      \___  \   |    __/   |:  |    |:  ____/ |:  |      |:  |  \/    |   |_____/   ) 
       __/  \\\  (// _  \   |.  |    (|  /      \  |___   |.  |  // ___)_  //      / 
      /" \   :) |: | \  \  /\  |\  /|__/ \    ( \_|:  \  /\  |\(:      "| |:  __   \ 
     (_______/  (__|  \__)(__\_|_)(_______)    \_______)(__\_|_)\_______) |__|  \___)


               ┌══════════════════════════════════════════════════┐
               █        THANK YOU FOR INSTALLING SKIPLIER         █
               █        WE HOPE YOU HAVE A GOOD EXPERIENCE        █
               █    AND DON'T FORGET TO GIVE US A STAR ON GITHUB! █
               └══════════════════════════════════════════════════┘
''')
url = input(boldblue + f'''
┌──[{blanco + 'ENTER THE SHORT LINK' + boldblue}]
└─>>> ''' + cyan)
domain = url.split("//")[-1].split("/")[0].split('?')[0]



if domain == 'favoacew.com' or domain == 'fumacrom.com':
    response = session.get(url, headers={'user-agent': useragent})
    ysmm = re.findall(r'var ysmm =.*\;?', response.text)
    ysmm = re.sub(r'var ysmm \= \'|\'\;', '', ysmm[0])
    left = ''
    right = ''
    for c in [ysmm[i:i+2] for i in range(0, len(ysmm), 2)]:
        left += c[0]
        right = c[1] + right
    encoded_uri = list(left + right)
    numbers = ((i, n) for i, n in enumerate(encoded_uri) if str.isdigit(n))
    for first, second in zip(numbers, numbers):
        xor = int(first[1]) ^ int(second[1])
        if xor < 10:
            encoded_uri[first[0]] = str(xor)    
    uri = b64decode("".join(encoded_uri).encode())[16:-16].decode()
    os.system('sudo service tor stop')
    print(reset + '\n' + unquote(uri.split('=')[6]))
    exit()



if domain == 'cutt.us' or domain == 'soo.gd':
    response = session.get(url, headers={'user-agent': useragent})
    soup = BeautifulSoup(response.text, "lxml")
    uri = soup.find('a', attrs={'rel':'nofollow'})['href']
    os.system('sudo service tor stop')
    print(reset + '\n' + uri)
    exit()



else:
    response = session.head(url, headers={'user-agent': useragent})
    if response.headers['Location']:
        long = response.headers['Location']
        os.system('sudo service tor stop')
        print(reset + '\n' + long)
        exit()
