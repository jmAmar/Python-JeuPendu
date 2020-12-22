#!python3.9
#coding: UTF-8

#module: gestion_scores_EXC_v2
#content : execution
#date: 18/12/2020
#author: jmAmar


import gestion_scores_SRC_v2 as mdlGS
import gestion_fichiers_SRC_v2 as mdlGF

import json

global fichier_scores
fichier_scores = "scores_joueurs.txt"

global liste_scores
liste_scores = [("J001",10),("J003",20),("J004",15)]


def main():
  # initialise l'exécution
  initialiserExecution(fichier_scores)
  #
  # transforme la liste des scores en dictionnaire
  dico_scores = dict(liste_scores)
  #
  # enregistre le dictionnaire dans le fichier des scores
  enregistrerDictionnaire(dico_scores, fichier_scores)
  #
  # affiche les scores de joueurs
  gestion_scores.afficherScoreJoueur("J003")
  gestion_scores.afficherScoreJoueur("J005")
  #
  # ajoute le score d'un nouveau joueur
  gestion_scores.enregistrerScoreJoueur("J005",5)
  gestion_scores.afficherScoreJoueur("J005")
  #
  # actualise le score d'un joueur
  gestion_scores.actualiserScoreJoueur("J005", 10)
  gestion_scores.afficherScoreJoueur("J005")
  #
  gestion_scores.afficherScoreJoueur("J004")
  gestion_scores.actualiserScoreJoueur("J004", 10)
  gestion_scores.afficherScoreJoueur("J004")
  
  print("\n///\n")
  
  
def initialiserExecution(fichierScores = fichier_scores):
  # instancie la classe Gestion_Scores en objet gestion_scores
  global gestion_scores
  gestion_scores = mdlGS.Gestion_Scores()
  # instancie l'objet fichier_texte de la classe Fichier_Texte du module gestion_fichiers_SRC_v2
  global fichier_scores
  fichier_scores = mdlGF.Fichier_Texte()
  # affecte le nom du fichier des scores à l'objet créé
  fichier_scores.assigner(fichierScores)
  

def enregistrerDictionnaire(dico,fichierScores):
  # convertit le dictionnaire dico en string avec la fonction "dumps" de la bibliothèque json
  string_scores = json.dumps(dico)
  # ouvre le fichier des scores et y inscrit la string string_scores 
  fichierScores.ecrire(string_scores)
  # aux fins de vérification, ouvre le fichier des scores en lecture et récupère son contenu et son nom
  txt = fichierScores.lire()
  nom = fichierScores.nom()
  # affiche le résultat de la vérification
  print("'{}' : {}\n".format(nom,txt))
  

if(__name__ == "__main__"):
  main()











        
    