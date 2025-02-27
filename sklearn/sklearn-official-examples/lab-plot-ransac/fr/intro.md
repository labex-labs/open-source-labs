# Introduction

Dans ce laboratoire, nous allons démontrer comment ajuster robustement un modèle linéaire à des données fautives à l'aide de l'algorithme RANSAC dans scikit-learn. Le régresseur linéaire ordinaire est sensible aux valeurs aberrantes, et la droite ajustée peut facilement être déviée de la vraie relation sous-jacente des données. Le régresseur RANSAC divise automatiquement les données en données cohérentes et valeurs aberrantes, et la droite ajustée est déterminée uniquement par les données cohérentes identifiées. Nous allons utiliser le jeu de données make_regression de scikit-learn pour générer des données aléatoires avec des valeurs aberrantes, puis ajuster à la fois un modèle linéaire et un régresseur RANSAC aux données.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous réglerons rapidement le problème pour vous.
