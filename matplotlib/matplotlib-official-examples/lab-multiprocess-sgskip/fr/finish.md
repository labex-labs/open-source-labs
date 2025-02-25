# Résumé

Dans ce laboratoire, nous avons appris à utiliser la bibliothèque `multiprocessing` et Matplotlib pour tracer des données générées à partir d'un processus séparé. Nous avons créé deux classes - `ProcessPlotter` et `NBPlot` - pour gérer respectivement le tracé et la génération de données. La classe `NBPlot` a généré des données aléatoires et les a envoyées à la classe `ProcessPlotter` via un tube, qui a ensuite tracé les données en temps réel.
