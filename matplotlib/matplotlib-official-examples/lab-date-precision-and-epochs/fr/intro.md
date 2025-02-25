# Introduction

Ceci est un laboratoire étape par étape qui démontre comment gérer la précision des dates et les époques dans Matplotlib. Matplotlib peut travailler avec des objets `.datetime` et des objets `numpy.datetime64` en utilisant un convertisseur d'unités qui reconnaît ces dates et les convertit en nombres à virgule flottante. Avant Matplotlib 3.3, la valeur par défaut de cette conversion renvoyait un nombre à virgule flottante correspondant au nombre de jours depuis "0000-12-31T00:00:00". Depuis Matplotlib 3.3, la valeur par défaut est le nombre de jours depuis "1970-01-01T00:00:00". Cela permet une plus grande résolution pour les dates modernes.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder au carnet Jupyter Notebook pour pratiquer.

Parfois, vous devrez peut-être attendre quelques secondes pour que le carnet Jupyter Notebook se charge complètement. La validation des opérations ne peut pas être automatisée en raison des limitations du carnet Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
