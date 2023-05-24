#ce code affiche les jours de semaines
day = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
a, b = 0, 0
while a < 7:
# additions les chiffre jusque a 7
    a = a + 1
    b = a % 7
    print(day[b])
