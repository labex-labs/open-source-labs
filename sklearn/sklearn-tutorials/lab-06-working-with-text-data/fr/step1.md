# Chargement des données textuelles

Tout d'abord, nous devons charger les données textuelles avec lesquelles nous allons travailler. Nous allons utiliser l'ensemble de données 20 Newsgroups, qui contient des articles de presse provenant de vingt sujets différents. Pour charger l'ensemble de données, nous pouvons utiliser la fonction `fetch_20newsgroups` de scikit-learn.

```python
from sklearn.datasets import fetch_20newsgroups

# Charge l'ensemble de données
categories = ['alt.atheism','soc.religion.christian', 'comp.graphics','sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
```

Maintenant que nous avons chargé les données, nous pouvons explorer sa structure et son contenu.
