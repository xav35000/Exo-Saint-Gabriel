from colorama import Fore, init, deinit
import replit


def ex1():
    while 0 == 0:
        replit.clear
        print(Fore.BLUE + "  _____      _       _  ")
        print(Fore.BLUE + " |  __ \    (_)     | | ")
        print(Fore.BLUE + " | |__) | __ _ _ __ | |_ ")
        print(Fore.BLUE + " |  ___/ '__| | '_ \| __|")
        print(Fore.BLUE + " | |   | |  | | | | | |_ ")
        print(Fore.BLUE + " |_|   |_|  |_|_| |_|\__|")
        print(
            Fore.WHITE +
            "Bonjour, nous allons commencer par éxécuter la commande la plus simple \nqu'il soit : nous allons faire dire à la console 'Hello World'\nEn python, nous allons utiliser la fonction 'print', print \ns'accompagne systématiquement de parenthèses avec des guillemets à \nl'intérieur, tel que : ("
            ")\nC'est maintenant à vous d'essayer !\nAppuyez sur la touche entrée quanc vous avez terminé\n"
        )
        v = 0
        while v == 0:
            reponse = input("")
            if reponse == 'print ("Hello World")':
                v == 1
                print("\nBravo")

                break
            if reponse == 'print ("hello world")':
                v == 1
                print("\nBravo")

                break
            if reponse == 'print("Hello World")':

                print("\nBravo")

                break
            if reponse == 'print("hello world")':
                print("\nBravo")

                break
            else:
                print("Tu t'est trompé, recommence")
                print()
