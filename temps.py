#on supposera qu'il y a 30 jours dans chaque mois, 365 jours dans une annee
s=int(12345678912)
m=s//60
heures=m//60
m=m%60
jours=heures//24
heures=heures%24
mois=jours//30
jours=jours%30
annees=jours//365
jours=jours%365
print(s,'secondes')
print(m,'minutes')
print(heures,'heures')
print(jours,'jours')
print(annees,'annees')