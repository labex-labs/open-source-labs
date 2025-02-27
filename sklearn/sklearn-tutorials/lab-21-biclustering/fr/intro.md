# Introduction

Le biclustering est une méthode qui effectue simultanément le regroupement des lignes et des colonnes d'une matrice de données. Cela nous permet d'identifier des sous-matrices dans la matrice de données qui ont des propriétés spécifiques. Le biclustering est utile dans divers domaines, y compris l'analyse de données, le traitement d'images et l'informatique bio.

Dans ce laboratoire, nous allons apprendre à effectuer le biclustering à l'aide du module `sklearn.cluster.bicluster` dans scikit-learn. Nous allons explorer deux algorithmes de biclustering courants : le co-clustering spectral et le biclustering spectral. Ces algorithmes diffèrent par la manière dont ils définissent et attribuent les lignes et les colonnes aux biclusters.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous réglerons rapidement le problème pour vous.
