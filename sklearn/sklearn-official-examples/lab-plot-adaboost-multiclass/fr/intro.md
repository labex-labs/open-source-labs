# Introduction

Dans ce laboratoire, nous allons explorer la manière dont le boosting peut améliorer la précision de prédiction sur un problème multi-classe. Nous utiliserons un ensemble de données construit en prenant une distribution normale standard de dix dimensions et en définissant trois classes séparées par des sphères concentriques imbriquées de dix dimensions de sorte que le nombre de samples soit approximativement égal dans chaque classe.

Nous comparerons les performances des algorithmes SAMME et SAMME.R. SAMME.R utilise les estimations de probabilité pour mettre à jour le modèle additif, tandis que SAMME utilise seulement les classifications.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session et nous résoudrons rapidement le problème pour vous.
