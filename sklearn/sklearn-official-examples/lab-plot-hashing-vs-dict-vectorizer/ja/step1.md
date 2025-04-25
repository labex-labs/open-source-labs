# データの読み込み

`20newsgroups_dataset` からデータを読み込みます。これは、20 のトピックに関する約 18,000 のニュースグループ投稿から構成されており、2 つのサブセットに分割されています。1 つは学習用、もう 1 つはテスト用です。簡単のために計算コストを削減するため、7 つのトピックのサブセットを選択し、学習セットのみを使用します。

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

print("Loading 20 newsgroups training data")
raw_data, _ = fetch_20newsgroups(subset="train", categories=categories, return_X_y=True)
data_size_mb = sum(len(s.encode("utf-8")) for s in raw_data) / 1e6
print(f"{len(raw_data)} documents - {data_size_mb:.3f}MB")
```
