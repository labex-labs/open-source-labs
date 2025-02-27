# Charger les données

Nous allons charger les données à partir de `20newsgroups_dataset`, qui comprend environ 18000 messages de newsgroups sur 20 sujets divisés en deux sous-ensembles : l'un pour l'entraînement et l'autre pour le test. Pour simplifier et réduire le coût de calcul, nous sélectionnons un sous-ensemble de 7 sujets et n'utilisons que l'ensemble d'entraînement.

```python
from sklearn.datasets import fetch_20newsgroups

categories = [
    "alt.atheism",
    "comp.graphics",
    "comp.sys.ibm.pc.hardware",
    "misc.forsale",
    "rec.autos",
    "sci.space",
    "talk.religion.misc",
]

print("Chargement des données d'entraînement des 20 newsgroups")
raw_data, _ = fetch_20newsgroups(subset="train", categories=categories, return_X_y=True)
data_size_mb = sum(len(s.encode("utf-8")) for s in raw_data) / 1e6
print(f"{len(raw_data)} documents - {data_size_mb:.3f}MB")
```
