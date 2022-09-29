from colorama import Fore, init, deinit
def ex3():
  import replit
  replit.clear()
  print (Fore.CYAN +   "  _____  __      ______ _          ")
  print (Fore.CYAN +   " |_   _|/ _|    |  ____| |         ")
  print (Fore.CYAN +   "   | | | |_     | |__  | |___  ___ ")
  print (Fore.CYAN +   "   | | |  _|    |  __| | / __|/ _ |")
  print (Fore.CYAN +   "  _| |_| |_ _ _ | |____| \__ \  __/")
  print (Fore.CYAN +   " |_____|_(_|_|_)|______|_|___/\___|")
         
  print(Fore.WHITE + "\nIci, nous allons voir les condition 'if ... else'\nC'est une fonction qui vérifie une condition.\n Il y a trois éléments dans une boucle 'if ... else:   If, qui vérifie la condition    elif, qui, si la 1ére condition n'est pas vérifiée, en propose une deuxiéme      et else qui à la différence de elif, ne propose aucune deuxiéme condition et termine la boucle.\nOpérateurs:\n==, est égal à\n!=, est différent de\n<, plus petit que\n>, plus grand que\n<=, supérieur ou égal à\n>=, inférieur ou égal à\nStructure:\nscore = input('Quel était ta derniére note ?  (sur 20)  '')\nscore = int(score)\nif score <= 20:\n  score = str(score)\n  print('Ta note est: ' + score + '/20')\nelse:\n  print('La note entrée n'est pas valide')" )
  score = input("Quel était ta derniére note ? (sur 20) ")
  print("\nVoici le résultat du code ci-dessus:\n")
  score = int(score)
  if score <= 20:
    score = str(score)
    print("Ta note est: " + score + "/20")
    
  else:
    print("La note entrée n'est pas valide")