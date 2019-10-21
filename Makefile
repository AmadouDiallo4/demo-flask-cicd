
build:


# Une cible "prepare" qui fasse l'installation des dependances du projet

prepare:
	pipenv install 

# TODO: ajouter une cible "Test" qui test la qualite du projet (et plante sinon)
#
test:
	pipenv run pylint hello.py
