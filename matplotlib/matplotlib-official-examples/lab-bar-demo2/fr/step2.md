# Création des données pour le graphique en barres

Dans cette étape, nous devons créer les données pour le graphique en barres. Nous utiliserons la bibliothèque numpy pour créer un tableau de valeurs que nous utiliserons pour le graphique en barres.

```python
from basic_units import cm, inch

cms = cm * np.arange(0, 10, 2)
bottom = 0 * cm
width = 0.8 * cm
```
