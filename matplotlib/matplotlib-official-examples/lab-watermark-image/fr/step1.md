# Création d'un Jupyter Notebook et importation des bibliothèques nécessaires

Dans la première cellule de votre notebook, entrez le code suivant pour importer les bibliothèques nécessaires :

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
```

Comprenons ce que chaque bibliothèque fait :

- `matplotlib.pyplot` (alias `plt`) : Une collection de fonctions qui font fonctionner matplotlib comme MATLAB, offrant une interface pratique pour créer des graphiques.
- `numpy` (alias `np`) : Un package fondamental pour le calcul scientifique en Python, que nous utiliserons pour la manipulation de données.
- `matplotlib.cbook` : Une collection de fonctions utilitaires pour matplotlib, y compris des fonctions pour obtenir des données d'exemple.
- `matplotlib.image` : Un module pour les fonctionnalités liées aux images dans matplotlib, que nous utiliserons pour lire et afficher des images.

Exécutez la cellule en cliquant sur le bouton "Run" en haut du notebook ou en appuyant sur Shift+Enter.

![libraries-imported](../assets/screenshot-20250306-18gJ6FRZ@2x.png)

L'exécution de cette cellule devrait se terminer sans aucun affichage, ce qui indique que toutes les bibliothèques ont été importées avec succès.
