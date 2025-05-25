# Carregar Dados

Vamos carregar o conjunto de dados 20newsgroups, que é uma coleção de aproximadamente 20.000 documentos de grupos de notícias em 20 categorias diferentes. Neste laboratório, iremos concentrar-nos em duas categorias: alt.atheism e talk.religion.misc.

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

print(f"Carregando conjunto de dados 20 newsgroups para {len(data_train.target_names)} categorias:")
print(data_train.target_names)
print(f"{len(data_train.data)} documentos")
```
