#!python3.9
#coding: UTF-8

#module: gestion_scores_EXC
#content : execution
#date: 18/12/2020
#author: jmAmar


import gestion_scores_v1_SRC as mdlSS
import gestion_fichiers_v1_SRC as mdlGF
from json import dumps

global liste_scores
liste_scores = [("J001",10),("J003",20),("J004",15)]


def main():
  # transforme la liste des scores en dictionnaire
  print("liste_scores :",liste_scores,"\n")
  
  dico_scores = dict(liste_scores)
  print("dico_cores",dico_scores,"\n")
  
  # enregistre le dictionnaire dans le fichier de sauvegarde
  enregistrer_dictionnaire(dico_scores)

  # affiche les scores de joueurs
  afficher_score("J003")
  afficher_score("J005")
  
  print("\n///\n")


def enregistrer_dictionnaire(dico):
  # instancie l'objet fchTexte de la classe Fichier_Texte du module gestion_fichiers_v1_SRC
  fchTexte = mdlGF.Fichier_Texte()
  # affecte le nom du fichier des scores à l'objet créé
  fchTexte.assigner("scores_joueurs.txt")
  # convertit le dictionnaire dico en string au format JSON
  txtScores = dumps(dico)
  # ouvre le fichier des scores et y inscrit la string txtScores 
  fchTexte.ecrire(txtScores)
  # aux fins de vérification, ouvre le fichier des scores en lecture et récupère son contenu et son nom
  txt = fchTexte.lire()
  nom = fchTexte.nom()
  # affiche le résultat de la vérification
  print("{} :: {}\n".format(nom,txt))
  

# a modifier et compléter
def enregistrer_score(score):
  """ recherche le dernier score du joueur figurant dans le dictionnaire des scores,
      puis compare ce dernier score à celui de la dernière partie.
      Si le score de la dernière partie est plus élevé que le dernier score enregistré,
      alors ce lui de la dernière partie remplace ce dernier.
  """
  fchTexte = mdlGF.Fichier_Texte()
  fchTexte.assigner("scores_joueurs.txt")
  # dicoScores= dumps(dico_scores)
  # fichTexte.ecrire(txt_scores)
  txt = fchTexte.lire()
  nom = fchTexte.nom()
  print("{} :: {}\n".format(nom,txt))

 
def extraire_score(joueur):
  # instancie l'objet gestionScores de la classe Gestion_Scores du module gestion_scores_v1_SRC
  gestionScores = mdlSS.gestion_scores()
  # appelle la méthode "extraire" de l'objet instancié pour récupérer le score du joueur passé en paramètre
  score = gestionScores.extraire(joueur)
  return(score)

def afficher_score(joueur):
  # appelle la fonction "extraire_score" ci-dessus pour obtenir le score du joueur
  score = extraire_score(joueur)
  if(score != "NO"):
    print("score enregistré pour le joueur no.{}: {}".format(joueur,score))
  else:
    print("pas de score enregistré pour le joueur no.{}".format(joueur))


if(__name__ == "__main__"):
  main()











        
    