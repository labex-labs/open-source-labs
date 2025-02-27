# Introduction

Dans ce laboratoire, nous allons utiliser le jeu de données Ames Housing pour comparer différentes méthodes de gestion des variables catégorielles dans les estimateurs Gradient Boosting. Le jeu de données contient des variables numériques et catégorielles, et la variable cible est le prix de vente des maisons. Nous comparerons les performances de quatre pipelines différents :

- Suppression des variables catégorielles
- Encodage one-hot des variables catégorielles
- Traitement des variables catégorielles comme des valeurs ordinale
- Utilisation du support natif pour les variables catégorielles dans l'estimateur Gradient Boosting

Nous évaluerons les pipelines en termes de temps d'ajustement et de performances de prédiction en utilisant la validation croisée.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous réglerons rapidement le problème pour vous.
