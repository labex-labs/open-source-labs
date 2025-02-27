# Introduction

Ce tutoriel montrera comment effectuer une régression quantile à l'aide de scikit-learn. Nous allons générer deux jeux de données synthétiques pour illustrer la manière dont la régression quantile peut prédire des quantiles conditionnels non triviaux. Nous utiliserons la classe `QuantileRegressor` pour estimer la médiane ainsi qu'un quantile bas et un quantile haut fixés respectivement à 5 % et 95 %. Nous comparerons `QuantileRegressor` avec `LinearRegression` et évaluerons leurs performances en utilisant l'erreur absolue moyenne (MAE) et l'erreur quadratique moyenne (MSE).

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous réglerons rapidement le problème pour vous.
