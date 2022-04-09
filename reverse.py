# i used this modules if u got better ones please add :p
#telegram me : https://t.me/kickflap
from importlib.resources import contents
import os
import sys
import json
import random
import requests
import platform
import threading

#ca depends la version de python  ////// if its 2 then importing from Queue otherwise from queue
py_version = platform.python_version()
if int(py_version[0]) == 2:
   from Queue import Queue
if int(py_version[0]) == 3:
   from queue import Queue



#clearing the interpreter in both systems Linux and WINDOWS
if sys.platform == 'win32':
   os.system('cls')
else:
   os.system('clear')

#  takhreb nikek barkana


class Reverse_Ip:
   def __init__(self):
      self.url = 'https://sonar.omnisint.io/reverse/'
      self.banner()
      self.save = 'hrackedz.txt'
   def reverse(self, domain):
        try:
            req = requests.get(self.url+domain)
            
            if req.status_code == 200:
                
                
                bb = requests.get(self.url+domain).text
                
                print (f"{domain} >> ({len(bb)} domains)")
                res = req.json()
                if res:
                    domains = '\n'.join(res)
                    open(self.save, 'a').write(domains+'\n')
        except Exception as v:
            print(v)
   def start(self, q):
     while not q.empty():
       dom = q.get()
       if dom:
          self.reverse(dom)
       q.task_done()
   def banner(self):
      b = """

 ██░ ██  ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████ ▓█████▄ ▒███████▒
▓██░ ██▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▒██▀ ██▌▒ ▒ ▒ ▄▀░
▒██▀▀██░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ░██   █▌░ ▒ ▄▀▒░ 
░▓█ ░██ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ░▓█▄   ▌  ▄▀▒   ░
░▓█▒░██▓░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░▒████▓ ▒███████▒
 ▒ ░░▒░▒░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒▒▓  ▒ ░▒▒ ▓░▒░▒
 ▒ ░▒░ ░  ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░ ░ ▒  ▒ ░░▒ ▒ ░ ▒
 ░  ░░ ░  ░░   ░   ░   ▒   ░        ░ ░░ ░    ░    ░ ░  ░ ░ ░ ░ ░ ░
 ░  ░  ░   ░           ░  ░░ ░      ░  ░      ░  ░   ░      ░ ░    
                           ░                       ░      ░        
                        Telegram : https://t.me/kickflap
                        Discord : https://discord.gg/DmrrQkuUn6
                        Reverse IP lookup V2.0 :
                        Grab massive domains from ips
                        you know where to use them :3    
                            
                             """  

                             
     
      
      print(b)
   def input(self, q):
      #input based on python version 2 or 3 ya boubgra
      if int(py_version[0]) == 3:
           return input(str(q))
      elif int(py_version[0]) == 2:
           return input(str(q))
   def main(self):
      jobs = Queue()
      thread = 10
      try:
          hehe = self.input('Give path to Domains/Ip List -> ')
          list = open(hehe, 'r').read().splitlines()
      except IOError:
           exit("File Not Found!\n")
      except FileNotFoundError:
           exit("File Not Found!\n")
      print ('\nBetter using no more than (10) threads \nOr the tool will crash!')
      thread = int(self.input('Thread -> '))
      print('\nResult will be saved in: hrackedz.txt')
      for dom in list:
         if dom:
             jobs.put(dom)

      for x in range(thread):
         worker = threading.Thread(target=self.start, args=(jobs,))
         worker.start()


if __name__ == '__main__':
     Reverse_Ip().main()
