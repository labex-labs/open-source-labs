# Introduction

Dans ce laboratoire, nous allons explorer la manière dont la complexité du modèle influence à la fois la précision de prédiction et la performance de calcul. Nous utiliserons deux jeux de données - le Diabetes Dataset pour la régression et le 20newsgroups Dataset pour la classification. Nous modéliserons l'influence de la complexité sur trois estimateurs différents :

- SGDClassifier (pour les données de classification) qui implémente l'apprentissage par descente de gradient stochastique
- NuSVR (pour les données de régression) qui implémente la régression vectorielle à support Nu
- GradientBoostingRegressor construit un modèle additif de manière progressive et itérative

Nous allons varier la complexité du modèle en choisissant les paramètres de modèle appropriés dans chacun de nos modèles sélectionnés. Ensuite, nous mesurerons l'influence sur la performance de calcul (latence) et la puissance prédictive (MSE ou perte de Hamming).

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
