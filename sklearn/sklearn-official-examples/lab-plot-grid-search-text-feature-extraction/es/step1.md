# Cargar datos

Cargaremos el conjunto de datos 20newsgroups, que es una colección de aproximadamente 20.000 documentos de grupos de noticias en 20 categorías diferentes. Para este laboratorio, nos centraremos en dos categorías: alt.atheism y talk.religion.misc.

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

print(f"Cargando el conjunto de datos 20 newsgroups para {len(data_train.target_names)} categorías:")
print(data_train.target_names)
print(f"{len(data_train.data)} documentos")
```
