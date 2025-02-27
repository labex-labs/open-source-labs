# Introduction

La détection de nouveauté et d'anomalies est un ensemble de techniques permettant d'identifier si une nouvelle observation appartient à la même distribution que les observations existantes ou si elle doit être considérée comme différente. Ces techniques sont couramment utilisées pour nettoyer des jeux de données réels en identifiant les observations anormales ou inhabituelles.

Il existe deux distinctions importantes dans ce contexte :

1. La détection d'anomalies : Les données d'entraînement contiennent des anomalies, qui sont des observations éloignées des autres. Les estimateurs de détection d'anomalies tentent d'ajuster les régions où les données d'entraînement sont les plus concentrées, en ignorant les observations aberrantes.
2. La détection de nouveauté : Les données d'entraînement ne sont pas polluées par des anomalies, et l'objectif est de détecter si une nouvelle observation est une anomalie. Dans ce contexte, une anomalie est également appelée nouveauté.

Le projet scikit-learn fournit un ensemble d'outils d'apprentissage automatique qui peuvent être utilisés pour la détection de nouveauté et d'anomalies. Ces outils sont implémentés à l'aide d'algorithmes d'apprentissage non supervisé, ce qui signifie qu'ils apprennent des modèles à partir des données sans avoir besoin d'exemples étiquetés.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder à Jupyter Notebook et pratiquer.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
