# Introduction

Ce tutoriel montre l'utilisation de différents types de covariance pour les modèles de mélange gaussien (GMM). Les GMM sont souvent utilisés pour le regroupement, et nous pouvons comparer les groupes obtenus avec les classes réelles du jeu de données. Nous initialisons les moyennes des Gaussiennes avec les moyennes des classes de l'ensemble d'entraînement pour que cette comparaison soit valide. Nous traçons les étiquettes prédites sur les données d'entraînement et de test de validation en utilisant différents types de covariance GMM sur l'ensemble de données iris. Nous comparons les GMM avec des matrices de covariance sphérique, diagonale, complète et liée dans l'ordre croissant de performance.

Bien que l'on s'attende à ce que la covariance complète offre généralement les meilleures performances, elle tend à surajuster sur de petits jeux de données et ne généralise pas bien aux données de test de validation.

Sur les graphiques, les données d'entraînement sont représentées par des points, tandis que les données de test sont représentées par des croix. L'ensemble de données iris est à quatre dimensions. Seules les deux premières dimensions sont montrées ici, et donc certains points sont séparés dans les autres dimensions.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder à Jupyter Notebook pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que Jupyter Notebook ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations de Jupyter Notebook.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
