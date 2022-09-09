import os
from pystyle import *

os.system("cls")

def logo():
    print(Center.XCenter("\033[1;34m" + f'''
            ___                                          
           (   )                                         
  .--.      | |_       .--.    ___ .-.      ___ .-. .-.   
 /  _  \   (   __)    /    \  (   )   \   (   )   '   \  
. .' `. ;   | |      |  .-. ;  | ' .-. ;  |  .-.  .-. ; 
| '   | |   | | ___  | |  | |  |  / (___) | |  | |  | | 
_\_`.(___)  | |(   ) | |  | |  | |        | |  | |  | | 
(   ). '.   | | | |  | |  | |  | |        | |  | |  | | 
| |  `\ |   | ' | |  | '  | |  | |        | |  | |  | | 
; '._,' '   ' `-' ;  '  `-' /  | |        | |  | |  | | 
 '.___.'     `.__.    `.__.'  (___)      (___)(___)(___)


           THANK YOU FOR INSTALLING STORM         
         WE HOPE YOU HAVE A GOOD EXPERIENCE        
    AND DON'T FORGET TO GIVE US A STAR ON GITHUB!  
    '''))

if __name__ == "__main__":
    logo()
    from track import run
    run()
