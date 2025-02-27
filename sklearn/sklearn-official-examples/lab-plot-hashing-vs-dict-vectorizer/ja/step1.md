# データの読み込み

`20newsgroups_dataset` からデータを読み込みます。これは、20のトピックに関する約18,000のニュースグループ投稿から構成されており、2つのサブセットに分割されています。1つは学習用、もう1つはテスト用です。簡単のために計算コストを削減するため、7つのトピックのサブセットを選択し、学習セットのみを使用します。

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
