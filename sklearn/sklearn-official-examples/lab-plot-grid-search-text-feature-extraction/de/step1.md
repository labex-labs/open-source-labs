# Daten laden

Wir werden den 20newsgroups-Datensatz laden, der eine Sammlung von ungefähr 20.000 Newsgroup-Dokumenten in 20 verschiedenen Kategorien ist. In diesem Lab werden wir uns auf zwei Kategorien konzentrieren: alt.atheism und talk.religion.misc.

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

print(f"Loading 20 newsgroups dataset for {len(data_train.target_names)} categories:")
print(data_train.target_names)
print(f"{len(data_train.data)} documents")
```
