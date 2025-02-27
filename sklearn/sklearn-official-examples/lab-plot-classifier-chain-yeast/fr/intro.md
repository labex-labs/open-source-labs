# Introduction

Ce laboratoire démontre un exemple d'utilisation de la chaîne de classifieurs sur un ensemble de données multilabel. L'algorithme de chaîne de classifieurs est une modification de la méthode de transformation du problème pour la classification multilabel. Cette méthode exploite la corrélation entre les classes en construisant une chaîne de classifieurs binaires. Chaque modèle reçoit les prédictions des modèles précédents dans la chaîne en tant que caractéristiques. Nous utiliserons l'ensemble de données `yeast` qui contient 2417 points de données, chacun avec 103 caractéristiques et 14 étiquettes possibles. Chaque point de données a au moins une étiquette. En tant que référence, nous entraînons tout d'abord un classifieur de régression logistique pour chacune des 14 étiquettes. Pour évaluer les performances de ces classifieurs, nous prédisons sur un ensemble de test séparé et calculons le score de Jaccard pour chaque échantillon.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
