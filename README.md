<h3 style="" align="center">Storm</h3>
<p align="center">
  <a href="#setup">Setup</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#requirements">Requirements</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
</p>
<p>It is a script that decodes any short link, even links that have ads and wait without knowing your IP address or even the browser or even the system. The truth information will be hidden that there are sites that reveal your IP address to those who made the short link. So I made it to avoid those scams they use to reveal some information from us too. I used Tor to implement this code. I wish you good luck
</p>

## Setup

You must first install the Tor server
```console
$ sudo apt-get install tor
```
After Tor is installed you just have to do some configuration.
```console
$ sudo nano /etc/proxychains4.conf
```
After that, copy everything that is in this link or file [proxychains4.conf](https://raw.githubusercontent.com/Enmn/Storm/main/src/proxychains4.txt) and paste it in `/etc/proxychains4.conf`</br>
After that, save the file, and you will be done with the Tor server</br>

Now install Git to be able to install Storm
```console
$ sudo apt-get install git
```
## Requirements
<p>1. you must have a Linux or even a Linux subfolder<br>2. you must have Python<br>3. You must install the libraries in the file <code>requirements.txt</code></p>

## Installation
```console
# Here, type this command to install
$ git clone https://github.com/Enmn/storm

# Here you will enter the Storm folder
$ cd storm

# Here, run the main file
$ python3 storm.py
```
## Usage
Simply dear user, put the short link and then enter yes or no if you want to save the results in a file, i think it's clear isn't it?

## Error
Dear, you may encounter errors or problems in your use of the performance, for example, some of the sites the tool cannot give you the real link (403) and the reason is due to the Tor proxy, which or the site refuses Tor proxy requests, it is good luck that there are sites that accept requests from Tor proxies and this is something good

## Preview
<img src="./assets/TAQhcob.png" alt="Interface">

## License
The source code for the site is licensed under the MIT license<br/>
Find a file called 'LICENSE'<br/>
Developr - [Emnm](https://github.com/Enmn)
