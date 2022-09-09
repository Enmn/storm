import json
import requests
import random
import os
import socket
import pycountry
from urllib.parse import urlparse
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from colorama import Fore, Style

# colors
boldgreen = "\033[1;32m"
cyan = "\033[0;36m"
boldblue = "\033[1;34m"
blue = "\033[0;34m"
white="\033[1;37m"
reset = "\033[0;0m"

session = requests.Session()
ua = UserAgent()
header = {'User-Agent': ua.random}
FliterWeb = random.choice(['unshorten.me'])
slink = input(boldblue + f'''
┌═══════════════════════════┐
█ {white}ENTER THE SHORT LINK HERE {boldblue}█
├═══════════════════════════┘
┃
└─═>>> ''' + cyan)
os.system("cls")
print(reset)
print(boldblue + "Just wait a few seconds . . .\n")

def ipinfo(ip):
    response = session.get('https://ipinfo.io/{}/json'.format(ip))
    data = response.json()
    return data


def unshorten():
    global uri
    if FliterWeb == 'unshorten.me':
        api_url = "https://unshorten.me/json/"
        url = api_url + slink
        response = session.get(url=url, headers=header).json()
        uri = response['resolved_url']


def info():
    file = open('blacklist.json', 'r').read()
    lists = json.loads(file)
    domain = uri.split("//")[-1].split("/")[0].split('?')[0]
    ip = socket.gethostbyname(domain)
    if domain in lists:
        st = Fore.RED + Style.BRIGHT + "Link you put can see the ip" + Fore.RESET + Style.NORMAL
    else:
        st = Fore.GREEN + Style.BRIGHT + "OK" + Fore.RESET + Style.NORMAL
    t = urlparse(uri).netloc
    d = '.'.join(t.split('.')[-2:])
    lib = str(d).upper()
    response = session.get('https://rdap.markmonitor.com/rdap/domain/' + lib)
    if response.status_code == 200:
        infoJson = response.json()
        expiration = infoJson['events'][0]['eventDate']
        updated = infoJson['events'][3]['eventDate']
        registration = infoJson['events'][1]['eventDate']
        organization = infoJson['entities'][1]['vcardArray'][1][1][3]
        location = ipinfo(ip)['loc']
        country = pycountry.countries.get(alpha_2=ipinfo(ip)['country'])
        city = ipinfo(ip)['city']
        name = infoJson['entities'][3]['vcardArray'][1][1][3]
        email = infoJson['entities'][3]['entities'][0]['vcardArray'][1][1][3]
        phone = infoJson['entities'][3]['entities'][0]['vcardArray'][1][2][3]
        timezone = ipinfo(ip)['timezone']
    if response.status_code == 404:
        expiration = Fore.YELLOW + Style.BRIGHT + '---' + Fore.RESET + Style.NORMAL
        updated = Fore.YELLOW + Style.BRIGHT + '---' + Fore.RESET + Style.NORMAL
        registration = Fore.YELLOW + Style.BRIGHT + '---' + Fore.RESET + Style.NORMAL
        organization = Fore.YELLOW + Style.BRIGHT + '---' + Fore.RESET + Style.NORMAL
        name = Fore.YELLOW + Style.BRIGHT + '---' + Fore.RESET + Style.NORMAL
        email = Fore.YELLOW + Style.BRIGHT + '---' + Fore.RESET + Style.NORMAL
        phone = Fore.YELLOW + Style.BRIGHT + '---' + Fore.RESET + Style.NORMAL
    print(boldblue + "Destination: " + cyan + uri)
    print(boldblue + "Expiration: " + cyan + expiration.split("T")[0])
    print(boldblue + "Updated: " + cyan + updated.split("T")[0])
    print(boldblue + "Registration: " + cyan + registration.split("T")[0])
    print(boldblue + "Organization: " + cyan + organization)
    print(boldblue + "Location: " + cyan + str(location))
    print(boldblue + "Country: " + cyan + country.name)
    print(boldblue + "City: " + cyan + city)
    print(boldblue + "Status: " + st)
    print(boldblue + "Owner: " + cyan + name)
    print(boldblue + "Email: " + cyan + email)
    print(boldblue + "Phonenumber: " + cyan + phone)
    print(boldblue + "Timezone: " + cyan + timezone)
    print(boldblue + "IP Address: " + cyan + ip + reset)
    input("\n" + boldblue + 'Press any key to continue . . .' + reset)


def run():
    unshorten()
    info()

if __name__ == '__main__':
    run()
