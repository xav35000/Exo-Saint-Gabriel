from colorama import Fore, init, deinit
import replit
init()
from exo1 import ex1
from exo2 import ex2
from exo3 import ex3
from exo4 import ex4
def menu():
  replit.clear
  exo = 0
  print (Fore.WHITE + "\n __  __")
  print (Fore.WHITE + "|  \/  | ___ _ __  _   _")
  print (Fore.WHITE + "| |\/| |/ _ \ '_ \| | | |")
  print (Fore.WHITE + "| |  | |  __/ | | | |_| |")
  print (Fore.WHITE + "|_|  |_|\___|_| |_|\__,_|")
  print (Fore.WHITE + "1. Print")
  print (Fore.WHITE + "2. Variables")
  print (Fore.WHITE + "3. If ... Else")
  print (Fore.WHITE + "4. Fonctions De Base")
  exo = int(input("Quel est le numéro de l'éxercice choisi? "))
  if exo == 1:
   ex1()
  elif exo == 2:
    ex2()
  elif exo == 3:
     ex3()
  elif exo == 4:
    ex4()
  elif exo == 9:
   exit()
menu()
# à regarder absolument https://aws.amazon.com/fr/free/?awsm.page=2&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all&awsm.page-all-free-tier=1
#https://aws.amazon.com/fr/dynamodb/?did=ft_card&trk=ft_card
#pour régler le problème de ressource
import atexit
import replit
atexit.register(replit.clear)

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#J'ai pas eu le temps de caser ce qu'il y a au dessus et j'ai vite fait casser quelques trucs...