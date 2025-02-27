# Introduction

Ce tutoriel vous guidera tout au long du processus d'utilisation de techniques d'approximation de noyau dans scikit-learn.

Les méthodes de noyau, telles que les machines à vecteurs de support (SVM), sont des techniques puissantes pour la classification non linéaire. Ces méthodes reposent sur le concept d'une fonction noyau qui projette les données d'entrée dans un espace de caractéristiques de dimension élevée. Cependant, travailler avec des mappages de caractéristiques explicites peut être coûteux en calcul, en particulier pour de grandes bases de données. Les méthodes d'approximation de noyau offrent une solution en générant des approximations de basse dimension de l'espace de caractéristiques de noyau.

Dans ce tutoriel, nous explorerons plusieurs techniques d'approximation de noyau disponibles dans scikit-learn, y compris la méthode de Nystroem, l'approximation du noyau à fonction de base radiale (RBF), l'approximation du noyau Additive Chi Squared (ACS), l'approximation du noyau Skewed Chi Squared (SCS) et l'approximation du noyau polynomial à l'aide de Tensor Sketch. Nous démontrerons comment utiliser ces techniques et discuterons de leurs avantages et limites.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous réglerons rapidement le problème pour vous.
