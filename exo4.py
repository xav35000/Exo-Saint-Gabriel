from colorama import Fore, init, deinit
def ex4():
  print( "__     __         _       _     _\n\ \   / /_ _ _ __(_) __ _| |__ | | ___  ___ \n \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|\n  \ V / (_| | |  | | (_| | |_) | |  __/\__ \ \n   \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/")
  print("Bonjour,\nTout d'abord, quesqu'une variable ?\nEh bien, une variable n'est rien d'autre qu'un paquet d'information, on va y stocker des valeurs.\nMaintenant, Comment signaler une variable ?\nC'est super simple aussi. Il suffit d'écrire le nom d'une variable, inserer le signe égal et de mettre la valeur de la variable.\nEx:   chats = 2\n    nom_|     |_valeur\nPour donner une nouvelle valeur à la variable, il suffit de la 'recréer' en lui donnant une nouvelle valeur.\nPS: Je te conseille de toujour mettre tes variables au tout debut de ton code.")

  while(0 == 0):
    x = input("A ton tours, crée une variable appelée voiture et assigne lui une valeur de 1\n")
  if(x == "voiture = 1"):
    print(Fore.GREEN + "Bravo")
  elif(x == "voitures = 1"):
    print(Fore.GREEN + "Bravo")    
  else:
    print(Fore.GREEN + "faux, réessaye\n")
  print(" Il y a également le print vu plus haut.\nCe sont les 2 fonctions indispensables")