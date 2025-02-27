# Introduction

Dans ce laboratoire, nous explorerons l'utilisation d'une estimation de covariance robuste avec des distances de Mahalanobis sur des données distribuées selon une loi normale. La distance de Mahalanobis est une mesure de la distance entre un point et une distribution. Elle est définie comme la distance entre un point et la moyenne de la distribution, mise à l'échelle par l'inverse de la matrice de covariance de la distribution. Pour des données distribuées selon une loi normale, la distance de Mahalanobis peut être utilisée pour calculer la distance d'une observation au mode de la distribution. Nous comparerons les performances de l'estimateur de déterminant de covariance minimum (MCD), un estimateur robuste de covariance, avec l'estimateur maximum de vraisemblance (MLE) de covariance standard dans le calcul des distances de Mahalanobis d'un ensemble de données contaminé.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder au carnet Jupyter pour pratiquer.

Parfois, vous devrez peut-être attendre quelques secondes pour que le carnet Jupyter ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations du carnet Jupyter.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez des commentaires après la session, et nous résoudrons rapidement le problème pour vous.
