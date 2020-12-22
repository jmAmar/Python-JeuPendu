#!python3.9
#coding: UTF-8

#module: fichiersRW
#date: 18/12/2020
#author: jmAmar

print("\n\t*** Fichiers R&W ***\n")

import json

# convert to string
var1 = json.dumps({'id': 10 })
print(type(var1))
print(var1)

# load to dict
var2 = json.loads(var1)
print(type(var2))
print(var2)
print()


liste_scores = [("J001",10),("J003",20),("J004",15)]
print(liste_scores)
print(type(liste_scores))

dico_scores = dict(liste_scores)
print(dico_scores)
print(type(dico_scores))

def ecrire(txt):
  fchW = open("scoresPendu.txt","w")
  fchW.write(txt)
  fchW.close()
  
ecrire(json.dumps(liste_scores))
ecrire(json.dumps(dico_scores))

string_scores = '{"J001": 10, "J003": 20, "J004": 15}'
dico_scores = json.loads(string_scores)
print(dico_scores)
print(type(dico_scores))
dico_scores.update({"J005":5})
print(dico_scores)
tpl = [("J006",25)]
dco = dict(tpl)
print(dco)
dico_scores.update(dco)
print(dico_scores)
ecrire(json.dumps(dico_scores))

def lire():
  fchR = open("scoresPendu.txt","r")
  txt = fchR.read()
  fchR.close()
  return(txt)

string_scores = lire()
dico_scores = json.loads(string_scores)
print(dico_scores)
print(type(dico_scores))

valeur = dico_scores.get('J000')
print(valeur)
if(valeur == None):
  print("NO")
else:
  print(valeur)

