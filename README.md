# Projet fil rouge SIO 2022

## Description

Ce projet a pour but de développer l'ensemble d'une chaîne de traitements en Python, de la collecte des données en passant par la validation, la reconnaissance d'entités nommées, la mise en relation, la restitution, la déduction de nouvelles données.

Tous les projets qui se sont intégrés ont un dossier dédié avec un README associé à part Docker qui sera détaillé ici:
- AWS
- Hadoop

Dans le dossier src, se touve le code Python du projet sous forme de Notebook. Ce Notebook s'exectute sans problème sur Google Colab. J'ai principalement utilisé Google Colab pour le développement.

## Installation

Pour commencer il faut clonner le repo Github
  
    git clone https://github.com/Caojerem/Projet_fil_rouge_SIO_2022.git

Ensuite se placer dedans pour l'exécuter

    cd Projet_fil_rouge_SIO_2022
 
## Sans Docker
  
Créer un environnement virtuel

    python3 -m .venv venv
    source .venv/bin/activate

Intaller les librairies néccessaires

    pip install -r requirements.txt

## Docker
 
Pour information seulement les parties Récupération des PDF, Extraction des données, Reconnaissances des Entités nommées ont été conteneurisées.

L'image donnera les metadonnées de l'article le plus récent publé sur Arciv ainsi que les 5 pemiers noms des références
 
    docker build -t filrouge .
    docker run -d -p 80:80 filrouge
 
 ## Utilisation
 
 Lancer le Notebook
 
