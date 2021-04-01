# Project purBeurre

This project involves retrieving products from the OpenFoodFacts site (https://fr.openfoodfacts.org) and storing them in a database.
The user of this project can then browse this database by choosing a category and then a product. 
An algorithm finaly proposes a substitute of this product with a better nutriscore (and with a maximum of category in common with the substituted product).

## To begin

To get a good start with the project, you will have here some instructions concerning the pre-requisite installations and those to be done.

### Requirements

Have to install on your device :

* Python 3.7.6 or a higher version (if not : https://www.python.org/downloads/)
* Pipenv (if not : https://geniesducode.com/articles/comment-installer-pipenv/)
* MySQL (if not : https://openclassrooms.com/fr/courses/1959476-administrez-vos-bases-de-donnees-avec-mysql/1959969-installez-mysql)

### Installation

1. Go to your terminal, in the folder where you want to install this project
1. Run the command: `git clone https://github.com/QuentinDevPython/PurBeurre.git`
1. Go to the newly created project folder with: `cd PurBeurre`
1. Run the command: `pipenv shell`pour lancer l'environnement virtuel du projet
1. Install an unsupported pipenv dependency: `pip install mysql-connector-python`

L'installation est maintenant terminée

## Start the project

To start the project, go to your terminal where you installed the project and execute the following command:
`python main.py`

## Made with

Here are some software/resources I used to develop my project :

* Openclassrooms course : https://openclassrooms.com/fr/courses/1959476-administrez-vos-bases-de-donnees-avec-mysql
* SublimeText (text editor)
* MySQL (to interpretate SQL programming langage)
* Peewee (to interpretate Python programming langage)

## Authors

* Quentin Barthélémy (student in application development with Python)
* Ranga Gonnage (my Openclassrooms mentor)
