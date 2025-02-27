# Introduction

Ce laboratoire montre comment utiliser la régression quantile pour créer des intervalles de prédiction à l'aide de scikit-learn. Nous allons générer des données synthétiques pour un problème de régression, appliquer la fonction à ces données et créer des observations de la variable cible en utilisant une distribution lognormale. Nous allons ensuite diviser les données en ensembles d'entraînement et de test, ajuster des régresseurs quantiles non linéaires et de moindres carrés, et créer un ensemble d'évaluation régulièrement espacé de valeurs d'entrée couvrant la plage [0, 10]. Nous comparerons la médiane prédite avec la moyenne prédite, analyserons les métriques d'erreur et calibrerons l'intervalle de confiance. Enfin, nous allons régler les hyperparamètres des régresseurs quantiles.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous réglerons rapidement le problème pour vous.
