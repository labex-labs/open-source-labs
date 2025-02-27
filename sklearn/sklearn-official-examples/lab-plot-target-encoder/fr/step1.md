# Chargement des données à partir d'OpenML

Tout d'abord, nous chargeons l'ensemble de données d'évaluations de vins à l'aide de la fonction `fetch_openml` du module `scikit - learn.datasets`. Nous n'utiliserons que sous - ensemble de fonctionnalités numériques et catégorielles dans les données. Nous utiliserons le sous - ensemble suivant de fonctionnalités numériques et catégorielles dans les données : `caractéristiques_numériques = ["prix"]` et `caractéristiques_catégorielles = ["pays", "province", "région_1", "région_2", "variété", "vignoble"]`.
