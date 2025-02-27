# Introduction

Dans ce laboratoire, nous allons apprendre à transformer un signal en une combinaison sparse d'ondelettes de Ricker en utilisant des méthodes de codage sparse. Le Ricker (également connu sous le nom de chapeau mexicain ou la seconde dérivée d'un Gaussien) n'est pas un noyau particulièrement adapté pour représenter des signaux piecewise constants comme celui-ci. On peut donc voir combien l'ajout d'atomes de différentes largeurs compte et cela justifie donc l'apprentissage du dictionnaire pour adapter le mieux possible votre type de signaux.

Nous comparerons visuellement différentes méthodes de codage sparse en utilisant l'estimateur `SparseCoder`. Le dictionnaire plus riche à droite n'est pas plus grand en taille, une sous-échantillonnage plus important est effectué pour rester dans le même ordre de grandeur.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session et nous résoudrons rapidement le problème pour vous.
