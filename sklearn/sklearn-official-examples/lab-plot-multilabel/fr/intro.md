# Introduction

Ce laboratoire démontre un problème de classification de documents multi-étiquettes à l'aide de scikit-learn. Le jeu de données est généré aléatoirement selon le processus suivant :

- Choisissez le nombre d'étiquettes : n ~ Poisson(n_labels)
- N fois, choisissez une classe c : c ~ Multinomial(theta)
- Choisissez la longueur du document : k ~ Poisson(length)
- K fois, choisissez un mot : w ~ Multinomial(theta_c)

Dans ce processus, l'échantillonnage par rejet est utilisé pour s'assurer que n est supérieur à 2 et que la longueur du document n'est jamais nulle. De même, les classes déjà choisies sont rejetées. Les documents assignés à les deux classes sont tracés entourés de deux cercles colorés.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session et nous résoudrons rapidement le problème pour vous.
