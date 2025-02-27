# Introduction

Ce laboratoire montre comment utiliser la classe `BayesianGaussianMixture` de scikit-learn pour ajuster un jeu de données d'entraînement contenant un mélange de trois Gaussiennes. Cette classe peut adapter automatiquement le nombre de composants de mélange en utilisant une loi a priori de concentration, qui est spécifiée en utilisant le paramètre `weight_concentration_prior_type`. Ce laboratoire montre la différence entre l'utilisation d'une loi a priori de distribution de Dirichlet et d'un processus de Dirichlet pour sélectionner le nombre de composants avec des poids non nuls.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder au carnet Jupyter pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que le carnet Jupyter ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations du carnet Jupyter.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
