#!python3.9
#coding: UTF-8

#module: fichiersRW
#date: 18/12/2020
#author: jmAmar

print("\n\t*** Fichiers R&W ***\n")
  
def main():
  global fichTXT
  fichTXT = "scoresPendu.txt"
  #
  text1 = "J001:10\nJ003:20\nJ004:15"
  ecrire(text1)
  #
  text2 = lire()
  dico = convertirEnDictionnaire(text2)
  print(dico)
  #
  text3 = ""
  for item in dico.items():
    print(item)
    strItem = str(item)
    strItem = strItem.replace(",",":")
    strItem = strItem.replace("(","")
    strItem = strItem.replace("\'","")
    strItem = strItem.replace(" ","")
    strItem = strItem.replace(")","\n")
    text3 += strItem
  #ecrire(text3)
  print(text3)
  #
  print("\n///\n")


def ecrire(txt):
  fchW = open(fichTXT,"w")
  fchW.write(txt)
  fchW.close()


def ajouter(txt):
  fchA = open(fichTXT,"a")
  fchA.write(txt)
  fchA.close()


def lire():
  fchR = open(fichTXT,"r")
  txt = fchR.read()
  fchR.close()
  return(txt)

def convertirEnDictionnaire(txt):
  txt = txt.replace("\n",",")
  ls1 = txt.split(",")
  ls2 = []
  for el1 in ls1:
    el2 = el1.split(":")
    ls2.append(el2)
  dco = dict(ls2)
  print(dco)
  for key in dco.keys():
    print("clé : {} , valeur : {}".format(key, dco[key]))
  return(dco) 


if(__name__ == "__main__"):
  main()
  

"""    
def convertirDico():
  txt = lire()
  txt = txt.replace("\n",",")
  print(txt)
  lst = txt.split(",")
  print(lst)
  listeScores = []
  for el1 in lst:
    el2 = el1.split(":")
    print(el2)
    listeScores.append(el2)
  print(listeScores)
  dco = dict(listeScores)
  print(dco)
  for key in dco.keys():
    print("clé : {} , valeur : {}".format(key, dco[key]))
""" 

