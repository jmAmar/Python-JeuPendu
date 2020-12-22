#!python3.9.0
#coding: UTF-8

#module: Jeu_Pendu / gestion_Scores
#content :  définitions
#author: jmAmar
#date: 15/12/2012


import gestion_fichiers_SRC_v1 as mdlGF
from json import(loads)

class Score():
  """ classe de definition d'un score """
  def __init__(self, scoreInitial):
    self.score = int(scoreInitial)

  def modifier(self, nveauScore):
    self.score = int(nveauScore)
        
  def afficher(self):
    print(" score :", self.score)
        
  def augmenter(self, augmentation):
    self.score += int(augmentation)
        
  def diminuer(self, diminution):
    self.score -= int(diminution)
        
  def appeler(self):
    return(self.score)


class Score_Joueur():
  """ classe de définition du score d'un joueur """
  def __init__(self, joueur, score):
    self.joueur = str(joueur)
    self.score = score
    # initialise un dictionnaire pour les paires joueur:score (clé:valeur)
    self.score_joueur = {}
    # cree une paire joueur:valeur
    self.score_joueur[self.joueur] = self.score
        
  def modifier(self, score):
    self.score = Score(score).appeler()
    self.score_joueur[self.joueur] = self.score
        
  def appelerJoueur(self):
    return(self.joueur)
  
  def appelerScore(self):
    return(self.score)
        
  def afficher(self):
    print("joueur :",self.joueur,", score :",self.score_joueur[self.joueur])
        
        
class gestion_scores():
  """ recherche le dernier score du joueur figurant dans le dictionnaire des scores,
      puis compare ce dernier score à celui de la dernière partie.
      Si le score de la dernière partie est plus élevé que le dernier score enregistré,
      alors ce lui de la dernière partie remplace ce dernier.
  """
  def __init__(self):
    pass
    
  def extraire(self, joueur, fichierScores="scores_joueurs.txt"):
    self.fichierScores = fichierScores
    self.joueur = joueur
    # instancie l'objet fchTexte la classe Fichier_Texte du module gestion_figestion_fichiers_SRC_v2exte = mdlGF.Fichier_Texte()
    fchTexte = mdlGF.Fichier_Texte(self.fichierScores)
    # assigne le nom du fichier texte des scores à l'objet fchTexte
    fchTexte.assigner(self.fichierScores)
    # ouvre le fchier des scores en lecture et lit son contenu. celui-ci est affecté à la variable locale dicoScores.
    dicoScores = fchTexte.lire()
    # transforme les éventuelles simple-quotes de la string dicoScores en double-quotes
    dicoScores = dicoScores.replace("\'",'\"')
    # convertit la string dicoScores en dictionnaire au format JSON pour que la fonction "keys" ci-après puisse fonctionner.
    dicoScores = loads(dicoScores)
    # recherche si la clé representée par l'identifiant du joueur est présente dans le dictionnaire
    for key in dicoScores.keys():
      if(self.joueur == key):
        # si le joueur correspond à l'une des clés contenues dans dicoScores, retourne sa valeur (score)
        r = dicoScores[key] 
        break
      else:
        r = "NO"
    return(r)   

