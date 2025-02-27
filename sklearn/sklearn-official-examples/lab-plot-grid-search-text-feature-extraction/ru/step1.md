# Загрузка данных

Мы загрузим набор данных 20newsgroups, который представляет собой коллекцию примерно 20 000 новостных документов, разделенных на 20 различных категорий. В этом лабораторном занятии мы сосредоточимся на двух категориях: alt.atheism и talk.religion.misc.

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
