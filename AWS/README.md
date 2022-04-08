# Instruction pour le module AWS

## Descriptif

Le format Notebook est employé pour le projet. Il est fonctionnel mais il est néanmoins nécessaire dans renseigner ACCESS_ID, ACCESS_KEY et ACCESS_TOKEN.

## Installation

Dans le terminal, excutez la commande ci-dessous

    git clone https://github.com/Caojerem/pdf-reader-api.git

Travaillez ensuite depuis ce répertoire.

Si besoin, créer un environnement virtuel puis l'activer

    python3 -m venv venv
    . venv/bin/activate

Installer ensuite les librairies néccessaires

    pip install -r requirements.txt

## Utilisation

Le Notebook devrait renvoyer les premières entités nommées dans les références (limité à 5000 bytes) grace au service COMPREHEND d'AWS
