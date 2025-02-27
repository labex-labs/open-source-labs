# Introduction

En apprentissage automatique, nous évaluons souvent les performances d'un modèle de classification en utilisant un score. Cependant, nous devons également tester la significativité du score pour nous assurer que les performances du modèle ne sont pas dues au hasard. C'est là que le test de permutation du score s'avère pratique. Il génère une distribution nulle en calculant la précision du classifieur sur 1000 permutations différentes du jeu de données. Une valeur p empirique est ensuite calculée comme le pourcentage de permutations pour lesquelles le score obtenu est supérieur au score obtenu en utilisant les données originales. Dans ce laboratoire, nous utiliserons la fonction `permutation_test_score` de `sklearn.model_selection` pour évaluer la significativité d'un score validé croisé en utilisant des permutations.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
