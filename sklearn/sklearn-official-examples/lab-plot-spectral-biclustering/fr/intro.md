# Introduction

Dans ce laboratoire, nous utiliserons l'algorithme de biclustering spectral pour regrouper des données en considérant simultanément les lignes (échantillons) et les colonnes (caractéristiques) d'une matrice. Son but est d'identifier des modèles non seulement entre les échantillons, mais également au sein de sous-ensembles d'échantillons, permettant de détecter une structure localisée dans les données. Cela rend le biclustering spectral particulièrement adapté à des ensembles de données où l'ordre ou l'arrangement des caractéristiques est fixe, comme dans les images, les séries temporelles ou les génomes. Nous utiliserons la bibliothèque scikit-learn pour générer un ensemble de données en damier et le regrouper en biclusters à l'aide de l'algorithme de biclustering spectral.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder au carnet Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que le carnet Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations du carnet Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous résoudrons rapidement le problème pour vous.
