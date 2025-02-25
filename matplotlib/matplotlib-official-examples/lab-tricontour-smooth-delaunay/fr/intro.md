# Introduction

Ce tutoriel montre comment générer des graphes de tricontours haute résolution avec Matplotlib. La tricontouring est une technique utilisée pour représenter des données sur un maillage triangulaire non structuré. Elle est souvent utilisée lorsque les données sont collectées à des points espacés de manière irrégulière, ou lorsque les données sont intrinsèquement triangulaires par nature. Le tutoriel montrera comment générer un ensemble aléatoire de points, effectuer une triangulation de Delaunay sur ces points, masquer certaines des triangles dans le maillage, raffiner et interpoler les données, et finalement tracer les données raffinées à l'aide de la fonction `tricontour` de Matplotlib.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous résoudrons rapidement le problème pour vous.
