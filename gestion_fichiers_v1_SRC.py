#!python3.9
#coding: UTF-8

#module: gestion_fichiers_SRC
#date: 18/12/2020
#author: jmAmar


class Fichier_Texte():
  """ classe définissant les attributs et méthodes d'un fichier texte """
  def __init__(self):
    self.fchTXT = self
    self.nomFCH = ""
  
  def assigner(self, fch):
    self.fchTXT = str(fch)
  
  def ecrire(self, txt):
    fchW = open(self.fchTXT, "w")
    self.nomFCH = fchW.name
    fchW.write(str(txt))
    fchW.close()

  def ajouter(self, txt):
    fchA = open(self.fchTXT, "a")
    self.nomFCH = fchA.name
    fchA.write(str(txt))
    fchA.close()

  def lire(self):
    fchR = open(self.fchTXT, "r")
    self.nomFCH = fchR.name
    txt = fchR.read()
    fchR.close()
    return(txt)
    fchR.close()
    
  def nom(self):
    return(self.nomFCH)
    
  
    
    
    

  