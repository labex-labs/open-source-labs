# Introduction

Dans ce laboratoire, nous utiliserons la méthode d'empilement pour combiner plusieurs estimateurs afin de faire des prédictions. Dans cette stratégie, certains estimateurs sont ajustés individuellement sur une partie des données d'entraînement tandis qu'un estimateur final est entraîné à l'aide des prédictions empilées de ces estimateurs de base. Nous utiliserons le jeu de données Ames Housing pour prédire le prix logarithmique final des maisons. Nous utiliserons 3 apprenants, linéaires et non linéaires, et utiliserons un régresseur ridge pour combiner leurs sorties. Nous comparerons également les performances de chaque prédicteur individuel ainsi que celles de la pile de régresseurs.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous résoudrons rapidement le problème pour vous.
