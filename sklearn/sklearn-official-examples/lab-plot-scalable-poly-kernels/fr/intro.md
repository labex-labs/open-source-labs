# Introduction

Ce laboratoire démontrera comment utiliser l'approximation du noyau polynomial dans scikit-learn pour générer efficacement des approximations d'espace de caractéristiques de noyau polynomial. Cela est utilisé pour entraîner des classifieurs linéaires qui approchent la précision des classifieurs à noyau. Nous utiliserons le jeu de données Covtype, qui contient 581 012 échantillons avec 54 caractéristiques chacun, répartis entre 6 classes. Le but de ce jeu de données est de prédire le type de couvert forestier à partir de variables cartographiques seulement (aucune donnée de télédétection). Après le chargement, nous le transformons en un problème de classification binaire pour correspondre à la version du jeu de données sur la page web de LIBSVM, qui était celle utilisée dans l'article original.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous réglerons rapidement le problème pour vous.
