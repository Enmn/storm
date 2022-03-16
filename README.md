<h1 align="center">Skiplier</h1>

It is a script that decodes any short link, even links that have ads and wait without knowing your IP address or even the browser or even the system. The truth information will be hidden that there are sites that reveal your IP address to those who made the short link. So I made it to avoid those scams they use to reveal some information from us too. I used Tor to implement this code. I wish you good luck

## Setup
You must first install the Tor server
```
sudo apt-get install tor
```
After Tor is installed you just have to do some configuration.
```
sudo nano /etc/proxychains4.conf
```
After that, copy everything that is in this link or file [proxychains4.conf](https://raw.githubusercontent.com/Enmn/Skiplier/main/src/proxychains4.txt) and paste it in `/etc/proxychains4.conf`</br>
After that, save the file, and you will be done with the Tor server


## Installation
```console
$ git clone https://github.com/Enmn/Skiplier

# Here you will enter the Skiplier folder
$ cd Skiplier

# Here I give all permissions to the files
$ chmod +x *

# Here, run the main file
$ python3 skiplier.py
```
## Screenshot
<img src="https://i.imgur.com/kPdLNyt.png" alt="screenshot" width="650" height="500">

## License
The source code for the site is licensed under the MIT license<br/>
Find a file called 'LICENSE'<br/>
Developr - [Emnm](https://github.com/Enmn)
