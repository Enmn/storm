import random
import time
import os
import shutil
import json
import socket
import re
from urllib.parse import unquote
from base64 import b64decode
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip3 install requests')
    os.system('pip3 install bs4')



def installTor():
    if shutil.which('tor'):
        os.system('sudo service tor start')
        pass
    else:
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
installTor()



def output_file(i):
    with open('output_extras.json', 'w') as file:
        file.write(i)



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
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        ]
    randuser = random.choice(useragent_list)
    return randuser



def get_tor_session():
    useragent = headers()
    session = requests.Session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
    session.headers = {'user-agent': useragent}
    return session



os.system("clear")
session = get_tor_session()



def DecodeURL(url):
    global json_data
    info = session.get(url)
    hostname = url.split("//")[-1].split("/")[0].split('?')[0]
    ip = socket.gethostbyname(hostname)
    dev_info = json.loads(session.get('https://ipinfo.io/' + ip + '/json').text)
    data = {}
    # title
    soup = BeautifulSoup(info.text, "lxml")
    data['Title'] = soup.title.string
    # destination
    data['Destination'] = url
    # domain
    data['Domain'] = hostname
    # status
    data['Status'] = str(info.status_code) + ' ' + str(info.reason)
    # onlone
    data['Online'] = str(info.ok).lower()
    # ip
    ip = socket.gethostbyname(hostname)
    data['IP'] = ip
    # dev
    try:
        data['City'] = dev_info['city']
        data['Region'] = dev_info['region']
        data['Country'] = dev_info['country']
        data['Loc'] = dev_info['loc']
        data['Org'] = dev_info['org']
        data['Postal'] = dev_info['postal']
        data['Timezone'] = dev_info['timezone']
        data['Filesave'] = 'true'
    except KeyError:
        pass
    json_data = json.dumps(data)
    return json_data



def EncodeURL(url):
    global json_datae
    hostname = url.split("//")[-1].split("/")[0].split('?')[0]
    if hostname == 'favoacew.com' or domain == 'fumacrom.com' or domain == 'barsoocm.com':
        hostname = 'adf.ly'
    info = session.get('https://' + hostname)
    ip = socket.gethostbyname(hostname)
    dev_info = json.loads(session.get('https://ipinfo.io/' + ip + '/json').text)
    data = {}
    data['Website'] = 'https://' + hostname
    # domain
    data['Domain'] = hostname
    # status
    data['Status'] = str(info.status_code) + ' ' + str(info.reason)
    # onlone
    data['Online'] = str(info.ok).lower()
    # ip
    ip = socket.gethostbyname(hostname)
    data['IP'] = ip
    # dev
    try:
        data['City'] = dev_info['city']
        data['Region'] = dev_info['region']
        data['Country'] = dev_info['country']
        data['Loc'] = dev_info['loc']
        data['Org'] = dev_info['org']
        data['Postal'] = dev_info['postal']
        data['Timezone'] = dev_info['timezone']
        data['Filesave'] = 'false'
    except KeyError:
        pass
    json_datae = json.dumps(data)
    return json_datae



def for_loop():
    print(boldblue + f"[ {reset + '*' + boldblue} ] {cyan + 'Here You Will See the Information of the Site That Was Decoded'}")
    for key in json.loads(json_data):
        print(boldblue + '      ' + key + ": " + cyan + json.loads(json_data)[key])
    print(boldblue + f"[ {reset + '*' + boldblue} ] {cyan + 'Here You Will See Information About the Short Site'}")
    for key in json.loads(json_datae):
        print(boldblue + '      ' + key + ": " + cyan + json.loads(json_datae)[key])



# colors
boldgreen = "\033[1;32m"
cyan = "\033[0;36m"
boldblue = "\033[1;34m"
blue = "\033[0;34m"
white="\033[1;37m"
reset = "\033[0;0m"



print(boldblue + '''
       ________  __   ___   __       _______   ___        __     _______    _______ 
      /"       )|/"| /  ") |" \     |   __ "\ |"  |      |" \   /"     "|  /"      \ 
     (:   \___/ (: |/   /  ||  |    (. |__) :)||  |      ||  | (: ______) |:        | 
      \___  \   |    __/   |:  |    |:  ____/ |:  |      |:  |  \/    |   |_____/   ) 
       __/  \\\  (// _  \   |.  |    (|  /      \  |___   |.  |  // ___)_  //      / 
      /" \   :) |: | \  \  /\  |\  /|__/ \    ( \_|:  \  /\  |\(:      "| |:  __   \ 
     (_______/  (__|  \__)(__\_|_)(_______)    \_______)(__\_|_)\_______) |__|  \___)

               
                            THANK YOU FOR INSTALLING SKIPLIER         
                            WE HOPE YOU HAVE A GOOD EXPERIENCE        
                      AND DON'T FORGET TO GIVE US A STAR ON GITHUB! 
''')
url = input(boldblue + f'''
┌═══════════════════════════┐
█ {white}ENTER THE SHORT LINK HERE {boldblue}█
├═══════════════════════════┘
┃
└─═>>> ''' + cyan)
domain = url.split("//")[-1].split("/")[0].split('?')[0]
EncodeURL(url)


if domain == 'favoacew.com' or domain == 'fumacrom.com' or domain == 'barsoocm.com':
    response = session.get(url)
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
    output_file(DecodeURL(unquote(uri.split('=')[6])))
    os.system('sudo service tor stop')
    os.system('clear')
    for_loop()
    exit()



if domain == 'cutt.us' or domain == 'soo.gd':
    response = session.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    uri = soup.find('a', attrs={'rel':'nofollow'})['href']
    output_file(DecodeURL(uri))
    os.system('sudo service tor stop')
    os.system('clear')
    for_loop()
    exit()



if domain == 'tiny.cc':
    protocol = url.split(':')[-0]
    if protocol == 'http':
        link = url.split(':')[1]
        url = protocol + 's' + ':' + link
    elif protocol == 'https':
        url = url
    elif protocol != 'http' or protocol != 'https':
        url = 'https://' + url
    response = session.head(url)
    if response.headers['Location']:
        uri = response.headers['Location']
        output_file(DecodeURL(uri))
        os.system('sudo service tor stop')
        os.system('clear')
        for_loop()
        exit()



if domain == 'trimurl.co':
    response = session.get(url)
    uri = response.url
    print(reset + '\n' + uri)
    output_file(DecodeURL(uri))
    os.system('sudo service tor stop')
    os.system('clear')
    for_loop()
    exit()



if domain == 'chilp.it':
    link = url.split('://')[1]
    protocol = url.split(':')[-0]
    if protocol == 'https':
        protocol2 = protocol.replace('s','')
        url = protocol2 + '://' + link
    elif protocol == 'http':
        url = url
    response = session.head(url)
    if response.headers['Location']:
        uri = response.headers['Location']
        output_file(DecodeURL(uri))
        os.system('sudo service tor stop')
        os.system('clear')
        for_loop()
        exit()



else:
    response = session.head(url)
    if response.headers['Location']:
        long = response.headers['Location']
        output_file(DecodeURL(long))
        os.system('sudo service tor stop')
        os.system('clear')
        for_loop()
        exit()
