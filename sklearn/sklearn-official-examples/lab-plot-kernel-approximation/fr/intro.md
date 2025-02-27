# Introduction

Ce laboratoire illustre l'approximation de la carte de caractéristiques d'un noyau RBF en utilisant RBFSampler et Nystroem pour approximer la carte de caractéristiques d'un noyau RBF pour la classification avec un SVM sur l'ensemble de données des chiffres. Les résultats obtenus avec un SVM linéaire dans l'espace original, un SVM linéaire utilisant les mappages approximatifs et un SVM à noyau sont comparés. Les temps d'exécution et la précision pour différents nombres d'échantillonnages Monte Carlo (dans le cas de RBFSampler, qui utilise des caractéristiques de Fourier aléatoires) et différents sous-ensembles de taille du jeu d'entraînement (pour Nystroem) pour le mappage approximatif sont présentés.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
