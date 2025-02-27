# Introduction

Ce laboratoire illustre comment appliquer différents pipelines de prétraitement et d'extraction de fonctionnalités à différents sous-ensembles de fonctionnalités, en utilisant `ColumnTransformer`. Cela est particulièrement pratique dans le cas de jeux de données qui contiennent différents types de données, car nous pouvons vouloir mettre à l'échelle les fonctionnalités numériques et encoder en une-hot les fonctionnalités catégorielles.

Dans ce laboratoire, nous utiliserons le jeu de données Titanic d'OpenML pour construire un pipeline qui prétraite les données catégorielles et numériques à l'aide de `ColumnTransformer` et l'utiliser pour entraîner un modèle de régression logistique.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour passer à l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous résoudrons rapidement le problème pour vous.
