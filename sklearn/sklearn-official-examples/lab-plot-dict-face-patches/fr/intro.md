# Introduction

Ce laboratoire montre comment utiliser l'API scikit-learn pour traiter un grand ensemble de données d'images de visages et apprendre un ensemble de patches d'images de 20 x 20 représentant des visages. L'aspect clé de ce laboratoire est l'utilisation de l'apprentissage en ligne, où nous chargeons et traitons les images une par une et extraisons 50 patches aléatoires de chaque image. Nous accumulons 500 patches (à partir de 10 images) puis exécutons la méthode partial_fit de l'objet MiniBatchKMeans pour le KMeans en ligne.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session et nous résoudrons rapidement le problème pour vous.
