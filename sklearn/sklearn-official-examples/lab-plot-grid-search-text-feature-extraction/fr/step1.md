# Charger les données

Nous allons charger l'ensemble de données 20newsgroups qui est une collection d'environ 20 000 documents de newsgroup répartis en 20 catégories différentes. Pour ce laboratoire, nous nous concentrerons sur deux catégories : alt.atheism et talk.religion.misc.

```python
from sklearn.datasets import fetch_20newsgroups

categories = [
    "alt.atheism",
    "talk.religion.misc",
]

data_train = fetch_20newsgroups(
    subset="train",
    categories=categories,
    shuffle=True,
    random_state=42,
    remove=("headers", "footers", "quotes"),
)

data_test = fetch_20newsgroups(
    subset="test",
    categories=categories,
    shuffle=True,
    random_state=42,
    remove=("headers", "footers", "quotes"),
)

print(f"Chargement de l'ensemble de données 20 newsgroups pour {len(data_train.target_names)} catégories :")
print(data_train.target_names)
print(f"{len(data_train.data)} documents")
```
