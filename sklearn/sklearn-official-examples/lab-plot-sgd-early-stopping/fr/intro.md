# Introduction

La descente de gradient stochastique est une technique d'optimisation populaire utilisée pour minimiser une fonction de perte. La technique effectue la descente de gradient étape par étape de manière stochastique, c'est-à-dire en sélectionnant aléatoirement des échantillons à chaque itération. La méthode est efficace, en particulier pour ajuster des modèles linéaires. Cependant, la convergence n'est pas garantie à chaque itération, et la fonction de perte ne diminue pas nécessairement à chaque itération. Dans ce cas, il peut être difficile de surveiller la convergence sur la fonction de perte. Dans ce laboratoire, nous explorerons la stratégie d'arrêt précoce, qui est une approche pour surveiller la convergence sur un score de validation. Nous utiliserons le modèle `SGDClassifier` de la bibliothèque scikit-learn et l'ensemble de données MNIST pour illustrer comment l'arrêt précoce peut être utilisé pour obtenir presque la même précision qu'un modèle construit sans arrêt précoce, et réduire considérablement le temps d'entraînement.

## Conseils sur la VM

Une fois le démarrage de la VM terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
