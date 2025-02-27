# Introduction

Dans ce laboratoire, nous utiliserons l'algorithme de co-classement spectral sur l'ensemble de données des vingt groupes de news pour effectuer un co-classement bicluster des documents. L'ensemble de données contient 20 catégories de documents et nous exclurons la catégorie "comp.os.ms-windows.misc" car elle contient des messages sans données. Les messages vectorisés TF-IDF forment une matrice de fréquence de mots qui est ensuite co-classée bicluster en utilisant l'algorithme de co-classement spectral de Dhillon. Les co-classements bicluster document-mot résultants indiquent des sous-ensembles de mots utilisés plus fréquemment dans ces sous-ensembles de documents. Nous allons également regrouper les documents en utilisant MiniBatchKMeans pour la comparaison.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session et nous réglerons rapidement le problème pour vous.
