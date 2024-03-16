Projet de Steganographie - NSI 2022-2023
Ce projet Python de stéganographie a été réalisé dans le cadre du cours de Sciences du Numérique et de l'Informatique (NSI) pour l'année scolaire 2022-2023. 
Il propose une application permettant de cacher des messages textuels à l'intérieur d'images, en utilisant la méthode de la stéganographie.

Fonctionnalités
Le projet se compose des modules suivants :

- Module IHM avec Tkinter
Le module IHM utilise Tkinter, une bibliothèque Python standard pour créer des interfaces graphiques utilisateur (GUI). Cette interface permet à l'utilisateur de sélectionner une image, d'entrer un message à cacher et de déclencher le processus de stéganographie.

- Module Image
Le module Image est responsable de la manipulation des images. Il convertit l'image sélectionnée par l'utilisateur en une liste de valeurs RGB de ses pixels, permettant ainsi de les modifier pour cacher le message.

- Module Stega
Le module Stega met en œuvre l'algorithme de stéganographie. Il prend en entrée l'image convertie en liste de pixels RGB et le message à cacher. En utilisant des techniques de manipulation des bits, il cache le message dans les pixels de l'image choisie par l'utilisateur.

Utilisation
Pour utiliser l'application :

1. Exécutez le module IHM avec Tkinter.
2. Sélectionnez une image à traiter.
3. Saisissez le message que vous souhaitez cacher.
4. Lancez le processus de stéganographie.
5. Le message sera caché dans l'image.
6. Vous pouvez ensuite extraire le message de l'image si nécessaire.

Prérequis
Python 3.x
Tkinter (généralement inclus dans les distributions Python)
PIL (Python Imaging Library) pour la manipulation d'images

Auteur
Ce projet a été réalisé par Melvyn Bariou et Alexis Gandemer dans le cadre du cours de NSI pour l'année scolaire 2022-2023.

Licence
Ce projet est disponible sous la licence GPL.
