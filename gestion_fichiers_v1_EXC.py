#!python3.9
#coding: UTF-8

#module: gestion_fichiers_EXC
#date: 19/12/2020
#author: jmAmar

import gestion_fichiers_v1_SRC as mdlGF

fchTXT = mdlGF.Fichier_Texte()
print(type(fchTXT))
fchTXT.creer("SauvegardeScores.txt")
fchTXT.ecrire("toto")
fchTXT.ajouter(",lola")
txt = fchTXT.lire()
nom = fchTXT.nom()
print(nom,":",txt,"\n")

print("\n///\n")
