import os
pseudo = os.environ['username']
pwd = os.environ['password']
def admin():
  id =input("Identifiant?:\n")
  pswd =input("Mot de pass:\n")
  if id == pseudo and pswd == pwd:
    print("aaaaa")
    admin_menu()
  else:
    print ("faux")
def admin_menu():
  print ("hello")
  