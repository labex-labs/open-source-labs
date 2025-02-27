# Introduction

Dans ce laboratoire, nous allons apprendre à effectuer la sélection de modèles avec des modèles de mélange gaussien (GMM) en utilisant des critères d'information théorique. La sélection de modèles concerne à la fois le type de covariance et le nombre de composants dans le modèle. Nous utiliserons le critère d'information d'Akaike (AIC) et le critère d'information bayésien (BIC) pour sélectionner le meilleur modèle. Nous allons générer deux composants en échantillonnant aléatoirement la distribution normale standard. Un composant est conservé sphérique mais déplacé et redimensionné. L'autre est déformé pour avoir une matrice de covariance plus générale.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder au carnet Jupyter pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que le carnet Jupyter ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limitations du carnet Jupyter.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous réglerons rapidement le problème pour vous.
