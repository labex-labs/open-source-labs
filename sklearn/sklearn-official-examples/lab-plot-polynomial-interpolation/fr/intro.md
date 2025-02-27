# Introduction

Dans ce laboratoire, nous allons apprendre à approximer une fonction avec des polynômes jusqu'à un certain degré en utilisant la régression ridge. Nous allons montrer deux manières différentes de le faire étant donné `n_samples` de points 1D `x_i` :

1. `PolynomialFeatures` : génère tous les monômes jusqu'à un degré spécifié. Cela nous donne la matrice de Vandermonde avec `n_samples` lignes et `degree + 1` colonnes.
2. `SplineTransformer` : génère des fonctions de base B-spline. Une fonction de base d'une B-spline est une fonction polynomiale par morceaux de degré `degree` qui n'est non-nulle que entre `degree+1` noeuds consécutifs.

Nous utiliserons la fonction `make_pipeline` pour ajouter des fonctionnalités non linéaires et montrer comment ces transformateurs sont bien adaptés pour modéliser les effets non linéaires avec un modèle linéaire. Nous tracerons la fonction, les points d'entraînement et l'interpolation en utilisant les fonctionnalités polynômiales et les B-splines. Nous tracerons également toutes les colonnes des deux transformateurs séparément et montrerons les noeuds de la spline. Enfin, nous démontrerons l'utilisation de splines périodiques.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous réglerons rapidement le problème pour vous.
