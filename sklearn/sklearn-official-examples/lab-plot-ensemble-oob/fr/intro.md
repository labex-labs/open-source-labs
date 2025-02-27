# Introduction

Dans ce laboratoire, nous allons démontrer comment mesurer le taux d'erreur hors-bag (OOB) pour un modèle Random Forest à l'aide de la bibliothèque scikit-learn en Python. Le taux d'erreur hors-bag est la moyenne des erreurs pour chaque observation d'entraînement calculée à partir des prédictions des arbres qui ne contiennent pas l'observation dans leur échantillonnage bootstrap respectif. Cela permet d'ajuster et de valider le modèle Random Forest pendant l'entraînement.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous résoudrons rapidement le problème pour vous.
