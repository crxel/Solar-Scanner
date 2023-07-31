
import subprocess
import fade
import requests
import time
import threading
from mcstatus import JavaServer
import re
import shutil
import os
import platform
from colorama import Fore

red = Fore.RED
os.system('cls')

logo = """                                                          
   SSSSSSSSSSSSSSS                  lllllll                                      
 SS:::::::::::::::S                 l:::::l                                      
S:::::SSSSSS::::::S                 l:::::l                                      
S:::::S     SSSSSSS                 l:::::l                                      
S:::::S               ooooooooooo    l::::l   aaaaaaaaaaaaa  rrrrr   rrrrrrrrr   
S:::::S             oo:::::::::::oo  l::::l   a::::::::::::a r::::rrr:::::::::r  
 S::::SSSS         o:::::::::::::::o l::::l   aaaaaaaaa:::::ar:::::::::::::::::r 
  SS::::::SSSSS    o:::::ooooo:::::o l::::l            a::::arr::::::rrrrr::::::r
    SSS::::::::SS  o::::o     o::::o l::::l     aaaaaaa:::::a r:::::r     r:::::r
       SSSSSS::::S o::::o     o::::o l::::l   aa::::::::::::a r:::::r     rrrrrrr
            S:::::So::::o     o::::o l::::l  a::::aaaa::::::a r:::::r            
            S:::::So::::o     o::::o l::::l a::::a    a:::::a r:::::r            
SSSSSSS     S:::::So:::::ooooo:::::ol::::::la::::a    a:::::a r:::::r            
S::::::SSSSSS:::::So:::::::::::::::ol::::::la:::::aaaa::::::a r:::::r            
S:::::::::::::::SS  oo:::::::::::oo l::::::l a::::::::::aa:::ar:::::r         
 SSSSSSSSSSSSSSS      ooooooooooo   llllllll  aaaaaaaaaa  aaaarrrrrrr                                                              
"""
print(fade.pinkred(logo))
print(fade.pinkred('[*] Cleaning solarlogs.solar'))
with open('./solarlogs.solar', 'w', encoding='utf-8') as e:
        e.write(logo)

shutil.rmtree('./outputs', ignore_errors=True)
print(fade.pinkred('[*] Starting Scan'))
time.sleep(2)

lock = threading.Lock()
if platform.system() == "Windows":
 def main():
    while True:
          try:
            url = "https://minecraft-mp.com/servers/random/"
            r = requests.get(url)
            ips = re.findall(r'<strong>(.*?)</strong></button>', r.text)
            for ip in ips:
                    try:
                        res = re.sub(r':([^:]+)$',"",ip)
                        result = subprocess.run(f'ping -n 1 {res}', capture_output=True, text=True)
                        
                        # get numeric ip
                        output = result.stdout
                        pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
                        r = re.findall(pattern, output)
                        r = str(list(set(r))).replace('[', '').replace(']', '').replace('\'', '')
                        if r == '' or r == ' ':
                            pass
                        else:
                             print(fade.greenblue(f'[+] Starting scan on: {r}'))

                        # check if server valid
                        if output != f'Ping request could not find host {result} Please check the name and try again.':
                            if r != '':
                                try:
                                        
                                        cmd = f'java -Dfile.encoding=UTF-8 -jar qubo.jar -port 25500-35590 -th 100 -ti 500 -c 1 -noping -range {r}'
                                        subprocess.run(cmd, shell=True, capture_output=True, text=True)
                                        with open(f'./outputs/{r}-{r}.txt', 'r', encoding='utf-8') as i:
                                          i = i.read()
                                          i = str(i).replace('quboScanner by @zreply - Version 0.3.5 ', '').replace('Json not readable', '').replace('-', '').replace('Scanner started on', 'Time')
                                          i = i.strip('')

                                          if r not in i.lower():
                                               print(f'\n{red}[-] Deleted {r}! No ports found.\n')
                                          
                                          elif 'error' in i.lower():
                                               print(f'\n{red}[-] Deleted {r}! Protected Server.\n')
                                          
                                          elif 'tcpshield' in i.lower():
                                               print(f'\n{red}[-] Deleted {r}! TCPShield Server.\n.')
                                          
                                          elif 'invalid' in i.lower():
                                               print(f'\n{red}[-] Deleted {r}! Invalid Server.\n')
                                          
                                          elif 'ddos' in i.lower():
                                              print(f'\n{red}[-] Deleted {r}! DDoS Protected Server.\n')
                                          
                                          elif 'velocity' in i.lower():
                                              print(f'\n{red}[-] Deleted {r}! Velocity Server.\n')
                                          
                                          elif 'fml' in i.lower():
                                              print(f'\n{red}[-] Deleted {r}! FML Server.\n')
                                          
                                          elif 'mod' in i.lower():
                                             print(f'\n{red}[-] Deleted {r}! Modded Server.\n')
                                          
                                          elif 'forge' in i.lower():
                                             print(f'\n{red}[-] Deleted {r}! Forge Server.\n')

                                          elif 'guard' in i.lower():
                                             print(f'\n{red}[-] Deleted {r}! Guarded Server.\n')   
                                          
                                          else:
                                           print(fade.greenblue(f'[+] Found Server! IP: {r}'))
                                           print(fade.pinkred(i))
                                           with open('./solarlogs.solar', 'a', encoding='utf-8') as e:
                                                 e.write(f'\n====================================================================================\nSolar Info {i}')
                                    
                                except Exception:
                                    pass

                            elif r == '':
                                pass

                    except Exception:
                        pass

          except Exception:
              pass

 threads = []
 for i in range(10):
    try:
     t = threading.Thread(target=main)
     t.start()
     threads.append(t)
     print(fade.greenblue(f'[+] Started thread! ID: {t}'))
    except Exception:
        pass
    
elif platform.system() == 'Linux':
    print('Solar is not yet supported for linux.')
    time.sleep(10)
    quit()