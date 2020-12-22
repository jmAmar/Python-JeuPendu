#!python3.9
#coding: UTF-8

#module: gestion_fichiers_SRC_v2
#date: 22/12/2020
#author: jmAmar


class Fichier_Texte():
  """ classe définissant les attributs et méthodes d'un fichier texte """
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
    fchR = open(self.fichierTexte, "r")
    self.nomFichier = fchR.name
    txt = fchR.read()
    fchR.close()
    return(txt)
    
  def nom(self):
    return(self.nomFichier)
    
  
    
    
    

  