# Daten laden

Wir werden den 20newsgroups-Datensatz laden, der eine Sammlung von etwa 20.000 Newsgroup-Dokumenten in 20 verschiedenen Kategorien ist. Für dieses Lab konzentrieren wir uns auf zwei Kategorien: alt.atheism und talk.religion.misc.

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

print(f"Laden des 20 newsgroups-Datensatzes für {len(data_train.target_names)} Kategorien:")
print(data_train.target_names)
print(f"{len(data_train.data)} Dokumente")
```