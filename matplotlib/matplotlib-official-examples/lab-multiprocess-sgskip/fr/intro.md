# Introduction

Dans ce laboratoire, vous allez apprendre à utiliser la bibliothèque `multiprocessing` et Matplotlib pour tracer des données générées à partir d'un processus séparé. Nous allons créer deux classes - `ProcessPlotter` et `NBPlot` - pour gérer respectivement le tracé et la génération de données. La classe `NBPlot` générera des données aléatoires et les enverra à la classe `ProcessPlotter` via un tube, qui tracerra ensuite les données en temps réel.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous réglerons rapidement le problème pour vous.
