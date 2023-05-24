ch = 'montye python flying circus'

cr = "e"

lc = len(ch)

i = 0

t = 0
while i < lc:
    if ch[i] == cr:
        t = 1
    i = i + 1
print("Le caractère", cr, end=' ')
if t == 1:
        print("est présent",end=' ')
else:
    print("est introuvable", end=' ')
    print("dans la chaine", ch)