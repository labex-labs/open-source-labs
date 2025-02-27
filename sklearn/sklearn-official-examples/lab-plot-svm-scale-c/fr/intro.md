# Introduction

Ce laboratoire démontre l'effet de la mise à l'échelle du paramètre de régularisation lors de l'utilisation de Machines à Vecteurs de Support (SVM) pour la classification. En classification SVM, nous sommes intéressés par la minimisation du risque pour l'équation :

```math
C \sum_{i=1, n} \mathcal{L} (f(x_i), y_i) + \Omega (w)
```

où :

- `C` est utilisé pour définir la quantité de régularisation
- `L` est une fonction de perte de nos échantillons et de nos paramètres de modèle.
- `Ω` est une fonction de pénalité de nos paramètres de modèle

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder au carnet Jupyter pour la pratique.

Parfois, vous devrez peut-être attendre quelques secondes pour que le carnet Jupyter ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites du carnet Jupyter.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous résoudrons rapidement le problème pour vous.
