from colorama import Fore, Back, init, deinit
import replit


def ex2():
    replit.clear()
    print(" __      __        _       _     _           ")
    print(" \ \    / /       (_)     | |   | |          ")
    print("  \ \  / /_ _ _ __ _  __ _| |__ | | ___  ___ ")
    print("   \ \/ / _` | '__| |/ _` | '_ \| |/ _ \/ __|")
    print("    \  / (_| | |  | | (_| | |_) | |  __/\__ |")
    print("     \/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/")
    print("Maintenant, nous allons voir les variable.\n")
    print(
        "Une variable sert à contenir quelque chose (des mots, des chiffres ...). on utilise la structure : Nom = Valeur\n/!\ attention, cette structure est a retenir /!\ "
    )
    print("Ex:")
    print(Fore.GREEN + "chats = 2")
    print(Fore.WHITE + "print('chats')")
    print(
        Fore.WHITE +
        "Maintenant, à ton tour. Crée une variable appelée note, donne lui la valeur que tu veux"
    )
    var = input("")
    rep = "note = "
    b = 0
    while b == 0:
        if var.find(rep):
            print(
                "bravo passons a la seconde partie du cour.\n maintenant, nous allons integrer une variable dans un print. pour cela, nous allons creer un print:\nprint ('Bonjour')\nNous allons ensuite ajouter un nom derriere le print.\nnom = 'Jean'\nprint ('Bonjour ' + nom)\nNous aurons donc une sortie du genre :\nBonjour Jean"
            )
            a = input()
            b = 1
            break
        else:
            print("Faux, Recommence")
