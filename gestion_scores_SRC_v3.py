#!python3.9.0
#coding: UTF-8

#module: Jeu_Pendu / gestion_Scores
#content :  définitions
#author: jmAmar
#date: 15/12/2012


import gestion_fichiers_SRC_v3 as mdlGF
from datetime import datetime
import json

class Score():
  """ classe de definition d'un score """
  def __init__(self, scoreInitial):
    self.score = int(scoreInitial)

  def modifier(self, nouveauScore):
    self.score = int(nouveauScore)
        
  def afficher(self):
    print(" score :", self.score)
        
  def augmenter(self, augmentation):
    self.score += int(augmentation)
        
  def diminuer(self, diminution):
    self.score -= int(diminution)
        
  def extraire(self):
    return(self.score)


class Score_Joueur():
  """ classe de définition du score d'un joueur """
  def __init__(self, joueur, score):
    self.joueur = str(joueur)
    self.score = score
    self.horodatage = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # initialise un dictionnaire pour les paires joueur:score (clé:valeur)
    self.score_joueur = {}
    # cree une paire joueur:valeur
    self.score_joueur[self.joueur] = (self.score,self.date_heure)
        
  def modifier(self, score):
    self.horodatage = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    self.score_joueur[self.joueur][0] = score
    self.score_joueur[self.joueur][1] = self.horodatage
        
  def extraireJoueur(self):
    return(self.joueur)
  
  def extraireScore(self):
    return(self.score,self.horodatage)
        
  def afficherScoreJoueur(self):
    print("joueur : {} , score : {} , date&heure : {}"
          .format(self.joueur,self.score_joueur[self.joueur][0],self.score_joueur[self.joueur][1]))


class Gestion_Scores():
  """ recherche le dernier score du joueur figurant dans le dictionnaire des scores,
      puis compare ce dernier score à celui de la dernière partie.
      Si le score de la dernière partie est plus élevé que le dernier score enregistré,
      alors ce lui de la dernière partie remplace ce dernier.
  """
  def __init__(self):
    pass
  
  def enregistrerScoreJoueur(self, joueur, score, fichierScores="scores_joueurs.txt"):
    self.fichier_scores = fichierScores
    self.joueur = joueur
    self.score = score
    self.horodatage = datetime.now().strftime("%d/%m/%Y %H:%M:%S")# créé une liste contenant un tuple composé du no. du joueur et de son score
    # créé une liste contenant le joueur et ses éléments de score associés
    joueur_score = [(joueur,(score,self.horodatage))]
    # convertit la liste score_joueur en dictionnaire
    score_joueur = dict(joueur_score)
    # instancie l'objet fichier_texte de la classe Fichier_Texte du module gestion_fichiers_SRC_v2
    fichier_scores = mdlGF.Fichier_Texte()
    # assigne le nom du fichier des scores à l'objet fichier_texte
    fichier_scores.assigner(self.fichier_scores)
    # ouvre le fchier des scores en lecture et lit son contenu. celui-ci est affecté à la variable locale string_scores
    string_scores = fichier_scores.lire()
    # test si le fichier contient des scores enregistrés
    if(string_scores != ""):
      # convertit la chaîne string_score en dictionnaire avec la fonction "loads" de la bibliothèque json
      dico_scores = json.loads(string_scores)
      # insère le dictionnaire score_joueur dans le dictionnaire dico_scores
      dico_scores.update(score_joueur)
    else:
      dico_scores = score_joueur
    # convertit le dictionnaire dico_scores en string avec la fonction "dumps" de la bibliothèque json
    string_scores = json.dumps(dico_scores)
    # enregistre la string des scores des joueurs dans le fichier des scores
    fichier_scores.ecrire(string_scores)
    """
    # aux fins de vérification, ouvre le fichier des scores en lecture et récupère son contenu et son nom
    txt = fichier_scores.lire()
    nom = fichier_scores.nom()
    # affiche le résultat de la vérification
    print("'{}' : {}\n".format(nom,txt))
    """
  
  
  def extraireScoreJoueur(self, joueur, fichierScores="scores_joueurs.txt"):
    self.fichier_scores = fichierScores
    self.joueur = joueur
    # instancie l'objet fichier_scores de la classe Fichier_Texte du module gestion_fichiers_SRC_v2
    fichier_scores = mdlGF.Fichier_Texte()
    # assigne le nom du fichier des scores à l'objet fichier_scores
    fichier_scores.assigner(self.fichier_scores)
    # ouvre le fchier des scores en lecture et lit son contenu. celui-ci est affecté à la variable locale string_scores
    string_scores = fichier_scores.lire()
    # convertit la chaîne string_score en dictionnaire avec la fonction "loads" de la bibliothèque json
    dico_scores = json.loads(string_scores)
    # extrait la valeur associée à la clé joueur dans le dictionnaire dico_scores
    score_joueur = dico_scores.get(joueur)
    return(score_joueur)
  
  
  def actualiserScoreJoueur(self, joueur, score, fichierScores="scores_joueurs.txt"):
    # extraction du score enregistré
    self.score_enregistre = self.extraireScoreJoueur(joueur)
    self.nouveau_score = score
    # compare les deux scores. Si le score tranmis est supérieur au score enregistré, il est alors enregistré
    if(self.nouveau_score > self.score_enregistre[0]):
      self.enregistrerScoreJoueur(joueur, self.nouveau_score)
    
  
  def afficherScoreJoueur(self,joueur):
    # appelle la fonction "extraire_score" ci-dessus pour obtenir le score du joueur
    score_joueur = self.extraireScoreJoueur(joueur)
    if(score_joueur != None):
      print("score joueur {} : {} - {}".format(joueur,score_joueur[0], score_joueur[1]))
    else:
      print("score joueur {} : non enregistré.".format(joueur))
    
   
