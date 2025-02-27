# データの読み込み

ここでは、20 の異なるカテゴリにまたがる約 20,000 のニュースグループ文書のコレクションである 20newsgroups データセットを読み込みます。この実験では、2 つのカテゴリ、`alt.atheism` と `talk.religion.misc` に焦点を当てます。

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
