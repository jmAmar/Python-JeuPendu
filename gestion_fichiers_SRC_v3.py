#!python3.9
#coding: UTF-8

#module: gestion_fichiers_SRC_v2
#date: 22/12/2020
#author: jmAmar


class Fichier_Texte():
  """ classe definissant les attributs et methodes d'un fichier texte """
  def __init__(self):
    self.fichierTexte = self
    self.nomFichier = ""
  
  def assigner(self, fch):
    self.fichierTexte = str(fch)
  
  def ecrire(self, txt):
    fchW = open(self.fichierTexte, "w")
    self.nomFichier = fchW.name
    fchW.write(str(txt))
    fchW.close()

  def ajouter(self, txt):
    fchA = open(self.fichierTexte, "a")
    self.nomFichier = fchA.name
    fchA.write(str(txt))
    fchA.close()

  def lire(self):
    #vérifie l'existence du fichier de gestion des scores
    from os.path import isfile
    if(not isfile(self.fichierTexte)):
      self.ecrire("")
    fchR = open(self.fichierTexte, "r")
    self.nomFichier = fchR.name
    txt = fchR.read()
    fchR.close()
    return(txt)
    
  def nom(self):
    return(self.nomFichier)
    
  
    
    
    

  