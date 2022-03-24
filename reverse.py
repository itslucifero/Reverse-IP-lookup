# i used this modules if u got better ones please add :p
#telegram me : https://t.me/kickflap
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

# My Used colors :p
if sys.platform in ["linux","linux2"]:
   purple = '\033[95m'
   blue = '\033[94m'
   cyan = '\033[96m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   end = '\033[0m'
   bold = '\033[1m'
   u = '\033[4m'
else:
   purple = ''
   blue = ''
   cyan = ''
   green = ''
   yellow = ''
   red = ''
   end = ''
   bold = ''
   u = ''

#clearing the interpreter in both systems Linux and WINDOWS
if sys.platform == 'win32':
   os.system('cls')
else:
   os.system('clear')

# Our class for the main reverse job
class Reverse_Ip:
   def __init__(self):
      self.url = 'https://reverseip-tools.com/api?q='
      self.banner()
      self.save = 'hrackedz.txt'
   def reverse(self, domain):
        try:
            req = requests.get(self.url+domain)
            if req.status_code == 200:
                jumlah = len(req.json()['result'])
                if jumlah > 10  and  jumlah < 100:
                    color = yellow
                elif jumlah < 10:
                    color = red
                else:
                    color = green
                print ("{} >> ({} domains)".format(color+domain, str(jumlah)))
                res = req.json()
                if res['result']:
                    domains = '\n'.join(res['result'])
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
                        website : https://hrackedz.com
                        Reverse IP tool :
                        Grab massive domains from ips
                        you know where to use them :3    
                            
                             """  

                             
      co = random.choice([red,purple,blue])
      ct = random.choice([green,cyan,yellow])
      banner = b.replace('◢◤',co+'◢◤').replace('R',ct+'R').replace('B',ct+'B')
      print(banner)
   def input(self, q):
      #input based on python version
      if int(py_version[0]) == 3:
           return input(str(q))
      elif int(py_version[0]) == 2:
           return input(str(q))
   def main(self):
      jobs = Queue()
      thread = 10
      try:
          filename = self.input(yellow+'Give path to Domains/Ip List -> '+green)
          list = open(filename, 'r').read().splitlines()
      except IOError:
           exit(red+"File Not Found!\n")
      except FileNotFoundError:
           exit(red+"File Not Found!\n")
      print (red+'\nBetter using no more than (10) threads \nOr the tool will crash!')
      thread = int(self.input(yellow+'Thread -> '+green))
      print(blue+'\nResult will be saved in: hrackedz.txt')
      for dom in list:
         if dom:
             jobs.put(dom)

      for x in range(thread):
         worker = threading.Thread(target=self.start, args=(jobs,))
         worker.start()


if __name__ == '__main__':
     Reverse_Ip().main()