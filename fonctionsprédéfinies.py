i, list = 1, []
# i est un booléen true

while i:
    valeurInput = input("Veuillez entrer une valeur : ")
    if valeurInput != "":  # tant que l'utilisateur ne rentre pas d'entrée
        list.append(int(valeurInput))  # on entre l'input dans la liste
    else:
        i = 0  # sinon, i vaut false

print(list)