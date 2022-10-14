def ex5():
  print("Tu es içi à ,l'évaluation.\nJe vais te poser une série de question et je te donerrais ta note sur 5. Tu peux retenter jusqu'a être satisfais\n")
  a = input("comment s'apelle la commande qui permet d'afficher un text a l'écran? ")
  b= input("Quel est la structure utilisée pour déclarer une variable? ")
  c= input("Quels sont les 3 éléments d'une boucle If ... Else? (élément1, élément2, élément3)") 
  d = input("Quels sont les 2 fonctions de base? ")
  e = input("1 + 1 = ? (J'ai pitié de ta note, c'est pour ça que je t'offre un point")
  note = 0
  if a == ("print") or ("print ()") or ("print()"):
    note +=1
  if b == ("Nom = Valeur"):
    note += 1
  if c == ("If, Elif, Else") or ("if, elif, else"):
    note += 1
  if d == ("print, variables") or ("print, variable"):
    note += 1
  if e == 2 :
    note += 1
  print("Note : " + note)
  print("Bravo, j'éspére que tu es fiére de ta note")
  