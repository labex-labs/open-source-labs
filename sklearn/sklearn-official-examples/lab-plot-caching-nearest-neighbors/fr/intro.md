# Introduction

Ce laboratoire montre comment pré-calculer les k plus proches voisins avant de les utiliser dans KNeighborsClassifier. KNeighborsClassifier peut calculer les plus proches voisins en interne, mais le fait de les pré-calculer peut présenter plusieurs avantages, tels qu'un contrôle plus fin des paramètres, la mise en cache pour une utilisation multiple ou des implémentations personnalisées. Ici, nous utilisons la propriété de mise en cache des pipelines pour mettre en cache le graphe des plus proches voisins entre plusieurs ajustements de KNeighborsClassifier.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder au carnet Jupyter pour pratiquer.

Parfois, vous devrez attendre quelques secondes pour que le carnet Jupyter ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations du carnet Jupyter.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
